#include <Arduino.h>

// Definição dos pinos
#define SENSOR_PIN A0  // Pino do sensor analógico
#define RELE_PIN 7     // Pino do relé

// Valor limite para ativação do relé
const int LIMIAR = 500;

void setup() {
    pinMode(SENSOR_PIN, INPUT);
    pinMode(RELE_PIN, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    int sensorValue = analogRead(SENSOR_PIN);
    Serial.print("Valor do sensor: ");
    Serial.println(sensorValue);

    // Lógica de acionamento do relé
    if (sensorValue > LIMIAR) {
        digitalWrite(RELE_PIN, HIGH); // Liga o relé
        Serial.println("Relé ativado!");
    } else {
        digitalWrite(RELE_PIN, LOW); // Desliga o relé
        Serial.println("Relé desativado!");
    }

    delay(1000); // Pequena pausa para evitar leituras excessivas
}