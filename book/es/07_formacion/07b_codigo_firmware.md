# Código Completo del Firmware

A continuación se presenta el código completo del firmware desarrollado para el nodo LoRaWAN, listo para ser cargado en el módulo **Heltec LoRa32 V3** mediante PlatformIO o Arduino IDE. El proyecto está dividido en dos archivos principales:

1. `config.h`: Contiene las definiciones de hardware, pines SPI y las claves de sesión de la red LoRaWAN (OTAA).
2. `firmware_lora.ino`: Contiene la lógica principal, lectura de sensores, empaquetado del *payload* y gestión de energía (Deep Sleep).

## 1. Archivo `config.h`

Este archivo concentra toda la configuración de conectividad y pines, facilitando su adaptación a otras placas o redes.

```cpp
#ifndef _RADIOLIB_EX_LORAWAN_CONFIG_H
#define _RADIOLIB_EX_LORAWAN_CONFIG_H

#include <RadioLib.h>
#include <SPI.h>

// =========================
// Hardware
// =========================
// Pines de tu placa:
// SCK  = 5
// MISO = 19
// MOSI = 27
// CS   = 18
// RST  = 23
// DIO0 = 26

SPIClass spi = SPIClass(VSPI);
SX1276 radio = new Module(18, 26, 23, RADIOLIB_NC, spi);

// =========================
// LoRaWAN / TTN
// =========================
const uint32_t uplinkIntervalSeconds = 60UL;   // 1 min

#define RADIOLIB_LORAWAN_JOIN_EUI  0x0000000000000000
#define RADIOLIB_LORAWAN_DEV_EUI   0x70B3D57ED00766B9

#define RADIOLIB_LORAWAN_APP_KEY   \
  0x3E, 0x14, 0x65, 0xCE, 0x00, 0x54, 0xB2, 0xE4, \
  0xEF, 0xBC, 0x5D, 0x05, 0x39, 0x82, 0xA9, 0x79

// Algunas variantes de RadioLib usan beginOTAA(joinEUI, devEUI, nwkKey, appKey)
#define RADIOLIB_LORAWAN_NWK_KEY   \
  0x3E, 0x14, 0x65, 0xCE, 0x00, 0x54, 0xB2, 0xE4, \
  0xEF, 0xBC, 0x5D, 0x05, 0x39, 0x82, 0xA9, 0x79

const LoRaWANBand_t Region = EU868;
const uint8_t subBand = 0;

// =========================
// Objetos
// =========================
uint64_t joinEUI = RADIOLIB_LORAWAN_JOIN_EUI;
uint64_t devEUI  = RADIOLIB_LORAWAN_DEV_EUI;
uint8_t appKey[] = { RADIOLIB_LORAWAN_APP_KEY };
uint8_t nwkKey[] = { RADIOLIB_LORAWAN_NWK_KEY };

LoRaWANNode node(&radio, &Region, subBand);

// =========================
// Helpers
// =========================
String stateDecode(const int16_t result) {
  switch (result) {
    case RADIOLIB_ERR_NONE: return "ERR_NONE";
    case RADIOLIB_ERR_CHIP_NOT_FOUND: return "ERR_CHIP_NOT_FOUND";
    case RADIOLIB_ERR_PACKET_TOO_LONG: return "ERR_PACKET_TOO_LONG";
    case RADIOLIB_ERR_RX_TIMEOUT: return "ERR_RX_TIMEOUT";
    case RADIOLIB_ERR_MIC_MISMATCH: return "ERR_MIC_MISMATCH";
    case RADIOLIB_ERR_INVALID_BANDWIDTH: return "ERR_INVALID_BANDWIDTH";
    case RADIOLIB_ERR_INVALID_SPREADING_FACTOR: return "ERR_INVALID_SPREADING_FACTOR";
    case RADIOLIB_ERR_INVALID_CODING_RATE: return "ERR_INVALID_CODING_RATE";
    case RADIOLIB_ERR_INVALID_FREQUENCY: return "ERR_INVALID_FREQUENCY";
    case RADIOLIB_ERR_INVALID_OUTPUT_POWER: return "ERR_INVALID_OUTPUT_POWER";
    case RADIOLIB_ERR_NETWORK_NOT_JOINED: return "RADIOLIB_ERR_NETWORK_NOT_JOINED";
    case RADIOLIB_ERR_DOWNLINK_MALFORMED: return "RADIOLIB_ERR_DOWNLINK_MALFORMED";
    case RADIOLIB_ERR_INVALID_REVISION: return "RADIOLIB_ERR_INVALID_REVISION";
    case RADIOLIB_ERR_INVALID_PORT: return "RADIOLIB_ERR_INVALID_PORT";
    case RADIOLIB_ERR_NO_RX_WINDOW: return "RADIOLIB_ERR_NO_RX_WINDOW";
    case RADIOLIB_ERR_INVALID_CID: return "RADIOLIB_ERR_INVALID_CID";
    case RADIOLIB_ERR_UPLINK_UNAVAILABLE: return "RADIOLIB_ERR_UPLINK_UNAVAILABLE";
    case RADIOLIB_ERR_COMMAND_QUEUE_FULL: return "RADIOLIB_ERR_COMMAND_QUEUE_FULL";
    case RADIOLIB_ERR_COMMAND_QUEUE_ITEM_NOT_FOUND: return "RADIOLIB_ERR_COMMAND_QUEUE_ITEM_NOT_FOUND";
    case RADIOLIB_ERR_JOIN_NONCE_INVALID: return "RADIOLIB_ERR_JOIN_NONCE_INVALID";
    case RADIOLIB_ERR_DWELL_TIME_EXCEEDED: return "RADIOLIB_ERR_DWELL_TIME_EXCEEDED";
    case RADIOLIB_ERR_CHECKSUM_MISMATCH: return "RADIOLIB_ERR_CHECKSUM_MISMATCH";
    case RADIOLIB_ERR_NO_JOIN_ACCEPT: return "RADIOLIB_ERR_NO_JOIN_ACCEPT";
    case RADIOLIB_LORAWAN_SESSION_RESTORED: return "RADIOLIB_LORAWAN_SESSION_RESTORED";
    case RADIOLIB_LORAWAN_NEW_SESSION: return "RADIOLIB_LORAWAN_NEW_SESSION";
    case RADIOLIB_ERR_NONCES_DISCARDED: return "RADIOLIB_ERR_NONCES_DISCARDED";
    case RADIOLIB_ERR_SESSION_DISCARDED: return "RADIOLIB_ERR_SESSION_DISCARDED";
    default: return "Unknown / RadioLib docs";
  }
}

void debug(bool failed, const __FlashStringHelper* message, int state, bool halt) {
  if (failed) {
    Serial.print(message);
    Serial.print(" - ");
    Serial.print(stateDecode(state));
    Serial.print(" (");
    Serial.print(state);
    Serial.println(")");
    while (halt) {
      delay(1);
    }
  }
}

#endif
```

