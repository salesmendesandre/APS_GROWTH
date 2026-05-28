# Ensamblaje Físico y Despliegue

Con el firmware validado en el laboratorio, el siguiente paso es la integración física del nodo y su despliegue en campo.

## 1. Esquema Eléctrico

Antes de soldar o conectar cables, es imperativo revisar el esquema de conexiones.
- **Bus I2C**: Los pines SDA y SCL del módulo Heltec deben ir a los pines equivalentes del BH1750 (Sensor de Luz), añadiendo resistencias de pull-up si el módulo del sensor no las integra.
- **Alimentación de sensores**: Es preferible alimentar los sensores desde un pin GPIO que actúe como un interruptor de encendido (`Vext` en algunas placas Heltec). De esta manera, antes de dormir, el ESP32 apaga completamente los sensores cortando su VCC, ahorrando miliamperios.

## 2. Integración en Caja Estanca

Las inclemencias meteorológicas son el principal enemigo de un nodo IoT.
- El módulo Heltec y la batería se introducirán en una **caja estanca transparente**.
- Es vital el uso de prensaestopas (pasacables impermeables) en los orificios por donde salen los cables de los sensores de humedad del suelo y temperatura ambiente.
- La antena LoRa (generalmente un latiguillo U.FL a SMA) debe atornillarse firmemente al chasis de la caja, garantizando que quede vertical y fuera de la interferencia del panel solar.

## 3. Conexión del Panel Solar

El panel solar de 24V CC 6W no puede conectarse directamente al módulo Heltec, ya que el voltaje freiría el regulador interno del ESP32.
- **Regulador MPPT/Step-down**: Es necesario un módulo intermedio que reduzca y estabilice el voltaje del panel a los parámetros de carga de la batería de litio (típicamente 4.2V max), protegiendo contra sobrecargas y sobredescargas.

## 4. Despliegue en el Huerto

En el huerto educativo:
1. **Ubicación**: El panel solar debe orientarse al Sur (en el hemisferio norte) con una inclinación óptima para maximizar la insolación invernal.
2. **Sensores**: El sensor de humedad capacitivo se entierra en la tierra cerca de las raíces de un cultivo representativo. El sensor de temperatura ambiente debe estar a la sombra o protegido de la radiación directa para evitar lecturas falsas al alza.
3. El sensor de luz (BH1750) quedará dentro de la caja estanca transparente apuntando hacia el cielo.
