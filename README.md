
# Temperature Display and MQTT Monitoring System

A complete IoT temperature monitoring system for academic embedded systems assignment.

**Candidate:** MUHIZI Lilian Brian

## Project Overview

This project implements a full-stack temperature monitoring solution:

```
DHT11 Sensor → Arduino Uno → 16×2 LCD + USB Serial → Python PC Client → MQTT Broker (VPS) → Web Dashboard
```

## Features

- **Arduino Uno**: Reads temperature from DHT11, displays on 16×2 LCD (with horizontal scrolling for long names), transmits via serial
- **Python PC Client**: Reads serial data, publishes to MQTT broker, displays values in real time in the terminal
- **MQTT Broker**: Mosquitto on Ubuntu VPS
- **Web Dashboard**: Single-page HTML dashboard with real-time temperature gauge, chart, live readings log, and statistics

## Hardware Setup

See [docs/wiring_guide.md](docs/wiring_guide.md) for detailed wiring instructions.

### Quick Wiring Reference

| Component   | Pin  | Arduino Pin |
|-------------|------|-------------|
| LCD GND     | GND  | GND         |
| LCD VCC     | VCC  | 5V          |
| LCD SDA     | SDA  | A4          |
| LCD SCL     | SCL  | A5          |
| DHT11 GND   | GND  | GND         |
| DHT11 DATA  | DATA | D2          |
| DHT11 VCC   | VCC  | D7          |

## Repository Structure

```
Embedded_practical/
├── arduino/
│   └── temperature_monitor.ino      # Arduino program (Part 1)
├── pc_client/
│   └── main.py                      # Python MQTT client (Part 2)
├── dashboard.html                   # Web dashboard (real-time display)
├── docs/
│   ├── system_architecture.md       # System architecture diagram
│   ├── wiring_guide.md              # Hardware wiring guide
│   ├── mqtt_setup.md                # MQTT broker setup
│   └── vps_setup.md                 # VPS configuration
├── screenshots/                     # Execution screenshots
├── requirements.txt                 # Python dependencies
├── .env.example                     # Environment variable template
├── .gitignore
├── LICENSE
└── README.md
```

## Software Setup

### 1. Arduino Setup

1. Install the following libraries in Arduino IDE:
   - **DHT sensor library** by Adafruit
   - **Adafruit Unified Sensor**
   - **LiquidCrystal_I2C**
2. Open `arduino/temperature_monitor.ino`
3. Upload to Arduino Uno

#### LCD Display Behavior
- **Row 1**: Candidate name (`MUHIZI Lilian Brian`) — scrolls horizontally since it exceeds 16 characters
- **Row 2**: Temperature value (e.g., `Temp: 25.3 C`)

### 2. Python PC Client Setup

```bash
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your serial port and MQTT broker details
cd pc_client
python main.py
```

The PC client will:
- Read temperature values from Arduino via serial port
- Publish values to the MQTT broker on the VPS
- Display incoming values in real time in the terminal

### 3. Web Dashboard

Open `dashboard.html` in any browser (or deploy to your VPS). On first load:

1. Click **⚙️ MQTT Settings**
2. Enter your MQTT broker WebSocket URL (e.g., `ws://your-vps-ip:9001`)
3. Set the topic to `temperature/sensor`
4. Click **Connect**

The dashboard displays:
- **Current temperature** with live updates
- **High / Low / Average** statistics
- **Temperature gauge** (0–50 °C range)
- **Temperature history chart** (last 50 readings)
- **Live readings log** with timestamps

> **Note:** The MQTT broker must have WebSocket support enabled (default port 9001 for Mosquitto).

## Communication Protocols

| Link                  | Protocol             | Details                     |
|-----------------------|----------------------|-----------------------------|
| Arduino → PC          | USB Serial (UART)    | 9600 baud                   |
| PC → MQTT Broker      | MQTT v3.1.1 over TCP | Topic: `temperature/sensor` |
| Dashboard → Broker    | MQTT over WebSocket  | Port: 9001                  |

## Documentation

- [System Architecture](docs/system_architecture.md)
- [Wiring Guide](docs/wiring_guide.md)
- [MQTT Setup](docs/mqtt_setup.md)
- [VPS Setup](docs/vps_setup.md)

## Screenshots

Add the following screenshots to the `screenshots/` directory:
- `lcd_display.jpg` — LCD showing candidate name and temperature
- `serial_output.jpg` — Serial monitor / PC client output
- `mqtt_messages.jpg` — MQTT messages being transmitted
- `dashboard.jpg` — Web dashboard showing real-time data

## License

MIT License
