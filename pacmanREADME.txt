packman.py: Juego de Pacman

Descripción: 
El objetivo del juego es que Pacman recolecte todos los puntos blancos en 
el laberinto mientras evita ser capturado por los fantasmas. 

Modificaciones realizadas: 

	- Cambio en el tablero: El tablero del laberinto ha sido 
modificado para crear un diseño personalizado.

	- Aumento de velocidad de los fantasmas: Se ha aumentado la 
velocidad de movimiento de los fantasmas para hacer el juego más 
desafiante.

	- Mejora en la inteligencia de los fantasmas: Se ha implementado 
una lógica mejorada para que los fantasmas persigan al jugador de manera 
más inteligente.

Secciones:

	- Estado del juego: Se define un diccionario llamado state que 
almacena la puntuación actual del juego.

	- Inicialización de elementos del juego: Se crean instancias de 
objetos para representar el camino, el texto de puntuación, la dirección 
de Pacman y las posiciones y direcciones de los fantasmas.

	- Funciones de utilidad: Se definen varias funciones que se 
utilizan en el juego, como la función distance para calcular la distancia 
entre dos puntos, la función square para dibujar un cuadrado en el 
laberinto, la función offset para calcular el índice correspondiente a una 
posición en la matriz de casillas, y la función valid para verificar si 
una posición es válida en el laberinto.

	- Función world: Esta función dibuja el laberinto en la pantalla 
utilizando la librería turtle.

	- Función move: Esta función se encarga del movimiento de Pacman y 
los fantasmas. Actualiza la puntuación, borra la pantalla, mueve a Pacman 
en la dirección actual, verifica si Pacman ha recolectado un punto blanco, 
actualiza la posición de Pacman y los fantasmas, y verifica si Pacman ha 
sido capturado por un fantasma.

	- Función change: Esta función cambia la dirección de Pacman si es 
válida según la entrada del usuario.

	- Configuración inicial y bucle principal: Se realiza la 
configuración inicial del juego, como el tamaño de la ventana y la 
posición del texto de puntuación. Luego, se ejecuta el bucle principal del 
juego, donde se actualiza el movimiento de los personajes y se manejan las 
entradas del usuario.

Instrucciones:

Usa las flechas para atrapar todos los puntos blancos sin que pactan sea 
alcanzado por los fantasmas.
