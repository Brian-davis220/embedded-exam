
# Wiring Guide

## Hardware Requirements

- Arduino Uno
- 16x2 LCD with I2C backpack
- DHT11 temperature sensor module
- Jumper wires (male-to-male)

## Important Note

No breadboard or power splitter is available. Only one 5V pin is available on Arduino Uno. Therefore:
- LCD is powered directly from Arduino 5V pin
- DHT11 is powered from Arduino digital pin D7 (configured as OUTPUT HIGH)

## Exact Wiring

### LCD (I2C) Connections

| LCD Pin | Arduino Pin | Description |
|---------|-------------|-------------|
| GND     | GND         | Ground |
| VCC     | 5V          | Power (5V) |
| SDA     | A4          | I2C Data Line |
| SCL     | A5          | I2C Clock Line |

### DHT11 Connections

| DHT11 Pin | Arduino Pin | Description |
|-----------|-------------|-------------|
| GND       | GND         | Ground |
| DATA      | D2          | Data Signal |
| VCC       | D7          | Power (from digital pin) |

## Why D7 is Used for DHT11 Power?

The Arduino Uno only has one 5V pin available, which is already used to power the LCD. Since no power splitter or breadboard is available, we use a digital pin to power the DHT11 sensor.

**How it works:**
1. In the Arduino code, we configure pin D7 as an OUTPUT
2. We set D7 to HIGH, which provides approximately 5V (enough to power the DHT11)
3. We wait 1 second for the sensor to stabilize before taking readings

**Important considerations:**
- The DHT11 has low power requirements (~0.5-2.5mA during active reading)
- Arduino digital pins can supply up to 40mA (safely limited to 20mA per pin)
- This method is suitable for this project given the hardware constraints

## Wiring Diagram (Textual Representation)

```
          +-----------------+
          |   Arduino Uno   |
          +-----------------+
                 | | | | |
         GND----+ | | | +----5V
                 | | | |
          A4-----+ | +------D7
                 | |        |
          A5-------+        |
                           |
          +----------------+----------------+
          |                                 |
          v                                 v
    +-----------+                    +-----------+
    | 16x2 LCD  |                    |   DHT11   |
    |  (I2C)    |                    |           |
    +-----------+                    +-----------+
     | | | |                           | | |
     | | | +--- VCC                    | | +--- VCC
     | | +----- SDA                    | +----- DATA
     | +------- SCL                    +------- GND
     +--------- GND
```

## Screenshot Placeholders

Please place the following screenshots in the `screenshots/` directory:

- `lcd_display.jpg`: Photo of LCD showing candidate name and temperature
- `wiring_overview.jpg`: Photo of complete wiring setup

