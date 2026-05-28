# Theory III: Architecture and Security

To understand the complete ecosystem of the workshop, it is imperative to know the overall architecture and cryptographic mechanisms of LoRaWAN.

## *Star-of-Stars* Architecture

Unlike mesh networks (like Zigbee), LoRaWAN uses a **star-of-stars** architecture.

1. **End Devices (Nodes)**: Like the environmental IoT node we will build, equipped with sensors and a LoRa radio module. They communicate via radio frequency (LoRa).
2. **Gateways**: Multichannel and multi-spreading factor receivers. They act as transparent bridges (*Packet Forwarders*). They listen to the entire LoRa spectrum and forward any valid frame to the network (via Ethernet, WiFi, or 4G). A node is not associated with a specific Gateway; its message can be received by multiple Gateways simultaneously.
3. **Network Server (NS)**: The brain of the network (e.g., The Things Network or ChirpStack). It filters duplicate packets, verifies authenticity, manages ADR (Adaptive Data Rate), and routes data.
4. **Application Server (AS)**: The client's server that decrypts the data packet (*payload*) and stores or processes it.

```{figure} ../../_static/generated/diagrams/es/lorawan_architecture.svg
---
width: 100%
align: center
---
LoRaWAN Star-of-Stars Architecture.
```

## Security and Cryptography

Security is a native pillar of LoRaWAN. Every transmitted message is doubly protected using symmetric **AES-128** cryptography.

1. **Network Session Key (NwkSKey)**: Used by the node and the *Network Server* to mathematically sign the message using a **MIC** (Message Integrity Code). This prevents tampering or spoofing.
2. **Application Session Key (AppSKey)**: Used to **encrypt** the *payload* end-to-end. The Gateway and Network Server cannot read the content from the sensors; only the Application Server possesses the key to decrypt it.

```{figure} ../../_static/generated/diagrams/es/lorawan_security.svg
---
width: 90%
align: center
---
End-to-End encryption flow and integrity authentication (MIC).
```

## Activation Procedures (Joining the Network)

For the environmental node to obtain these session keys and associate with the network, there are two methods:

### OTAA (Over-The-Air Activation)
The recommended method and the one we will implement in the workshop. The node initiates a dynamic negotiation (*Join Request*) by sending its static global credentials:

1. **Device EUI (`DevEUI`)**: A 64-bit globally unique identifier (similar to a MAC address).
2. **Application EUI / Join EUI (`AppEUI`)**: Identifies which application the device belongs to.
3. **Application Key (`AppKey`)**: A secret cryptographic key. It must never be transmitted over the network! It is used to securely negotiate session keys during the *Join Request*.

The server verifies the identity, randomly generates a temporary identifier (`DevAddr`), and negotiates the session keys (`NwkSKey` y `AppSKey`) by sending them encrypted in a *Join Accept*.

```{figure} ../../_static/generated/diagrams/es/lorawan_otaa.svg
---
width: 100%
align: center
---
OTAA activation sequence (Join Procedure).
```

### ABP (Activation by Personalization)
Unlike OTAA, where session keys are negotiated dynamically, in ABP we **hardcode directly into the microcontroller's code** the device address (`DevAddr`) and the final session keys (`NwkSKey` and `AppSKey`).

```{figure} ../../_static/generated/diagrams/es/lorawan_abp.svg
---
width: 100%
align: center
---
Data transmission sequence using ABP (no Join Procedure).
```

### OTAA vs ABP Comparison

As a summary, these are the main differences between both activation methods:

| Feature | OTAA (Recommended) | ABP |
|---|---|---|
| **Key Negotiation** | Dynamic (*Join Request/Accept*) | Static (Hardcoded in firmware) |
| **Security** | High (rotating session keys) | Low (fixed keys, risk of *replay attack*) |
| **Initial Power Consumption** | Higher (requires bidirectional confirmation on startup) | Lower (can transmit immediately) |
| **Network Flexibility** | High (easy migration to another *Network Server*) | Low (requires reprogramming all nodes) |
| **Fault Tolerance** | *Join* may fail if coverage is marginal | No *Join*, but packets are dropped if desynchronized |

*In the assembly workshop, we will configure the OTAA credentials in PlatformIO to securely join our node to the Network Server.*
