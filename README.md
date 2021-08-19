# Ejemplos_enC_G4
Ejemplos realizados en C

Ejemplos de programación básica

Ejercicio 1: imprimir un menú

Instrucciones:

•	El programa debe de estar comentado para tú “yo del futuro”
•	Realiza un menú número de opciones
•	Utiliza la instrucción if para cada opción
•	En cada opción se debe de imprimir el mensaje “has seleccionado la opción: #de opción”


Ejercicio 2: operaciones aritméticas con variables de diferentes tipos

Instrucciones:
	
	Sección 1

•	El programa debe de estar comentado para tú “yo del futuro”
•	Declara una variable de tipo entero. Con valor asignado
•	Declara una variable de tipo decimal (float). Con valor asignado
•	Con esas variables realiza las operaciones aritméticas básicas (suma, resta multiplicación y división).
•	Imprime el resultado de cada operación de manera ordenada

Sección 2:

•	Modifica el programa para que ahora el usuario pueda introducir los valores. Cuidado con las divisiones.

Programación Intermedia

Ejercicio 1: Calculadora algebraica

Instrucciones:

•	El programa debe de estar comentado para tú “yo del futuro”
•	Realiza un menú número de opciones, las opciones constan de: calcular las raíces de una ecuación cuadrática, de una ecuación cubica, y de una recta
•	El usuario debe de introducir los valores
•	Imprimir el resultado y presentar la opción de realizar otra operación o salir del programa
•	Cuidado con los valores negativos

Ejercicio 2: Gráficas

Instrucciones:

	Sección 1

•	El programa debe de estar comentado para tú “yo del futuro”
•	Genera 20 valores aleatorios (de tipo float o double) que serán asignados a una variable x
•	Genera 20 valores aleatorios (de tipo float o double) que serán asignados a una variable y
•	Obtén la gráfica de los valores generados, con etiquetas en cada eje.

Sección 2

•	El programa debe de estar comentado para tú “yo del futuro”
•	Ahora modifica el programa para que el usuario introduzca los valores de x y y.
•	Considera que el usuario puede introducir valores numéricos negativos.

Programación Avanzada


Ejercicio 1: Regresión lineal

•	El programa debe de estar comentado para tú “yo del futuro”
•	Considera que recibes los valores de temperatura (1 dato por 0.1segundo)
•	Gráfica los datos que se adjuntan (supón que son los datos del sensor)
•	Este tipo de comportamiento es lineal, obtén la ecuación que representa la relación de estos datos en particular
•	El programa esta relacionado el método conocido como mínimos cuadrados.


Ejercicio 2: bits

•	El programa debe de estar comentado para tú “yo del futuro”
•	Considera la siguiente estructura:

0_00000000_0

Es una estructura de ocho bits, y dos bits adicionales uno para indicar que se inicia la transmisión de datos, y un bit de paridad que tendrá dos funciones una de indicar que finalizar la transmisión y la otra de indicar que se ha recibido los datos correctos.
•	Para que el ultimo bit pueda cumplir las dos funciones, se deben de considerar los últimos dos bits como operadores lógicos (compuertas).
•	Bajo esta premisa, elabora un programa en lenguaje C de tal forma que se pueda realizar una comparación con los datos enviados y recibidos, en donde el único indicador que son correctos es el bit de paridad.

Ejercicio 3: Lógica no bloqueante

Hacer un programa para encender 4 leds en secuencia exclusiva ascendente durante 5 segundos, encender en secuencia aditiva durante 5 segundos, enceder en secuencia descendente exclusiva durante 5 segundos, encender en secuencia descendente aditiva durante 5 segundos. Repetir en este orden durante durante 30 segundo y repetir en orden inverso durante 90 segundos minutos. Que esto se realice solo 4 veces. Despues todos los leds se apagan. Las exclusivas las tienen que hacer con operadores incrementales o decrementales. Las aditivas las tienen que hacer con operadores bitwise. Mientras se envia por mqtt una suma incremental mas el valor en binario de la secuencia de los leds. Todo debe de ser programado con base en lógica no bloqueante (sin usar delays)

Cada estado del led dura 0.2 segundos

LEDS= 0000

Secuencia ascendente exclusiva:
0000
1000
0100
0010
0001

0000 0000
0000 1000
0001 0000 <- No
0000 0000
0000 0001

Secuencia aditiva esxclusiva:
0000
1000
1100
1110
1111

Programación Experta

Ejercicio 1: Desarrolla una biblioteca




