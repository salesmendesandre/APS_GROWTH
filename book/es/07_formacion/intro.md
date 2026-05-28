# Formación: Taller LoRaWAN Ambiental

El proyecto **APS-GROWTH II** va más allá del simple despliegue de dispositivos en huertos educativos; su misión central es capacitar a los futuros ingenieros en el diseño y dominio de las arquitecturas que hacen posible el Internet de las Cosas (IoT) en entornos reales.

Este bloque de formación está diseñado para **estudiantes de Ingeniería Informática** y proporciona una inmersión profunda en las tecnologías **LPWAN** (Low Power Wide Area Network), centrándose específicamente en **LoRa** y el protocolo **LoRaWAN**.

## El Ecosistema LPWAN: ¿LoRa o LoRaWAN?

A menudo estos dos términos se confunden o se usan indistintamente, pero representan capas completamente diferentes dentro de las telecomunicaciones:

- **LoRa** (*Long Range*): Es puramente la **capa física** de transmisión. Es la técnica de modulación de radiofrecuencia (el "cómo" viajan las ondas por el aire).
- **LoRaWAN**: Es el **protocolo de red y arquitectura** del sistema (la capa MAC o Media Access Control). Define cómo se comunican los dispositivos, cómo se gestionan las conexiones, el encriptado de los datos y el ruteo a través de los Gateways hasta el servidor.

Ambas tecnologías se ubican en el extremo del ecosistema IoT diseñado para maximizar el alcance y minimizar el consumo energético, a costa de sacrificar ancho de banda (velocidad de datos), tal y como se muestra en la siguiente comparativa frente a Wi-Fi o 5G:

```{figure} ../../_static/generated/diagrams/es/lora_vs_others.svg
---
width: 80%
align: center
---
Ubicación de LoRaWAN en el espectro de tecnologías IoT (Alto Alcance y Bajo Consumo).
```

## Objetivos del Taller

A lo largo de las siguientes secciones, los participantes lograrán:

1. **Comprender la Capa Física LoRa:** Entender matemáticamente la modulación *Chirp Spread Spectrum* y su resiliencia al ruido.
2. **Dominar el Protocolo LoRaWAN:** Conocer la estructura de las tramas MAC, las clases de dispositivos y los algoritmos de optimización de red (ADR).
3. **Desplegar Arquitecturas Seguras:** Integrar nodos, *Gateways* y *Network Servers* aplicando criptografía robusta (AES-128).
4. **Desarrollar Firmware Eficiente:** Programar microcontroladores ESP32 manejando buses de sensores (I2C/ADC), empaquetando datos a nivel de bit y gestionando transiciones a estados de *Deep Sleep*.
5. **Ensamblar y Desplegar:** Integrar el hardware en envolventes estancas y alimentarlo mediante sistemas de energía solar para garantizar su autonomía.

La meta final es construir desde cero un **nodo IoT ambiental autosuficiente** y desplegarlo en un entorno real.
