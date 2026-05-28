# Theory IV: Network Servers and the TTN Community

In the LoRaWAN ecosystem, the **Network Server** is the brain of the network. It is the software responsible for receiving, managing, and processing all the radio frequency (RF) messages captured by the Gateways, subsequently delivering them, clean and ordered, to the final applications.

## What exactly does a Network Server do?

While a Gateway simply listens to the electromagnetic spectrum and forwards everything it captures to the Internet, the Network Server does the heavy lifting:

1. **Packet De-duplication**: If you have several Gateways nearby, it is very likely that they all hear the same message from your environmental node. They will all send it to the Internet. The Network Server detects that it is the same message (same timestamp, same frame counter) and discards the duplicates, keeping the one with the best signal quality (SNR and RSSI).
2. **Routing**: It determines which application (Application Server) a piece of data belongs to based on the device address (`DevAddr`).
3. **MAC Commands**: It manages low-level network commands (hidden from the user) to optimize the channel.
4. **Adaptive Data Rate (ADR)**: It constantly evaluates the quality of the radio link of each node. If a node has an excellent signal, the Network Server commands it (via MAC commands) to transmit faster (higher Data Rate) and with less power. This saves battery and frees up airtime on the spectrum.
5. **Authentication and Security**: It is responsible for executing the *Join* procedure in OTAA, verifying the node's identity with its `AppKey`, and generating the temporary session keys (`NwkSKey` and `AppSKey`).

## Integrations and Data Extraction

Once the Network Server has decrypted and validated the message, what does it do with it? It passes it to the **Application Server**, which is usually an integrated module in the same platform.

The Application Server is responsible for exposing this data so that other platforms can consume it. This is done through **Integrations**:

- **MQTT (Message Queuing Telemetry Transport)**: The de facto standard in IoT. It allows subscribing to a "topic" to receive sensor data in real-time.
- **Webhooks (HTTP POST)**: The server automatically sends an HTTP request to an external URL every time a packet arrives. Very useful for injecting data directly into databases or dashboards (like Grafana, Node-RED, or custom applications).
- **Native Integrations**: Platforms like AWS IoT Core, Azure IoT, or Datacake offer pre-configured native connectors to receive data streams without writing a single line of code.

## The Ecosystem: The Things Network (TTN)

For our project, we will use **The Things Network (TTN)**. But what exactly is it, and why is it so relevant?

### Origin and Philosophy

The Things Network was born in Amsterdam in 2015 with a revolutionary premise: **to build a data network for the Internet of Things that is open, decentralized, and community-owned (crowdsourced).**

Instead of relying on large traditional telecom operators (like AT&T, Vodafone, or Orange) that charge monthly subscriptions for each SIM, the founders proposed that if enough people and companies bought and connected a LoRaWAN Gateway on their roofs, a whole city could be covered in a matter of weeks. And they succeeded: they covered Amsterdam in less than 6 weeks using only 10 Gateways purchased by volunteers.

- **Goal of the TTN Community**: To provide free and global connectivity for IoT projects, fostering innovation, learning, and applications with a social or environmental impact (like our ecological garden).
- **The Pact**: If you contribute coverage to the network by installing a Gateway, you can use the coverage of Gateways installed by other people anywhere in the world.

### The Things Stack (V3)

All the software infrastructure that runs TTN is known as **The Things Stack** (currently in its version 3 or "V3"). There are different versions of the same software:

1. **The Things Network (Community Edition)**: It is free, operated by *The Things Industries*, and maintained by the global community. This is the one we will use. Its fair use policy limits transmission time to prevent saturation, making it perfect for environmental monitoring.
2. **The Things Enterprise Stack**: A paid version with service level agreements (SLAs), ideal for companies with massive commercial deployments that require official support and private servers.

## Alternatives to TTN

Although TTN is the largest collaborative network, there are other options for deploying LoRaWAN networks:

- **ChirpStack**: It is an *Open Source* Network Server. Instead of connecting to a global server (like in TTN), you can install ChirpStack on a local Raspberry Pi or on your own server. It is ideal for private networks (for example, covering an isolated farm where there is no Internet and everything is managed on a local network).
- **AWS IoT Core for LoRaWAN**: Amazon Web Services offers a managed Network Server that integrates directly with the entire AWS cloud computing ecosystem.
- **Helium**: A decentralized commercial network where Gateway owners receive cryptocurrencies (HNT) as a reward for providing coverage, and users pay micro-transactions to send data.
- **Commercial Networks**: Traditional operators (Orange, Actility, LORIOT) offer LoRaWAN as a classic paid service for corporate clients.

In this course, we opt for **The Things Network** because of its open nature, its strong community (with thousands of tutorials), and its perfect alignment with the educational values of the APS-GROWTH project.
