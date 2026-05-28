# Training: Environmental LoRaWAN Workshop

The **APS-GROWTH II** project goes beyond the simple deployment of devices in educational gardens; its core mission is to train future engineers in the design and mastery of the architectures that make the Internet of Things (IoT) possible in real-world environments.

This training block is designed for **Computer Engineering students** and provides a deep dive into **LPWAN** (Low Power Wide Area Network) technologies, focusing specifically on **LoRa** and the **LoRaWAN** protocol.

## The LPWAN Ecosystem: LoRa vs LoRaWAN

Often these two terms are confused or used interchangeably, but they represent completely different layers within telecommunications:

- **LoRa** (*Long Range*): It is purely the **physical layer** of transmission. It is the radio frequency modulation technique (the "how" the waves travel through the air).
- **LoRaWAN**: It is the **network protocol and architecture** of the system (the MAC or Media Access Control layer). It defines how devices communicate, how connections are managed, data encryption, and routing through Gateways to the server.

Both technologies are located at the extreme end of the IoT ecosystem designed to maximize range and minimize energy consumption, at the cost of sacrificing bandwidth (data rate), as shown in the following comparison against Wi-Fi or 5G:

```{figure} ../../_static/generated/diagrams/en/lora_vs_others.svg
---
width: 80%
align: center
---
LoRaWAN position in the IoT technologies spectrum (Long Range and Low Power).
```

## Workshop Objectives

Throughout the following sections, participants will achieve:

1. **Understand the LoRa Physical Layer:** Mathematically understand *Chirp Spread Spectrum* modulation and its resilience to noise.
2. **Master the LoRaWAN Protocol:** Know the structure of MAC frames, device classes, and network optimization algorithms (ADR).
3. **Deploy Secure Architectures:** Integrate nodes, Gateways, and Network Servers applying robust cryptography (AES-128).
4. **Develop Efficient Firmware:** Program ESP32 microcontrollers handling sensor buses (I2C/ADC), packing data at the bit level, and managing transitions to Deep Sleep states.
5. **Assemble and Deploy:** Integrate the hardware into waterproof enclosures and power it using solar energy systems to ensure autonomy.

The ultimate goal is to build a **self-sufficient environmental IoT node** from scratch and deploy it in a real-world environment.
