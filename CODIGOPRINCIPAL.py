import turtle
import time

class Paddle:
    def __init__(self, x, y, name):
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
        self.__name = self.__get_valid_name(name)  # Limita el nombre personalizado y realiza la validación.

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

    def get_name(self):  # Método para obtener el nombre del jugador.
        return self.__name

    def __get_valid_name(self, name):
        # Método privado para obtener un nombre válido.
        while True:
            if any(char.isdigit() for char in name):
                print("No se aceptan números en el nombre. Ingrese un nombre válido.")
            elif len(name) > 5:
                print("El nombre excede el límite de 5 caracteres. Ingrese un nombre válido.")
            else:
                return name
            name = input("Ingrese el nombre nuevamente (máximo 5 caracteres): ")

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
        self.__tiempo = 0  # Es la variable en donde se guarda el tiempo
        self.__wn = turtle.Screen()  # Crea una pantalla de Turtle.
        self.__wn.title("Pong by Mundo Python")  # Título de la ventana.
        self.__wn.bgcolor("black")  # Color de fondo de la ventana.
        self.__wn.setup(width=800, height=600)  # Tamaño de la ventana.
        self.__wn.tracer(0)  # Desactiva las actualizaciones automáticas.
        jugadorA_nombre = input("Nombre del jugador A (máximo 5 caracteres): ")
        jugadorB_nombre = input("Nombre del jugador B (máximo 5 caracteres): ")
        self.__jugadorA = Paddle(-350, 0, jugadorA_nombre)  # Crea la paleta del jugador A con nombre personalizado.
        self.__jugadorB = Paddle(350, 0, jugadorB_nombre)   # Crea la paleta del jugador B con nombre personalizado.
        self.__pelota = Ball()  # Crea la pelota.
        self.__pen_score = turtle.Turtle()  # Crea un objeto Turtle para dibujar el marcador.
        self.__pen_timer = turtle.Turtle()  # Crea un objeto Turtle para dibujar el cronómetro.
        self.__game_over_flag = False  # Variable para controlar el estado del juego.
        self.__setup_pen()  # Configura los objetos Turtle para el marcador y el cronómetro.

    def __setup_pen(self):
        # Configura el marcador en la pantalla.
        self.__pen_score.speed(0)  # Configura la velocidad de dibujo del marcador.
        self.__pen_score.color("white")  # Color del marcador.
        self.__pen_score.penup()  # Levanta el lápiz para no dibujar al moverse.
        self.__pen_score.hideturtle()  # Oculta el cursor de Turtle.
        self.__update_score()  # Actualiza el marcador con la puntuación inicial.

        # Configura el cronómetro en la pantalla.
        self.__pen_timer.speed(0)  # Configura la velocidad de dibujo del cronómetro.
        self.__pen_timer.color("white")  # Color del cronómetro.
        self.__pen_timer.penup()  # Levanta el lápiz para no dibujar al moverse.
        self.__pen_timer.hideturtle()  # Oculta el cursor de Turtle.
        self.__update_timer()  # Actualiza el cronómetro con el tiempo inicial.

    def __update_score(self):
        # Actualiza el marcador con la puntuación actual de los jugadores.
        self.__pen_score.clear()  # Borra el contenido anterior del marcador.
        self.__pen_score.goto(0, 230)  # Posiciona el marcador en la parte superior de la pantalla.
        self.__pen_score.write(f"{self.__jugadorA.get_name()}: {self.__marcadorA}     {self.__jugadorB.get_name()}: {self.__marcadorB}", align="center", font=("Courier", 15, "normal"))  # Escribe la puntuación.

    def __update_timer(self):
        # Actualiza el cronómetro con el tiempo transcurrido.
        self.__pen_timer.clear()  # Borra el contenido anterior del cronómetro.
        self.__pen_timer.goto(-390, -290)  # Posiciona el cronómetro en la esquina inferior izquierda.
        self.__pen_timer.write(f"Cronómetro: {self.__tiempo:.1f}", align="left", font=("Courier", 10, "normal"))

    def __check_collision(self):
        # Verifica las colisiones de la pelota con las paletas y los bordes de la pantalla.
        x, y = self.__pelota.get_position()  # Obtiene la posición actual de la pelota.
        if y > 290 or y < -290:
            self.__pelota._Ball__speed_y *= -1  # Invierte la velocidad de la pelota en el eje y al colisionar con los bordes superior o inferior.
        if (-340 <= x <= -330) and (
                self.__jugadorA.get_position()[1] - 50 < y < self.__jugadorA.get_position()[1] + 50):
            self.__pelota._Ball__speed_x *= -1  # Invierte la velocidad de la pelota en el eje x al colisionar con la paleta del jugador A.
        elif (340 >= x >= 330) and (
                self.__jugadorB.get_position()[1] - 50 < y < self.__jugadorB.get_position()[1] + 50):
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

    def __countdown(self):
        # Temporizador de cuenta regresiva antes de iniciar el juego.
        for i in range(10, 0, -1):# Itera desde 3 hasta 1 (exclusivo) en orden descendente.
            self.__pen_timer.clear() # Borra el contenido anterior del temporizador.
            self.__pen_timer.goto(0, 0) #se utiliza para asegurarse de que los números de la cuenta regresiva se escriban en el centro de la pantalla
            self.__pen_timer.write(f"{i}", align="center", font=("Courier", 25, "normal"))# Escribe el número de cuenta regresiva.
            self.__wn.update() #se utiliza para actualizar la pantalla de Turtle después de cada cuenta regresiva
            time.sleep(1)  # Espera un segundo.
        self.__pen_timer.clear() # Borra el contenido del temporizador para dejar la pantalla limpia antes de iniciar el juego.

    def play(self):
        # Inicia el juego.
        self.__countdown()  # Ejecuta el temporizador de cuenta regresiva antes de iniciar el juego.
        self.__wn.listen()  # Habilita la escucha de eventos del teclado.
        self.__wn.onkeypress(self.__jugadorA.move_up, "w")  # Configura la tecla 'w' para que mueva hacia arriba la paleta del jugador A.
        self.__wn.onkeypress(self.__jugadorA.move_down, "s")  # Configura la tecla 's' para que mueva hacia abajo la paleta del jugador A.
        self.__wn.onkeypress(self.__jugadorB.move_up, "Up")  # Configura la flecha arriba para que mueva hacia arriba la paleta del jugador B.
        self.__wn.onkeypress(self.__jugadorB.move_down, "Down")  # Configura la flecha abajo para que mueva hacia abajo la paleta del jugador B.

        start_time = time.time()  # Registra el tiempo de inicio del juego.

        while True:
            self.__wn.update()  # Actualiza la pantalla.
            self.__pelota.move()  # Mueve la pelota.
            self.__check_collision()  # Verifica las colisiones.
            self.__tiempo = time.time() - start_time  # Calcula el tiempo transcurrido desde el inicio del juego.
            self.__update_timer()  # Actualiza el cronómetro con el tiempo transcurrido.
            if self.__marcadorA == 20 or self.__marcadorB == 20:
                self.__game_over()
                break
        turtle.done()

    def __game_over(self):
        self.__game_over_flag = True
        self.__pen_score.clear()
        self.__pen_score.goto(0, 0)
        ganador = "Jugador A" if self.__marcadorA == 20 else "Jugador B"
        self.__pen_score.write(f"Fin del juego\nGanador: {ganador}", align="center", font=("Courier", 25, "normal"))
        self.__wn.update()

if __name__ == "__main__":
    # Ejecuta el juego.
    game = PongGame()  # Crea una instancia del juego.
    game.play()  # Inicia el juego.