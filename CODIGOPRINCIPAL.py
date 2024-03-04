import turtle

class Paddle:
    def __init__(self, x, y):
        # Inicializa la paleta con la posición (x, y) especificada.
        self.__x = x  # Coordenada x de la paleta (privada).
        self.__y = y  # Coordenada y de la paleta (privada).
        self.__height = 100  # Altura de la paleta.
        self.__width = 10    # Ancho de la paleta.
        self.__speed = 30    # Velocidad de movimiento de la paleta.
        self.__paddle = turtle.Turtle()  # Crea un objeto Turtle para la paleta.
        self.__paddle.shape("square")    # Forma de la paleta.
        self.__paddle.color("white")     # Color de la paleta.
        self.__paddle.shapesize(stretch_wid=5, stretch_len=1)  # Tamaño de la paleta.
        self.__paddle.penup()  # Levanta el lápiz para evitar que se dibuje la línea.
        self.__paddle.goto(self.__x, self.__y)  # Posiciona la paleta en las coordenadas especificadas.

    def move_up(self):
        # Método para mover la paleta hacia arriba.
        self.__y += self.__speed if self.__y + self.__speed <= 290 else 0  # Limita el movimiento para no salir de la pantalla.
        self.__paddle.sety(self.__y)  # Actualiza la posición y de la paleta.

    def move_down(self):
        # Método para mover la paleta hacia abajo.
        self.__y -= self.__speed if self.__y - self.__speed >= -290 else 0  # Limita el movimiento para no salir de la pantalla.
        self.__paddle.sety(self.__y)  # Actualiza la posición y de la paleta.

    def get_position(self):
        # Método para obtener la posición actual de la paleta.
        return self.__x, self.__y

class Ball:
    def __init__(self):
        # Inicializa la pelota en el centro de la pantalla.
        self.__x = 0  # Coordenada x de la pelota (privada).
        self.__y = 0  # Coordenada y de la pelota (privada).
        self.__speed_x = 1  # Velocidad de la pelota en el eje x.
        self.__speed_y = 1  # Velocidad de la pelota en el eje y.
        self.__ball = turtle.Turtle()  # Crea un objeto Turtle para la pelota.
        self.__ball.shape("square")    # Forma de la pelota.
        self.__ball.color("white")     # Color de la pelota.
        self.__ball.penup()  # Levanta el lápiz para evitar que se dibuje la línea.
        self.__ball.goto(self.__x, self.__y)  # Posiciona la pelota en el centro de la pantalla.

    def move(self):
        # Método para mover la pelota.
        self.__x += self.__speed_x  # Actualiza la posición x de la pelota.
        self.__y += self.__speed_y  # Actualiza la posición y de la pelota.
        self.__ball.goto(self.__x, self.__y)  # Mueve la pelota a la nueva posición.

    def get_position(self):
        # Método para obtener la posición actual de la pelota.
        return self.__x, self.__y

