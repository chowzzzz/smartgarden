#include <dht.h>    // dht lib

dht DHT;    // initialise dht sensor

#define DHT11_PIN 7

int soilValue = 0;    // set soil moisture value to 0
int soilPin = A0;        // set soil sensor to A0
int chk;
float temp;
float hum;
int ldrValue;
int redLEDPin = 13;     // set red led to pin 13 (water)
int yellowLEDPin = 12;  // set yellow led to pin 12 (ldr)
int ldrPin = A1;        // set ldr to A1
int motorPin = 3;       // set motor to pin 3
/* 'A': auto
   'M': manual
   'O': on
   'F': off
*/
char status;
int lightLevel;

void setup() {
  Serial.begin(9600);
  //Serial.println("Soil Moisture Sensor start reading");
  pinMode(redLEDPin, OUTPUT);
  pinMode(yellowLEDPin, OUTPUT);
  pinMode(ldrPin, INPUT);
  pinMode(motorPin, OUTPUT);
  
  delay (2000);
  }

void loop() {
  // Receive data from server
  if (Serial.available() ) {
    status = Serial.read();
  }
  
  chk = DHT.read11(DHT11_PIN);
  temp = DHT.temperature;
  hum = DHT.humidity;  
  soilValue = analogRead(soilPin);
  ldrValue = analogRead(ldrPin);
  
  Serial.println(temp);
  Serial.println(hum);
  Serial.println(soilValue);
  Serial.println(ldrValue);
  
  if (status == 'A') {
    if (soilValue > 500) {
      analogWrite(motorPin, 200);
      digitalWrite(redLEDPin, HIGH);
    } else {
      digitalWrite(redLEDPin, LOW);
      analogWrite(motorPin, LOW);
    }
  } else if (status == 'M' || status == 'F') {
    if (soilValue > 500) {
      analogWrite(motorPin, LOW);
      digitalWrite(redLEDPin, HIGH);
    } else {
      digitalWrite(redLEDPin, LOW);
      analogWrite(motorPin, LOW);
    }
  } else if (status == 'O') {
    if (soilValue > 500) {
      digitalWrite(redLEDPin, HIGH);
    } else {
      digitalWrite(redLEDPin, LOW);
    }
    analogWrite(motorPin, 200);
  } else {
    if (soilValue > 500) {
      digitalWrite(redLEDPin, HIGH);
    } else {
      digitalWrite(redLEDPin, LOW);
    }
    analogWrite(motorPin, LOW);
  }
  
  if (ldrValue>=300) {
    digitalWrite(yellowLEDPin, HIGH);
  } else {
    digitalWrite(yellowLEDPin, LOW);
  }
  delay(4000);
}

