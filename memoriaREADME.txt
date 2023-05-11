Memoria.py : Juego de Memoria con Fichas
Descripción:
Este programa es un juego de memoria en el que el jugador debe destapar 
todas las fichas ocultas encontrando sus respectivas parejas. El objetivo 
es recordar la ubicación de las fichas y emparejarlas correctamente.
Modificaciones realizadas:
	- Conteo de Taps: Se ha agregado un contador de toques (taps) para 
llevar la cuenta de la cantidad de veces que el jugador ha destapado una 
ficha.
	- Detección de Juego Completado: Se ha añadido un indicador de 
juego completado que verifica si todas las fichas han sido destapadas.
	- Centrado del Dígito: Se ha centrado el número de las fichas en 
cada cuadro para mejorar la presentación visual.
	- Elemento de Innovación: En lugar de utilizar dígitos para las 
fichas, se ha implementado un sistema de colores. Cada número de ficha se 
asigna a un color específico, lo que ayuda al jugador a recordar y asociar 
visualmente las parejas.
Funciones Principales:
	-square(x, y): Dibuja un cuadrado blanco con un borde negro en las 
coordenadas (x, y).
	- index(x, y): Convierte las coordenadas (x, y) a un índice de 
ficha.
	- xy(count): Convierte un índice de ficha a coordenadas (x, y).
	- tap(x, y): Actualiza la ficha marcada y las fichas ocultas según 
el toque del jugador.
	- draw(): Dibuja la imagen del auto, las fichas ocultas y el 
contador de toques en la ventana de Turtle. También muestra un mensaje de 
juego completado cuando todas las fichas han sido destapadas.
	- get_color(digit): Devuelve el color correspondiente al número de 
la ficha.
Instrucciones:
	- El jugador debe hacer clic en las fichas para destaparlas y 
encontrar sus parejas.
	- El contador de toques muestra la cantidad de veces que se ha 
destapado una ficha.
	- Cuando todas las fichas estén destapadas, se mostrará un mensaje 
de juego completado.