class PongGame:
    def __init__(self):
        # Inicializa el juego Pong.
        self.__marcadorA = 0  # Puntuación del jugador A.
        self.__marcadorB = 0  # Puntuación del jugador B.
        self.__wn = turtle.Screen()  # Crea una pantalla de Turtle.
        self.__wn.title("Pong by Mundo Python")  # Título de la ventana.
        self.__wn.bgcolor("black")  # Color de fondo de la ventana.
        self.__wn.setup(width=800, height=600)  # Tamaño de la ventana.
        self.__wn.tracer(0)  # Desactiva las actualizaciones automáticas.
        self.__jugadorA = Paddle(-350, 0)  # Crea la paleta del jugador A.
        self.__jugadorB = Paddle(350, 0)   # Crea la paleta del jugador B.
        self.__pelota = Ball()  # Crea la pelota.
        self.__pen = turtle.Turtle()  # Crea un objeto Turtle para dibujar el marcador.
        self.__setup_pen()  # Configura el objeto Turtle para el marcador.

    def __setup_pen(self):
        # Configura el marcador en la pantalla.
        self.__pen.speed(0)  # Configura la velocidad de dibujo del marcador.
        self.__pen.color("white")  # Color del marcador.
        self.__pen.penup()  # Levanta el lápiz para no dibujar al moverse.
        self.__pen.hideturtle()  # Oculta el cursor de Turtle.
        self.__pen.goto(0, 260)  # Posiciona el marcador en la parte superior de la pantalla.
        self.__update_score()  # Actualiza el marcador con la puntuación inicial.

    def __update_score(self):
        # Actualiza el marcador con la puntuación actual de los jugadores.
        self.__pen.clear()  # Borra el contenido anterior del marcador.
        self.__pen.write(f"Jugador A: {self.__marcadorA}     Jugador B: {self.__marcadorB}", align="center", font=("Courier", 25, "normal"))  # Escribe la puntuación.

    def __check_collision(self):
        # Verifica las colisiones de la pelota con las paletas y los bordes de la pantalla.
        x, y = self.__pelota.get_position()  # Obtiene la posición actual de la pelota.
        if y > 290 or y < -290:
            self.__pelota._Ball__speed_y *= -1  # Invierte la velocidad de la pelota en el eje y al colisionar con los bordes superior o inferior.
        if (-340 <= x <= -330) and (self.__jugadorA.get_position()[1] - 50 < y < self.__jugadorA.get_position()[1] + 50):
            self.__pelota._Ball__speed_x *= -1  # Invierte la velocidad de la pelota en el eje x al colisionar con la paleta del jugador A.
        elif (340 >= x >= 330) and (self.__jugadorB.get_position()[1] - 50 < y < self.__jugadorB.get_position()[1] + 50):
            self.__pelota._Ball__speed_x *= -1  # Invierte la velocidad de la pelota en el eje x al colisionar con la paleta del jugador B.
        if x > 390:
            # Si la pelota sale por la derecha, incrementa la puntuación del jugador A y reinicia la posición de la pelota.
            self.__pelota._Ball__x = 0
            self.__pelota._Ball__y = 0
            self.__pelota._Ball__speed_x *= -1
            self.__marcadorA += 1
            self.__update_score()  # Actualiza el marcador con la nueva puntuación.
        elif x < -390:
            # Si la pelota sale por la izquierda, incrementa la puntuación del jugador B y reinicia la posición de la pelota.
            self.__pelota._Ball__x = 0
            self.__pelota._Ball__y = 0
            self.__pelota._Ball__speed_x *= -1
            self.__marcadorB += 1
            self.__update_score()  # Actualiza el marcador con la nueva puntuación.

    def play(self):
        # Inicia el juego.
        self.__wn.listen()  # Habilita la escucha de eventos del teclado.
        self.__wn.onkeypress(self.__jugadorA.move_up, "w")  # Configura la tecla 'w' para que mueva hacia arriba la paleta del jugador A.
        self.__wn.onkeypress(self.__jugadorA.move_down, "s")  # Configura la tecla 's' para que mueva hacia abajo la paleta del jugador A.
        self.__wn.onkeypress(self.__jugadorB.move_up, "Up")   # Configura la flecha arriba para que mueva hacia arriba la paleta del jugador B.
        self.__wn.onkeypress(self.__jugadorB.move_down, "Down")  # Configura la flecha abajo para que mueva hacia abajo la paleta del jugador B.
        
        while True:
            self.__wn.update()  # Actualiza la pantalla.
            self.__pelota.move()  # Mueve la pelota.
            self.__check_collision()  # Verifica las colisiones.
            if self.__marcadorA == 3 or self.__marcadorB == 3:
                self.__game_over()
                break

    def __game_over(self):
        # Muestra "Fin del juego" en el centro de la pantalla.
        self.__pen.clear()
        self.__pen.goto(0, 0)
        self.__pen.write("Fin del juego", align="center", font=("Courier", 25, "normal"))

if __name__ == "__main__":
    # Ejecuta el juego.
    game = PongGame()  # Crea una instancia del juego.
    game.play()  # Inicia el juego.


