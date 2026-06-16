
# MQTT Setup Guide

This guide covers MQTT configuration for both the PC client and Node-RED dashboard.

## MQTT Broker Information

- Default Port: 1883
- Default Topic: `temperature/sensor`
- QoS Levels: 0, 1, or 2 (configurable)

## PC Client Configuration

1. Copy the example environment file:

```bash
cp .env.example .env
```

2. Edit `.env` with your settings:

```
SERIAL_PORT=/dev/ttyUSB0          # Your serial port (Windows: COM3, Mac: /dev/tty.usbmodem*)
BAUD_RATE=9600
MQTT_BROKER=your-vps-ip           # Replace with your VPS IP
MQTT_PORT=1883
MQTT_TOPIC=temperature/sensor
CLIENT_ID=pc_client_001
MQTT_QOS=0
MQTT_RETAIN=false
```

### Finding Your Serial Port

**Linux:**
```bash
ls /dev/ttyUSB*
ls /dev/ttyACM*
```

**Windows:**
Check Device Manager → Ports (COM & LPT)

**Mac:**
```bash
ls /dev/tty.usbmodem*
ls /dev/tty.usbserial*
```

## Testing MQTT

### Using Mosquitto Clients

**Subscribe to topic:**
```bash
mosquitto_sub -h your-vps-ip -t "temperature/sensor" -v
```

**Publish test message:**
```bash
mosquitto_pub -h your-vps-ip -t "temperature/sensor" -m "25.0"
```

## Node-RED MQTT Configuration

1. Open Node-RED at `http://your-vps-ip:1880`
2. Double-click the "MQTT in" node
3. Click the pencil icon next to "Server"
4. Update the server address to your VPS IP
5. Click "Update" and then "Deploy"

## MQTT Message Format

Messages published to the MQTT topic are raw temperature values:

```
24.5
24.6
24.7
```

No labels, units, or extra text - just the numeric value.

## QoS Levels Explained

- **QoS 0 (At most once)**: Message is delivered once or not at all
- **QoS 1 (At least once)**: Message is delivered at least once (may be duplicated)
- **QoS 2 (Exactly once)**: Message is delivered exactly once (safest but slowest)

For this project, QoS 0 is sufficient.

## Retained Messages

If `MQTT_RETAIN=true`, the broker will keep the last published message and send it to new subscribers immediately when they connect.

## Security Considerations (Optional)

For production use, you should:
1. Enable authentication (username/password)
2. Use TLS/SSL (port 8883)
3. Restrict access via firewall
4. Use unique client IDs

