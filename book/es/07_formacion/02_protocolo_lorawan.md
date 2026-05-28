# Teoría II: Protocolo LoRaWAN (Capa MAC)

Mientras que LoRa proporciona la capa física, **LoRaWAN** define la capa de Control de Acceso al Medio (MAC) y la arquitectura de red subyacente. Es un estándar abierto gestionado por la *LoRa Alliance*.

## Acceso al Medio: ALOHA puro

A diferencia de las redes WiFi o móviles donde los dispositivos se sincronizan y negocian cuándo hablar (CSMA/CA), LoRaWAN utiliza un esquema de acceso **ALOHA puro**.
Esto significa que un nodo transmite sus datos en el momento en el que los tiene listos, sin escuchar antes si el canal está libre.

- **Ventaja**: El dispositivo puede pasar la inmensa mayoría del tiempo durmiendo, despertarse, enviar sus datos, escuchar la respuesta (si la hay) y volver a dormir inmediatamente. Esto maximiza la vida útil de la batería.
- **Desventaja**: Riesgo de colisiones si muchos nodos transmiten al mismo tiempo en el mismo canal y con el mismo *Spreading Factor*.

## Clases de Dispositivos LoRaWAN

Para equilibrar latencia y consumo de batería, el protocolo define tres clases de dispositivos:

### Clase A (Bidireccional asíncrono)
Es la clase por defecto y la **obligatoria** para todos los dispositivos LoRaWAN.
1. El nodo transmite un mensaje (Uplink).
2. Abre dos breves ventanas de recepción (RX1 y RX2) inmediatamente después de transmitir.
3. Si el servidor tiene algo que enviarle (Downlink), lo hará en una de esas ventanas.
4. Si no hay respuesta, el nodo se duerme hasta la próxima transmisión.

> *Consumo: Extremadamente bajo (Ideal para nuestro nodo solar/batería en el huerto).*

### Clase B (Sincronización con Beacons)
Abre ventanas de recepción adicionales programadas. Para sincronizarse, los gateways emiten periódicamente balizas (*beacons*).

> *Consumo: Medio. Útil para dispositivos que necesitan actuar bajo demanda con cierta latencia.*

### Clase C (Recepción continua)
El dispositivo está siempre escuchando el canal (las ventanas de recepción están siempre abiertas salvo cuando transmite).

> *Consumo: Alto. No apto para baterías, requiere conexión a la red eléctrica (ej. actuadores industriales).*

## Adaptive Data Rate (ADR)

El **ADR** es un mecanismo clave mediante el cual el *Network Server* controla la velocidad de transmisión (*Data Rate*) y la potencia de transmisión de los nodos.

Si un nodo está muy cerca del Gateway y su señal llega con excelente relación señal/ruido (SNR), el Network Server le indicará (mediante comandos MAC MACPayload) que baje su potencia de transmisión (ahorrando batería) y baje su Spreading Factor (ej. de SF12 a SF7). 

Al usar SF7, el nodo envía los datos mucho más rápido, reduciendo drásticamente su *Time on Air* y liberando el canal para otros nodos. En el taller, dado que el nodo ambiental estará fijo en el huerto, el ADR debe activarse para que la red optimice automáticamente la cobertura y la batería con el paso de los días.
