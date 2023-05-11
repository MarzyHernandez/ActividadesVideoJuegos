
TiroP.py: Juego de tiro parabólico
Descripción:

El código busca hacer un juego interactivo en el cual el objetivo es 
golpear los objetivos en movimiento con una pelota. 

Modificaciones realizadas:
	- Ajuste de velocidad: Se ha reducido el factor de velocidad de los ejes horizontal y 
vertical, permitiendo que la pelota y los objetivos se muevan más rápido. 
Para incrementar la velocidad, se ha ajustado el factor de velocidad 
dividiendo por un valor más pequeño, en este caso, 12. Además, se ha 
aumentado la velocidad horizontal de los objetivos en el bucle move() para 
que se muevan más rápido a través de la ventana.
	- Juego infinito: Se ha modificado el comportamiento de los 
objetivos cuando salen de la ventana. En lugar de eliminarlos por 
completo, ahora se vuelven a posicionar en el lado derecho de la ventana 
con una nueva posición vertical aleatoria. Esto permite que el juego 
continúe sin límite de tiempo, ya que siempre habrá nuevos objetivos en 
movimiento.

Instrucciones: 

El juego se controla haciendo clic en la pantalla para definir la 
dirección y la velocidad de la pelota. El objetivo es golpear los 
objetivos azules en movimiento con la pelota roja. Los objetivos se 
generan de forma aleatoria en el lado derecho de la ventana y se mueven 
hacia la izquierda. Cuando la pelota golpea un objetivo, este desaparece. 
El juego continúa hasta que la pelota o un objetivo salen de la ventana.
