# Theory I: LoRa Physical Layer

To develop efficient applications over LPWAN networks, it is essential to understand what happens at the electromagnetic and physical levels. **LoRa** (Long Range) is a proprietary modulation technology originally patented by Cycleo (now Semtech) that exclusively defines the **physical layer** of communication.

## Chirp Spread Spectrum (CSS) Modulation

LoRa utilizes spread spectrum modulation using frequency sweeps, known as **Chirp Spread Spectrum (CSS)**. Unlike traditional modulations (such as FSK or OOK) that vary the amplitude or phase of a fixed carrier, CSS uses pulses called *chirps* that vary their frequency linearly over time across the entire available bandwidth.

There are two main types of chirps:
- **Up-chirp:** The frequency increases progressively over time.
- **Down-chirp:** The frequency decreases progressively.

```markdown
```{note}
This technique is extremely resilient to narrow-band interference, additive white Gaussian noise (AWGN), and the Doppler effect, allowing it to demodulate signals that are **below the noise floor** (up to -20 dB Signal-to-Noise Ratio or SNR).
```
```

## Key RF Parameters

LoRa modulation allows the configuration of three fundamental parameters that drastically affect range (Link Budget), data rate, and energy consumption:

### 1. Spreading Factor (SF)
The SF defines how many *chips* (the smallest fragments of information sent) make up a data symbol. In Europe, typical SF values range from **SF7 to SF12**.

Mathematically, a symbol contains $2^{SF}$ chips. By increasing the SF:
- The symbol is longer in time.
- It transmits at a slower speed (lower *Data Rate*).
- Greater resilience is achieved (increases range in kilometers).
- The **Time on Air (ToA)** increases, i.e., the time the radio must be on, increasing battery consumption.

### 2. Bandwidth (BW)
It represents the frequency range swept by the chirp. In LoRaWAN networks in Europe, a bandwidth of **125 kHz** is commonly used. Increasing the BW increases the transfer rate at the expense of reducing receiver sensitivity.

### 3. Coding Rate (CR)
LoRa employs a **Forward Error Correction** (FEC) mechanism to recover corrupt bits. Redundancy is added to the original payload, denoted as `4/5`, `4/6`, `4/7`, or `4/8`.
A CR of `4/5` means that for every 5 bits transmitted, 4 are real data and 1 is redundancy.

## Link Budget Calculation

The Link Budget defines the viability of a wireless link by summing antenna gains and transmission power, and subtracting medium losses. LoRa's success lies in its **reception sensitivity ($S$)**, which can be approximated with the following equation:

$$
S = -174 + 10 \log_{10}(BW) + NF + SNR_{limit}
$$ (eq-lora-sensitivity-en)

Where:
- `-174` is thermal noise in 1 Hz of bandwidth (in dBm).
- `BW` is the bandwidth in Hz.
- `NF` is the receiver's Noise Figure (typically 6 dB).
- `SNR_{limit}` is the required SNR limit to decode, which for SF12 can reach -20 dB.

Substituting for SF12 at 125 kHz, the theoretical sensitivity is approximately **-137 dBm**, allowing links of tens of kilometers with only 14 dBm (25 mW) of transmission power.

## Regulations and Duty Cycle (Europe - ETSI)

By operating in the **868 MHz ISM (Industrial, Scientific, and Medical)** band in Europe, devices do not require spectrum use licenses, but they must comply with very strict regulations on how much time they can transmit.

This is controlled by the **Duty Cycle**. In the most widely used 868 MHz sub-band, the maximum allowed Duty Cycle is **1%**.

> [!WARNING]
> A 1% Duty Cycle means that if your node sends a message that takes 1 second to transmit (Time on Air = 1s), the radio module MUST remain silent for the next 99 seconds. If you try to transmit more frequently, the LoRaWAN firmware or legal regulations will block the transmission.