## 2. Archivo principal `firmware_lora.ino`

El bucle `loop()` está vacío porque toda la lógica sigue un enfoque orientado a eventos y temporizadores. Cuando el dispositivo termina su tarea (leer sensores y enviar datos), programa un temporizador (Deep Sleep) que lo "apaga" durante 60 segundos (según lo configurado en `config.h`) y luego lo reinicia desde `setup()`, ahorrando la máxima cantidad de batería.

```cpp
#include "config.h"
#include "esp_sleep.h"
#include <LoRaWAN_ESP32.h>

#include <BH1750.h>
#include <DallasTemperature.h>
#include <OneWire.h>
#include <Wire.h>

RTC_DATA_ATTR uint32_t bootCount = 0;

// =========================
// Sensores
// =========================
#define SENSOR_POWER 25
#define SOIL_PIN 34
#define ONE_WIRE_BUS 14
#define I2C_SDA 21
#define I2C_SCL 22

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature ds18b20(&oneWire);
BH1750 lightMeter;

// =========================
// Helpers sensores
// =========================
int readSoilRaw() {
  long sum = 0;
  const int samples = 5;

  for (int i = 0; i < samples; i++) {
    sum += analogRead(SOIL_PIN);
    delay(20);
  }

  return sum / samples;
}

float readTemperatureC() {
  ds18b20.begin();
  ds18b20.requestTemperatures();
  delay(750);

  return ds18b20.getTempCByIndex(0);
}

float readLux() {
  Wire.begin(I2C_SDA, I2C_SCL);

  bool ok = lightMeter.begin(BH1750::CONTINUOUS_HIGH_RES_MODE);
  if (!ok) {
    Serial.println(F("BH1750 init FAIL"));
    return 0.0f;
  }

  delay(180);

  float lux = lightMeter.readLightLevel();
  if (lux < 0 || isnan(lux) || isinf(lux)) {
    return 0.0f;
  }

  return lux;
}

void goToDeepSleep() {
  Serial.println();
  Serial.print(F("Guardando sesion y entrando en deep sleep "));
  Serial.print(uplinkIntervalSeconds);
  Serial.println(F(" s"));

  bool ok = persist.saveSession(&node);
  Serial.print(F("saveSession(): "));
  Serial.println(ok ? F("OK") : F("FAIL"));

  Serial.flush();
  esp_sleep_enable_timer_wakeup((uint64_t)uplinkIntervalSeconds * 1000000ULL);
  esp_deep_sleep_start();
}

void setup() {
  Serial.begin(115200);
  delay(2000);

  bootCount++;

  Serial.println();
  Serial.println(F("===================================="));
  Serial.print(F("Arranque numero: "));
  Serial.println(bootCount);

  esp_sleep_wakeup_cause_t wakeup_reason = esp_sleep_get_wakeup_cause();
  Serial.print(F("Wakeup cause: "));
  if (wakeup_reason == ESP_SLEEP_WAKEUP_TIMER) {
    Serial.println(F("TIMER"));
  } else {
    Serial.println(F("POWER ON / RESET"));
  }

  // =========================
  // Alimentacion sensores
  // =========================
  pinMode(SENSOR_POWER, OUTPUT);
  digitalWrite(SENSOR_POWER, LOW);

  // =========================
  // Leer sensores
  // =========================
  digitalWrite(SENSOR_POWER, HIGH);
  delay(500);

  int soilRaw = readSoilRaw();
  Serial.print(F("Humedad raw: "));
  Serial.println(soilRaw);

  delay(100);

  float tempC = readTemperatureC();
  Serial.print(F("Temperatura: "));
  if (tempC == DEVICE_DISCONNECTED_C) {
    Serial.println(F("Error: DS18B20 no detectado"));
    tempC = -127.0f;
  } else if (tempC == 85.0f) {
    Serial.println(F("Lectura invalida (85C)"));
  } else {
    Serial.println(tempC);
  }

  delay(100);

  float lux = readLux();
  Serial.print(F("Lux: "));
  Serial.println(lux);

  digitalWrite(SENSOR_POWER, LOW);

  // =========================
  // LoRaWAN
  // =========================
  spi.begin(5, 19, 27, 18);

  Serial.println(F("Initialise radio"));
  int16_t state = radio.begin();
  debug(state != RADIOLIB_ERR_NONE, F("Initialise radio failed"), state, true);

  Serial.println(F("Initialise LoRaWAN node"));
  state = node.beginOTAA(joinEUI, devEUI, nwkKey, appKey);
  debug(state != RADIOLIB_ERR_NONE, F("Initialise node failed"), state, true);

  bool restored = persist.loadSession(&node);
  Serial.print(F("loadSession(): "));
  Serial.println(restored ? F("session restored") : F("no full session"));

  Serial.println(F("Activating LoRaWAN session"));
  state = node.activateOTAA();

  bool activationFailed = !(state == RADIOLIB_LORAWAN_NEW_SESSION ||
                            state == RADIOLIB_LORAWAN_SESSION_RESTORED);
  debug(activationFailed, F("Activation failed"), state, true);

  if (state == RADIOLIB_LORAWAN_NEW_SESSION) {
    Serial.println(F("OTAA join successful - new session"));
  } else if (state == RADIOLIB_LORAWAN_SESSION_RESTORED) {
    Serial.println(F("OTAA session restored"));
  }

  bool ok = persist.saveSession(&node);
  Serial.print(F("saveSession() after activation: "));
  Serial.println(ok ? F("OK") : F("FAIL"));

  Serial.println(F("Sending uplink"));

  int16_t tempInt = (int16_t)(tempC * 10.0f);
  uint16_t luxInt = (lux > 65535.0f) ? 65535 : (uint16_t)lux;

  uint8_t uplinkPayload[6];
  uplinkPayload[0] = highByte((uint16_t)soilRaw);
  uplinkPayload[1] = lowByte((uint16_t)soilRaw);
  uplinkPayload[2] = highByte((uint16_t)tempInt);
  uplinkPayload[3] = lowByte((uint16_t)tempInt);
  uplinkPayload[4] = highByte(luxInt);
  uplinkPayload[5] = lowByte(luxInt);

  Serial.print(F("Payload [soil, temp*10, lux]: "));
  Serial.print(soilRaw);
  Serial.print(F(", "));
  Serial.print(tempInt);
  Serial.print(F(", "));
  Serial.println(luxInt);

  state = node.sendReceive(uplinkPayload, sizeof(uplinkPayload));
  debug(state < RADIOLIB_ERR_NONE, F("Error in sendReceive"), state, false);

  if (state < 0) {
    Serial.print(F("sendReceive error: "));
    Serial.println(stateDecode(state));
  } else if (state > 0) {
    Serial.println(F("Received a downlink"));
  } else {
    Serial.println(F("No downlink received"));
  }

  ok = persist.saveSession(&node);
  Serial.print(F("saveSession() after uplink: "));
  Serial.println(ok ? F("OK") : F("FAIL"));

  goToDeepSleep();
}

void loop() {
  // no se usa
}
```
