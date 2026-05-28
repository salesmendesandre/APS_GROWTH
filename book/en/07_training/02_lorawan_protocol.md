# Theory II: LoRaWAN Protocol (MAC Layer)

While LoRa provides the physical layer, **LoRaWAN** defines the Media Access Control (MAC) layer and the underlying network architecture. It is an open standard managed by the *LoRa Alliance*.

## Media Access: Pure ALOHA

Unlike WiFi or mobile networks where devices synchronize and negotiate when to speak (CSMA/CA), LoRaWAN uses a **pure ALOHA** access scheme.
This means that a node transmits its data the moment it has it ready, without listening beforehand to check if the channel is free.

- **Advantage**: The device can spend the vast majority of its time sleeping, wake up, send its data, listen for a response (if any), and immediately go back to sleep. This maximizes battery life.
- **Disadvantage**: Risk of collisions if many nodes transmit at the same time on the same channel and with the same *Spreading Factor*.

## LoRaWAN Device Classes

To balance latency and battery consumption, the protocol defines three classes of devices:

### Class A (Bi-directional asynchronous)
This is the default class and is **mandatory** for all LoRaWAN devices.
1. The node transmits a message (Uplink).
2. It opens two brief reception windows (RX1 and RX2) immediately after transmitting.
3. If the server has something to send to it (Downlink), it will do so in one of those windows.
4. If there is no response, the node goes to sleep until the next transmission.

```{figure} ../../_static/generated/diagrams/es/lorawan_class_a.svg
---
width: 65%
align: center
---
Reception windows (RX1 and RX2) after an Uplink in a Class A device.
```

> *Consumption: Extremely low (Ideal for our solar/battery node in the garden).*

### Class B (Synchronization with Beacons)
It opens additional scheduled reception windows. To synchronize, gateways periodically emit beacons. This allows the server to know exactly when (*Ping Slot*) the device will be awake to receive a *Downlink* message, saving battery the rest of the time.

```{figure} ../../_static/generated/diagrams/es/lorawan_class_b.svg
---
width: 65%
align: center
---
Reception windows (Ping Slots) scheduled and synchronized by Beacons in a Class B device.
```

> *Consumption: Medium. Useful for devices that need to act on demand with some latency (e.g., a battery-operated irrigation valve).*

### Class C (Continuous Reception)
The device is always listening to the channel. The RX2 reception window remains continuously open except when the device is transmitting (TX). Latency is near zero because the server can send commands at any time without waiting for an *Uplink*.

```{figure} ../../_static/generated/diagrams/es/lorawan_class_c.svg
---
width: 65%
align: center
---
Continuous reception (RX2 always open) in a Class C device.
```

> *Consumption: High. Not suitable for batteries, requires connection to the electrical grid (e.g., smart streetlights or industrial actuators).*

## Adaptive Data Rate (ADR)

**ADR** is a key mechanism through which the *Network Server* controls the *Data Rate* and transmission power of the nodes.

If a node is very close to the Gateway and its signal arrives with an excellent signal-to-noise ratio (SNR), the Network Server will instruct it (via MAC MACPayload commands) to lower its transmission power (saving battery) and lower its Spreading Factor (e.g., from SF12 to SF7).

By using SF7, the node sends data much faster, drastically reducing its *Time on Air* and freeing up the channel for other nodes. In the workshop, since the environmental node will be fixed in the garden, ADR should be activated so that the network automatically optimizes coverage and battery over the days.
