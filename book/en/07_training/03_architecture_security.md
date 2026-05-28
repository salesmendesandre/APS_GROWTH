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

### ABP (Activation by Personalization)
Session keys (`NwkSKey`, `AppSKey`) and the device address (`DevAddr`) are statically programmed into the node's firmware (C++ code) at the factory.
- *Advantage*: The node does not need to negotiate its connection; it can transmit immediately.
- *Disadvantage*: It is less secure. If frame counter synchronization is lost, the network will drop packets to prevent *Replay attacks*.

### OTAA (Over-The-Air Activation)
The recommended method and the one we will implement in the workshop. The node initiates a dynamic negotiation (*Join Request*) by sending its static global credentials (`DevEUI`, `AppEUI`, and `AppKey`).
The server verifies the identity, randomly generates a temporary identifier (`DevAddr`), and negotiates the session keys (`NwkSKey` and `AppSKey`) by sending them encrypted in a *Join Accept*.

*In the assembly workshop, we will configure the OTAA credentials in PlatformIO to securely join our node to the Network Server.*
