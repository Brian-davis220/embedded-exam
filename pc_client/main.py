
import os
import time
import logging
from dotenv import load_dotenv
import serial
import serial.tools.list_ports
import paho.mqtt.client as mqtt

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class TemperatureMonitor:
    def __init__(self):
        load_dotenv()
        
        self.serial_port = os.getenv('SERIAL_PORT')
        self.baud_rate = int(os.getenv('BAUD_RATE', 9600))
        self.mqtt_broker = os.getenv('MQTT_BROKER')
        self.mqtt_port = int(os.getenv('MQTT_PORT', 1883))
        self.mqtt_topic = os.getenv('MQTT_TOPIC', 'temperature/sensor')
        self.client_id = os.getenv('CLIENT_ID', 'pc_client')
        self.mqtt_qos = int(os.getenv('MQTT_QOS', 0))
        self.mqtt_retain = os.getenv('MQTT_RETAIN', 'false').lower() == 'true'
        
        self.ser = None
        self.mqtt_client = None
        self.connected = False
        
        self.setup_mqtt()
        
    def setup_mqtt(self):
        self.mqtt_client = mqtt.Client(client_id=self.client_id)
        self.mqtt_client.on_connect = self.on_mqtt_connect
        self.mqtt_client.on_disconnect = self.on_mqtt_disconnect
        self.mqtt_client.on_publish = self.on_mqtt_publish
        
    def on_mqtt_connect(self, client, userdata, flags, rc):
        if rc == 0:
            logger.info("Connected to MQTT broker successfully")
            self.connected = True
        else:
            logger.error(f"Failed to connect to MQTT broker, return code {rc}")
            self.connected = False
            
    def on_mqtt_disconnect(self, client, userdata, rc):
        logger.warning("Disconnected from MQTT broker")
        self.connected = False
        
    def on_mqtt_publish(self, client, userdata, mid):
        logger.debug(f"Message published with id {mid}")
        
    def connect_mqtt(self):
        try:
            logger.info(f"Connecting to MQTT broker at {self.mqtt_broker}:{self.mqtt_port}")
            self.mqtt_client.connect(self.mqtt_broker, self.mqtt_port, 60)
            self.mqtt_client.loop_start()
        except Exception as e:
            logger.error(f"Error connecting to MQTT broker: {e}")
            
    def connect_serial(self):
        while not self.ser:
            try:
                logger.info(f"Connecting to serial port {self.serial_port} at {self.baud_rate} baud")
                self.ser = serial.Serial(self.serial_port, self.baud_rate, timeout=1)
                logger.info("Serial port connected successfully")
            except Exception as e:
                logger.error(f"Error connecting to serial port: {e}")
                logger.info("Retrying in 5 seconds...")
                time.sleep(5)
                
    def publish_temperature(self, temperature):
        if self.connected:
            try:
                result = self.mqtt_client.publish(
                    self.mqtt_topic,
                    temperature,
                    qos=self.mqtt_qos,
                    retain=self.mqtt_retain
                )
                if result.rc == mqtt.MQTT_ERR_SUCCESS:
                    logger.info(f"Published temperature: {temperature}")
                else:
                    logger.error(f"Failed to publish temperature: {result.rc}")
            except Exception as e:
                logger.error(f"Error publishing temperature: {e}")
        else:
            logger.warning("Not connected to MQTT broker, trying to reconnect")
            self.connect_mqtt()
            
    def validate_temperature(self, data):
        try:
            temp = float(data.strip())
            return temp
        except ValueError:
            return None
            
    def run(self):
        self.connect_mqtt()
        self.connect_serial()
        
        while True:
            try:
                if self.ser.in_waiting:
                    line = self.ser.readline().decode('utf-8').strip()
                    if line:
                        temperature = self.validate_temperature(line)
                        if temperature is not None:
                            logger.info(f"Received temperature: {temperature}")
                            self.publish_temperature(temperature)
                        else:
                            logger.warning(f"Invalid temperature data: {line}")
            except serial.SerialException as e:
                logger.error(f"Serial error: {e}")
                self.ser = None
                self.connect_serial()
            except KeyboardInterrupt:
                logger.info("Exiting...")
                break
            except Exception as e:
                logger.error(f"Unexpected error: {e}")
                time.sleep(1)
                
        if self.ser:
            self.ser.close()
        self.mqtt_client.loop_stop()
        self.mqtt_client.disconnect()
        
if __name__ == "__main__":
    monitor = TemperatureMonitor()
    monitor.run()

