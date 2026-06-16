#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <DHT.h>

#define LCD_COLUMNS 16
#define LCD_ROWS 2
#define LCD_ADDRESS 0x27

#define DHTPIN 2
#define DHTTYPE DHT11

LiquidCrystal_I2C lcd(LCD_ADDRESS, LCD_COLUMNS, LCD_ROWS);
DHT dht(DHTPIN, DHTTYPE);

const char* CANDIDATE_NAME = "MUHIZI Lilian Brian";

const unsigned long SCROLL_DELAY = 300;
const unsigned long READ_INTERVAL = 2000;

unsigned long previousScrollMillis = 0;
unsigned long previousReadMillis = 0;

int scrollPosition = 0;


void setup() {

  Serial.begin(9600);

  lcd.init();
  lcd.backlight();

  dht.begin();

  delay(1000);
}


void displayScrollingName() {

  unsigned long currentMillis = millis();
  int nameLength = strlen(CANDIDATE_NAME);


  if (currentMillis - previousScrollMillis >= SCROLL_DELAY) {

    previousScrollMillis = currentMillis;

    lcd.setCursor(0, 0);


    if (nameLength <= LCD_COLUMNS) {

      lcd.print(CANDIDATE_NAME);

      for (int i = nameLength; i < LCD_COLUMNS; i++) {
        lcd.print(" ");
      }

    } else {

      for (int i = 0; i < LCD_COLUMNS; i++) {

        int index = (scrollPosition + i) % (nameLength + LCD_COLUMNS);

        if (index < nameLength) {
          lcd.print(CANDIDATE_NAME[index]);
        } else {
          lcd.print(" ");
        }
      }


      scrollPosition++;

      if (scrollPosition >= nameLength + LCD_COLUMNS) {
        scrollPosition = 0;
      }
    }
  }
}


void loop() {

  displayScrollingName();


  unsigned long currentMillis = millis();


  if (currentMillis - previousReadMillis >= READ_INTERVAL) {

    previousReadMillis = currentMillis;


    float temperature = dht.readTemperature();


    if (!isnan(temperature)) {

      lcd.setCursor(0, 1);
      lcd.print("Temp: ");
      lcd.print(temperature, 1);
      lcd.print(" C    ");


      Serial.print("Temperature: ");
      Serial.print(temperature, 1);
      Serial.println(" C");


    } else {

      lcd.setCursor(0, 1);
      lcd.print("Temp: Error   ");

      Serial.println("DHT11 ERROR");
    }
  }
}