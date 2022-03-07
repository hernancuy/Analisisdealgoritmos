# Read me -Tarea 4

Hernan David Cuy Salcedo
Carlos Andres Torres Echavarria


-----------------
## RSA-Miller-Rabin-Java

La implementación del algoritmo RSA en Java se realizó de acuerdo al algoritmo nombrado en Algorthms Unlocked (Cormen 2013) en el cual se describe el proceso y paso a paso de su creación. 

Para la obtención de los primos se realizó por medio del algoritmo de Miller-Rabbin el cual realiza test de comprobación para encontra si el primo generado con el tamaño de bits asignado es o no primo.

Para la ejecucion del programa se puede importar el proyecto en netbeans, y correr la clase RSA.java,  esta clase posee el main del programa.

### Como funciona

Al iniciar el programa nos solicitará lo siguiente:

```
Tarea 4
Digite el numero de bits, el rango va de 3 a 1024:
```
Alli podremos colocar el numero de bits que queremos para nuestros numeros primos ***p*** y ***q***.

En el ejemplo solicitamos primos de **5** bits, el programa nos genera automaticamente dos numeros que cumplan con esta condición, en este caso el **19 **y el **23**
```
Tarea 4
Digite el numero de bits, el rango va de 3 a 1024:
5
Tiempo generacion p y q: 4ms
p = 19.
q = 23.
p*q = n = 437.
r = 396.
e = 5.
d = 317.
RSA llave publica P (5,437)
RSA llave privada S (317,437)
Digite el valor al que desea generar la llave (X)
20
Tiempo Generacion P(X) 0ms
Tiempo Generacion Q(X): 0ms
Al encriptar P(x)= 286.
Al desencriptar S(x)= 20.
```
Seguido a esto procede a realizar la operación de **p  * q** denominada ***n*** la cual da como resultado **437**.  Seguido a este procede a hacer la operación denominada ***r*** la cual es resultado de ***(p-1)*(q-1)*** en nuestro caso su resultado será **396**.

El valor de ***e*** se obtiene de seleccionar un entero impar que es  primo relativo a **r**.  Para el ejemplo e es **5**.

El computo de* **d*** lo obtenemos como el multiplicador inverso de **e**, modurlo ***r***, para el ejemplo **317**

Hasta el momento, ya tendríamos los valores necesarios para generar nuestros ***P=(e, n)*** y ***S(d, n)*** los cuales, para esta ejecución fueron ***P (5,437)*** y ***S (317,437)***.

Finalmente podemos hacer la encripcion y descripción con nuestros datos obtenidos de un valor solicitado.
