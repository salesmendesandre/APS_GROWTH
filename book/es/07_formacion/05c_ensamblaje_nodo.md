# Ensamblaje Físico del Nodo

Una vez que tenemos lista la PCB de interconexión, el siguiente paso es ensamblar todos los componentes dentro de la caja estanca para proteger la electrónica y los sensores de las inclemencias del tiempo en el exterior. A continuación, se detalla el proceso paso a paso.

## Preparación de la Caja y Cables

### 1. Preparación de la caja estanca
Comenzamos con la caja estanca vacía, la cual ya cuenta con los tres agujeros pasacables en uno de sus laterales ({numref}`fig-assembly-1`).

```{figure} ../../_static/assembly/1.png
---
name: fig-assembly-1
width: 60%
align: center
---
Caja estanca vacía con los tres agujeros pasacables.
```

### 2. Colocación de los prensaestopas
En estos agujeros debemos colocar los prensaestopas, que garantizarán el sellado de los cables hacia el interior ({numref}`fig-assembly-2`).

```{figure} ../../_static/assembly/2.png
---
name: fig-assembly-2
width: 60%
align: center
---
Colocación de los prensaestopas en los agujeros de la caja.
```

### 3. Distribución de los cables
Para mantener el orden, definimos por dónde pasará cada cable ({numref}`fig-assembly-3`):
- **Superior izquierdo:** Cable del panel solar.
- **Superior derecho:** Cable de la sonda de temperatura.
- **Inferior:** Cable del sensor de humedad del suelo.

```{figure} ../../_static/assembly/3.png
---
name: fig-assembly-3
width: 60%
align: center
---
Distribución de cables a través de los prensaestopas de la caja.
```

## Conexiones y Soldaduras Previas

### 4. Jack USB y sensores
Procedemos a soldar el conector Jack USB que nos permitirá enchufar el panel solar al nodo Heltec. Además, preparamos las conexiones de la sonda de temperatura soldándole su conector XTH correspondiente ({numref}`fig-assembly-4`).

```{figure} ../../_static/assembly/4.png
---
name: fig-assembly-4
width: 60%
align: center
---
Conexiones preparadas (Jack USB para panel solar y conector XTH de temperatura).
```

### 5. Sensor de luz
Este paso también es de soldadura. Los cables del sensor de luz van conectados al terminal XTH, asegurándonos de mantener la correspondencia de colores adecuada ({numref}`fig-assembly-5b`).

```{figure} ../../_static/assembly/5_b.png
---
name: fig-assembly-5b
width: 60%
align: center
---
Cables del sensor de luz soldados al conector XTH.
```

### 6. Cables de batería
Preparamos también el conector con los cables correspondientes que irán a la batería del nodo ({numref}`fig-assembly-6`).

```{figure} ../../_static/assembly/6.png
---
name: fig-assembly-6
width: 60%
align: center
---
Cableado de conexión preparado para la batería.
```

## Montaje en el Soporte 3D

Para fijar la placa y la batería dentro de la caja utilizamos un soporte impreso en 3D. 

### 7. Soporte de la batería
En la {numref}`fig-assembly-7` se aprecia el ensamblaje y aspecto del soporte 3D, el cual servirá para albergar la batería.

```{figure} ../../_static/assembly/7.png
---
name: fig-assembly-7
width: 60%
align: center
---
Soporte 3D diseñado para la batería y la placa.
```

### 8. Ensamblaje de la placa en el soporte
Atornillamos la PCB (con el nodo Heltec ya montado) al soporte 3D ({numref}`fig-assembly-8`). Deberá ir colocada directamente en la posición correcta tal y como se muestra en la {numref}`fig-assembly-9`.

```{figure} ../../_static/assembly/8.png
---
name: fig-assembly-8
width: 60%
align: center
---
PCB y módulo Heltec atornillados al soporte 3D.
```

```{figure} ../../_static/assembly/9.png
---
name: fig-assembly-9
width: 60%
align: center
---
Posición correcta de la placa en el soporte.
```

## Ensamblaje Final

### 9. Instalación del sensor de luz
Para instalar el sensor de luz en la caja, debemos aplicar una gota de adhesivo y colocarlo en su posición definitiva, conectándolo a la placa tal y como se muestra en las siguientes figuras ({numref}`fig-assembly-10` y {numref}`fig-assembly-11`).

```{figure} ../../_static/assembly/10.png
---
name: fig-assembly-10
width: 60%
align: center
---
Aplicación de una gota de adhesivo.
```

```{figure} ../../_static/assembly/11.png
---
name: fig-assembly-11
width: 60%
align: center
---
Posición y conexión del sensor de luz a la placa.
```

### 10. Conexión de la antena (SMA)
Instalamos la antena conectando el codo del conector SMA ({numref}`fig-assembly-12`).

```{figure} ../../_static/assembly/12.png
---
name: fig-assembly-12
width: 60%
align: center
---
Conexión del codo del conector SMA a la antena.
```

### 11. Conexión de sensores y panel
Conectamos a la placa el cable USB (para el panel solar), así como los cables de la sonda de temperatura y del sensor de humedad del suelo ({numref}`fig-assembly-13`).

```{figure} ../../_static/assembly/13.png
---
name: fig-assembly-13
width: 60%
align: center
---
Cable USB, sonda de temperatura y sensor de humedad conectados al nodo.
```

### 12. Colocación en la caja
Una vez conectada la electrónica, colocamos el soporte con la placa dentro de la caja estanca y lo fijamos instalando los dos tornillos de fijación ({numref}`fig-assembly-14`).

```{figure} ../../_static/assembly/14.png
---
name: fig-assembly-14
width: 60%
align: center
---
Soporte fijado dentro de la caja estanca con los dos tornillos.
```

### 13. Soporte del panel solar
A continuación, atornillamos el soporte del panel solar a la pieza impresa ({numref}`fig-assembly-15`).

```{figure} ../../_static/assembly/15.png
---
name: fig-assembly-15
width: 60%
align: center
---
Soporte del panel solar atornillado a la pieza impresa.
```

### 14. Nodo finalizado
Finalmente, cerramos la caja. En la {numref}`fig-assembly-16` se puede observar cómo se vería finalmente el nodo físico completamente ensamblado.

```{figure} ../../_static/assembly/16.png
---
name: fig-assembly-16
width: 60%
align: center
---
Aspecto final del nodo completamente ensamblado.
```
