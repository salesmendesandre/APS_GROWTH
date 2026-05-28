# Programación del Nodo IoT

El desarrollo del firmware para el ESP32 se realizará preferiblemente en **PlatformIO** o en el **Arduino IDE**, utilizando C/C++. El objetivo es leer los sensores, empaquetar los datos de forma ultra-eficiente y enviarlos vía LoRaWAN, minimizando el tiempo que el microcontrolador pasa encendido.

## 1. Librerías Necesarias
- **MCCI LoRaWAN LMIC library**: La implementación estándar de la pila LoRaWAN para microcontroladores. Maneja la lógica MAC, los tiempos de RX1/RX2 y el Duty Cycle.
- **Wire.h** y librerías específicas (como `BH1750.h` o las de sensores de temperatura/humedad).

## 2. Lectura de Sensores y Optimización del Payload (Empaquetado)

En LoRaWAN, cada byte extra enviado reduce drásticamente la batería y aumenta las probabilidades de colisión. **Nunca se deben enviar cadenas JSON o texto en claro**. Todo debe empaquetarse en binario.

Ejemplo de optimización mediante desplazamiento de bits (*bit shifting*):
Si la temperatura puede variar entre -10 y 50 ºC, en lugar de enviar un `float` (4 bytes), podemos enviar un `int16_t` (2 bytes) multiplicando el valor por 10 o 100.

```cpp
// Ejemplo: Temperatura 24.5 ºC -> 245
int16_t temp = (int16_t)(temperatura_leida * 10);
uint8_t payload[4];
payload[0] = temp >> 8;   // Byte más significativo
payload[1] = temp & 0xFF; // Byte menos significativo

// Igual para la luz o la humedad
uint16_t luz = leer_luxes();
payload[2] = luz >> 8;
payload[3] = luz & 0xFF;
```

## 3. Lógica Orientada a Eventos y LMIC

La librería LMIC funciona mediante callbacks (eventos). El flujo principal de nuestro programa será:
1. `setup()`: Inicializa el chip LoRa, los sensores I2C/ADC y programa las claves OTAA (`DevEUI`, `AppEUI`, `AppKey`).
2. Se encola un *Join Request*.
3. Evento `EV_JOINED`: El nodo se ha unido con éxito. Se habilitan los envíos periódicos.
4. Evento `EV_TXCOMPLETE`: El paquete se ha transmitido y se han cerrado las ventanas de recepción. **Este es el momento exacto para ir a dormir.**

## 4. Gestión Extrema de Energía (Deep Sleep)

En lugar de usar la función `delay()` (que mantiene la CPU consumiendo entre 40 y 80 mA), utilizaremos el **Deep Sleep** del ESP32.
En Deep Sleep, la memoria RAM y la CPU se apagan, reduciendo el consumo a < 10 µA. Solo el coprocesador RTC (Real Time Clock) se queda encendido para despertar al chip tras el tiempo estipulado (ej. 30 minutos).

Al despertar de un Deep Sleep, el ESP32 ejecuta la función `setup()` de nuevo. Para que LMIC no tenga que volver a hacer el proceso de *Join* (lo que gasta mucha batería), guardaremos las claves de sesión dinámicas en la memoria RTC RAM del ESP32 para recuperarlas al despertar.
