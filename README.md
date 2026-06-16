# Temperature Display and MQTT Monitoring System

A complete IoT temperature monitoring system for an academic embedded systems assignment.

**Candidate:** MUHIZI Lilian Brian

## Project Overview

This project implements a full-stack temperature monitoring solution:

```
DHT11 Sensor → Arduino Uno → 16×2 LCD + USB Serial → Python PC Client → MQTT Broker (VPS) → Web Dashboard
```

## Features

- **Arduino Uno**: Reads temperature from DHT11, displays the candidate name and temperature on a 16×2 LCD, and sends temperature values through USB serial.
- **Python PC Client**: Reads temperature data from Arduino serial communication and publishes values to the MQTT broker.
- **MQTT Broker**: Mosquitto MQTT broker running on an Ubuntu VPS.
- **Web Dashboard**: Displays real-time temperature values, gauge, history chart, statistics, and live readings.

---

# Hardware Setup

See [docs/wiring_guide.md](docs/wiring_guide.md) for detailed wiring instructions.

## Quick Wiring Reference

| Component | Pin | Arduino Pin |
|-----------|-----|-------------|
| LCD GND | GND | GND |
| LCD VCC | VCC | 5V |
| LCD SDA | SDA | A4 |
| LCD SCL | SCL | A5 |
| DHT11 GND | GND | GND |
| DHT11 DATA | DATA | D2 |
| DHT11 VCC | VCC | 3.3V |

The DHT11 sensor is powered directly from the Arduino 3.3V pin.

---

# Repository Structure

```
Embedded_practical/
│
├── arduino/
│   └── temperature_monitor.ino
│
├── pc_client/
│   └── main.py
│
├── dashboard.html
│
├── docs/
│   ├── system_architecture.md
│   ├── wiring_guide.md
│   ├── mqtt_setup.md
│   └── vps_setup.md
│
├── screenshots/
│
├── requirements.txt
├── .env.example
├── .gitignore
├── LICENSE
└── README.md
```

---

# Software Setup

## 1. Arduino Setup

Install the following libraries:

- DHT sensor library by Adafruit
- Adafruit Unified Sensor
- LiquidCrystal_I2C

Open:

```
arduino/temperature_monitor.ino
```

Select:

```
Board: Arduino Uno
Port: Arduino USB Port
```

Upload the sketch.

## LCD Display Behavior

The LCD displays:

### First Row

The candidate name with horizontal scrolling:

```
MUHIZI Lilian Brian
```

### Second Row

The temperature value:

```
Temp: 21.8 C
```

The Arduino sends only the temperature value through serial communication:

Example:

```
21.8
```

---

# 2. Python PC Client Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Create environment file:

```bash
cp .env.example .env
```

Edit `.env`:

```env
SERIAL_PORT=/dev/ttyACM0
BAUD_RATE=9600
MQTT_BROKER=157.173.101.159
MQTT_PORT=1883
MQTT_TOPIC=temperature/sensor
CLIENT_ID=pc_client_001
MQTT_QOS=0
MQTT_RETAIN=false
```

Run the client:

```bash
python3 pc_client/main.py
```

Example successful output:

```
Connecting to MQTT broker at 157.173.101.159:1883
Serial port connected successfully
Connected to MQTT broker successfully
Received temperature: 21.8
Published temperature: 21.8
```

---

# 3. MQTT Broker Setup

The system uses Mosquitto MQTT broker running on the VPS.

## Test MQTT Messages

Subscribe to the temperature topic:

```bash
mosquitto_sub -h 157.173.101.159 -t "temperature/sensor" -v
```

Expected output:

```
temperature/sensor 21.8
```

Publish a test message:

```bash
mosquitto_pub -h 157.173.101.159 -t "temperature/sensor" -m "25.0"
```

---

# 4. Web Dashboard Setup

The dashboard is available as:

```
dashboard.html
```

It can be opened locally or hosted on the VPS.

Open MQTT settings in the dashboard.

Use:

```
Broker Host:
ws://157.173.101.159:9001
```

Topic:

```
temperature/sensor
```

Click:

```
Connect
```

## Dashboard Features

The dashboard displays:

- Current temperature
- Temperature gauge
- Temperature history graph
- Maximum temperature
- Minimum temperature
- Average temperature
- Live temperature readings

---

# Communication Protocols

| Communication Link | Protocol | Details |
|--------------------|----------|---------|
| Arduino → PC | USB Serial (UART) | 9600 baud |
| PC → MQTT Broker | MQTT v3.1.1 | Port 1883 |
| Dashboard → MQTT Broker | MQTT over WebSocket | Port 9001 |

---

# System Architecture

```
              DHT11 Sensor
                   |
                   |
                   v
              Arduino Uno
                   |
          USB Serial (9600 baud)
                   |
                   v
            Python PC Client
                   |
            MQTT TCP Port 1883
                   |
                   v
          Mosquitto MQTT Broker
                   |
        MQTT WebSocket Port 9001
                   |
                   v
            Web Dashboard
```

---

# Documentation

Additional documentation:

- [System Architecture](docs/system_architecture.md)
- [Wiring Guide](docs/wiring_guide.md)
- [MQTT Setup](docs/mqtt_setup.md)
- [VPS Setup](docs/vps_setup.md)

---

# License

MIT License
