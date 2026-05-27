# APS-GROWTH II: Integración IoT y Análisis Botánico

## Evolución Tecnológica y Científica
En el curso **2025-2026**, el proyecto dio un salto cualitativo pasando de la simple gestión de tareas a la recolección activa de datos ambientales. La segunda anualidad se centró en la **sensorización del huerto**, uniendo las capacidades tecnológicas del Área de Informática con el rigor científico de los departamentos de Biología y Antropología.

El objetivo general fue reforzar la inclusión social y la sostenibilidad mediante una aplicación conectada a sensores ambientales a través de la red de bajo consumo LoRaWAN, permitiendo llevar la información del campo directamente a los usuarios sin depender de infraestructuras WiFi complejas.

## Implementación de la Red de Sensores

El sistema arquitectónico y de red se basó en los siguientes elementos clave:

1. **Nodos Sensorizados:** Se instalaron nodos con sensores para medir variables críticas como la humedad del suelo (sensores capacitivos), la temperatura y humedad ambiente (BME280) y la intensidad luminosa (BH1750).
2. **Comunicación LoRaWAN:** La transmisión de datos se garantizó mediante módulos LoRa conectados a un Gateway exterior, ideales para entornos agrícolas.
3. **Autonomía Energética:** Los nodos se equiparon con placas solares y baterías Li-ion, asegurando un despliegue ecológico y continuo en las cajas estancas (IP65).

```{figure} ../_static/aps_growth/aps2_lora.png
:width: 80%
:align: center
:name: fig-aps2-lora

Esquema de comunicación LoRaWAN implementado en el ecosistema del huerto.
```

## Dimensión Botánica y Pedagógica

La simple recolección de datos no era suficiente; era necesario interpretarlos. El equipo de Botánica elaboró **fichas técnicas** y definió qué parámetros eran críticos para las diferentes especies de plantas cultivadas.

Gracias a esto, los estudiantes y los usuarios del huerto pudieron aprender sobre fisiología vegetal en tiempo real, observando cómo las variaciones ambientales afectaban al crecimiento de los cultivos y convirtiendo el huerto en un auténtico laboratorio vivo.

## Impacto Comunitario

El proyecto evolucionó hacia un **monitoreo activo en tiempo real**, proporcionando recomendaciones basadas en datos empíricos. Se desarrollaron sistemas de alerta inteligente integrados en la aplicación con una visualización mejorada, garantizando en todo momento la accesibilidad cognitiva y consolidando una cultura de cuidado ecológico.
