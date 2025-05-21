#include <Arduino.h>

#define SENSOR_PIN A0  // Sensor analógico
#define RELE_PIN 7     // Pino do relé (bomba d'água)

const int LIMITE = 400;  // Valor de ativação do relé

void setup() {
    pinMode(SENSOR_PIN, INPUT);
    pinMode(RELE_PIN, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    int sensorValue = analogRead(SENSOR_PIN);
    Serial.print("Valor do sensor: ");
    Serial.println(sensorValue);

    // Lógica para ativação da bomba d'água
    if (sensorValue > LIMITE) {
        digitalWrite(RELE_PIN, HIGH); // Liga a bomba
        Serial.println("Bomba ativada!");
    } else {
        digitalWrite(RELE_PIN, LOW); // Desliga a bomba
        Serial.println("Bomba desativada!");
    }

    delay(1000);
}