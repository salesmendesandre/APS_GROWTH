# Teoría I: Capa Física LoRa

Para poder desarrollar aplicaciones eficientes sobre redes LPWAN, es fundamental comprender qué ocurre a nivel electromagnético y físico. **LoRa** (Long Range) es una tecnología de modulación patentada originalmente por Cycleo (hoy Semtech) que define exclusivamente la **capa física** de la comunicación.

## Modulación Chirp Spread Spectrum (CSS)

LoRa utiliza la modulación de espectro ensanchado mediante barridos de frecuencia, conocida como **Chirp Spread Spectrum (CSS)**. A diferencia de las modulaciones tradicionales (como FSK u OOK) que varían la amplitud o fase de una portadora fija, CSS utiliza pulsos llamados *chirps* que varían su frecuencia linealmente con el tiempo a través de todo el ancho de banda disponible.

Existen dos tipos principales de chirps:
- **Up-chirp:** La frecuencia aumenta progresivamente a lo largo del tiempo.
- **Down-chirp:** La frecuencia disminuye progresivamente.

```{note}
Esta técnica es extremadamente resiliente frente a interferencias de banda estrecha, ruido gaussiano blanco aditivo (AWGN) y el efecto Doppler, lo que permite demodular señales que se encuentran **por debajo del umbral de ruido** (hasta -20 dB de relación Señal a Ruido o SNR).
```

## Parámetros RF Clave

La modulación LoRa permite configurar tres parámetros fundamentales que afectan drásticamente al alcance (Link Budget), la tasa de datos y el consumo de energía:

### 1. Spreading Factor (SF)
El SF define cuántos *chips* (los fragmentos de información más pequeños enviados) componen un símbolo de datos. En Europa, los valores típicos de SF van del **SF7 al SF12**.

Matemáticamente, un símbolo contiene $2^{SF}$ chips. Al incrementar el SF:
- El símbolo es más largo en el tiempo.
- Se transmite a una velocidad menor (menor *Data Rate*).
- Se consigue mayor resiliencia (aumenta el alcance en kilómetros).
- Aumenta el **Time on Air (ToA)**, es decir, el tiempo que la radio debe estar encendida, incrementando el consumo de batería.

### 2. Ancho de Banda (Bandwidth - BW)
Representa el rango de frecuencias por el cual barre el chirp. En las redes LoRaWAN en Europa se suele utilizar un ancho de banda de **125 kHz**. Al aumentar el BW se aumenta la tasa de transferencia a expensas de reducir la sensibilidad del receptor.

### 3. Coding Rate (CR)
LoRa emplea un mecanismo de corrección de errores hacia adelante (*Forward Error Correction* - FEC) para recuperar bits corruptos. Se añade redundancia a la carga útil original, denotada como `4/5`, `4/6`, `4/7` o `4/8`.
Un CR de `4/5` significa que de cada 5 bits transmitidos, 4 son datos reales y 1 es redundancia.

## Cálculo del Link Budget (Presupuesto de Enlace)

El Link Budget define la viabilidad de un enlace inalámbrico sumando las ganancias de antena y la potencia de transmisión, y restando las pérdidas del medio. El éxito de LoRa radica en su **sensibilidad en recepción ($S$)**, la cual se puede aproximar con la siguiente ecuación:

$$
S = -174 + 10 \log_{10}(BW) + NF + SNR_{limit}
$$ (eq-lora-sensitivity)

Donde:
- `-174` es el ruido térmico en 1 Hz de ancho de banda (en dBm).
- `BW` es el ancho de banda en Hz.
- `NF` es la Figura de Ruido (*Noise Figure*) del receptor (típicamente 6 dB).
- `SNR_{limit}` es el SNR límite requerido para decodificar, que para SF12 puede llegar a -20 dB.

Sustituyendo para SF12 a 125 kHz, la sensibilidad teórica es de aproximadamente **-137 dBm**, lo que permite enlaces a decenas de kilómetros con solo 14 dBm (25 mW) de potencia de transmisión.

## Normativa y Duty Cycle (Europa - ETSI)

Al operar en la banda **ISM (Industrial, Scientific, and Medical) de 868 MHz** en Europa, los dispositivos no requieren licencias de uso del espectro, pero deben acatar normativas muy estrictas sobre cuánto tiempo pueden emitir.

Esto se controla mediante el **Duty Cycle** (Ciclo de Trabajo). En la subbanda más utilizada de 868 MHz, el Duty Cycle máximo permitido es del **1%**.

> [!WARNING]
> Un Duty Cycle del 1% significa que si tu nodo envía un mensaje que tarda 1 segundo en emitirse (Time on Air = 1s), el módulo de radio DEBE permanecer en silencio los siguientes 99 segundos. Si intentas emitir con mayor frecuencia, el firmware de LoRaWAN o las normativas legales bloquearán la transmisión.
