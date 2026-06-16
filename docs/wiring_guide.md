
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
| VCC       | 3.3V        | Power (from digital pin) |



## Wiring Diagram (Textual Representation)

```
          +-----------------+
          |   Arduino Uno   |
          +-----------------+
                 | | | | |
         GND----+ | | | +----5V
                 | | | |
          A4-----+ | +------3.3V
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

