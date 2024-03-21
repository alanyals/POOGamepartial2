import os
import turtle  # Importa el módulo turtle para crear gráficos.
import time  # Importa el módulo time para manejar el tiempo.
from openai import OpenAI


client = OpenAI(
  # This is the default and can be omitted
  api_key='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',
)

class Paddle:  # Define la clase Paddle.
    def __init__(self, x, y, name):  # Define el método de inicialización con los argumentos x, y y name.
        # Inicializa la paleta con la posición (x, y) especificada.
        self.__x = x  # Define el atributo privado __x como la coordenada x de la paleta.
        self.__y = y  # Define el atributo privado __y como la coordenada y de la paleta.
        self.__height = 100  # Define el atributo privado __height como la altura de la paleta.
        self.__width = 10    # Define el atributo privado __width como el ancho de la paleta.
        self.__speed = 30    # Define el atributo privado __speed como la velocidad de movimiento de la paleta.
        self.__paddle = turtle.Turtle()  # Crea un objeto Turtle para la paleta.
        self.__paddle.shape("square")    # Define la forma de la paleta como un cuadrado.
        self.__paddle.color("white")     # Define el color de la paleta como blanco.
        self.__paddle.shapesize(stretch_wid=5, stretch_len=1)  # Define el tamaño de la paleta.
        self.__paddle.penup()  # Levanta el lápiz para evitar que se dibuje la línea.
        self.__paddle.goto(self.__x, self.__y)  # Posiciona la paleta en las coordenadas especificadas.
        self.__name = self.__get_valid_name(name)  # Limita el nombre personalizado y realiza la validación.

    def move_up(self):  # Define el método move_up para mover la paleta hacia arriba.
        # Mueve la paleta hacia arriba si no supera el límite superior de la pantalla.
        self.__y += self.__speed if self.__y + self.__speed <= 290 else 0
        self.__paddle.sety(self.__y)  # Actualiza la posición y de la paleta.

    def move_down(self):  # Define el método move_down para mover la paleta hacia abajo.
        # Mueve la paleta hacia abajo si no supera el límite inferior de la pantalla.
        self.__y -= self.__speed if self.__y - self.__speed >= -290 else 0
        self.__paddle.sety(self.__y)  # Actualiza la posición y de la paleta.

    def get_position(self):  # Define el método get_position para obtener la posición actual de la paleta.
        return self.__x, self.__y  # Devuelve las coordenadas x e y de la paleta.

    def get_name(self):  # Define el método get_name para obtener el nombre del jugador.
        return self.__name  # Devuelve el nombre del jugador.

    def __get_valid_name(self, name):  # Define el método privado __get_valid_name para validar el nombre del jugador.
        while True:  # Bucle infinito para la validación continua del nombre.
            error_messages = {  # Define un diccionario de mensajes de error para la validación del nombre.
                any(char.isdigit() for char in name): "No se aceptan números en el nombre. Ingrese un nombre válido.",
                len(name) > 5: "El nombre excede el límite de 5 caracteres. Ingrese un nombre válido."
            }
            error = error_messages.get(True)  # Obtiene el mensaje de error si hay una condición verdadera.
            if error:  # Si hay un mensaje de error.
                print(error)  # Imprime el mensaje de error.
            else:  # Si no hay error.
                return name  # Devuelve el nombre válido.
            name = input("Ingrese el nombre nuevamente (máximo 5 caracteres): ")  # Solicita al usuario que ingrese el nombre nuevamente.

    def __get_unique_characters(self, name):  # Define el método privado __get_unique_characters para obtener un conjunto de caracteres únicos del nombre ingresado.
        unique_characters = {char for char in name}  # Utiliza una comprensión de conjuntos para obtener caracteres únicos del nombre.
        return unique_characters  # Devuelve el conjunto de caracteres únicos.

class MoveHorizontal:
    def __init__(self):
        self.__x = 0

    def moveX(self, value):
        self.__x += value

    def getX(self):
        return self.__x

class MoveVertical:
    def __init__(self):
        self.__y = 0

    def moveY(self, value):
        self.__y += value

    def getY(self):
        return self.__y

class Ball(MoveHorizontal, MoveVertical):
    def __init__(self):
        MoveHorizontal.__init__(self)
        MoveVertical.__init__(self)
        # Inicializa la pelota en el centro de la pantalla.
        self.__speed_x = 1  # Velocidad de la pelota en el eje x.
        self.__speed_y = 1  # Velocidad de la pelota en el eje y.
        self.__ball = turtle.Turtle()  # Crea un objeto Turtle para la pelota.
        self.__ball.shape("square")    # Define la forma de la pelota.
        self.__ball.color("white")     # Define el color de la pelota.
        self.__ball.penup()  # Levanta el lápiz para evitar que se dibuje la línea.
        self.__ball.goto(self.getX(), self.getY())  # Posiciona la pelota en el centro de la pantalla.

    def move(self):
        # Método para mover la pelota.
        self.moveX(self.__speed_x)  # Mueve la pelota en el eje x.
        self.moveY(self.__speed_y)  # Mueve la pelota en el eje y.
        self.__ball.goto(self.getX(), self.getY())  # Mueve la pelota a la nueva posición.

    def get_position(self):
        # Método para obtener la posición actual de la pelota.
        return self.getX(), self.getY()

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
        self.jugadorA_nombre = input("Nombre del jugador A (máximo 5 caracteres): ")
        self.jugadorB_nombre = input("Nombre del jugador B (máximo 5 caracteres): ")
        self.__jugadorA = Paddle(-350, 0, self.jugadorA_nombre)  # Crea la paleta del jugador A con nombre personalizado.
        self.__jugadorB = Paddle(350, 0, self.jugadorB_nombre)   # Crea la paleta del jugador B con nombre personalizado.
        self.__jugadores = [self.__jugadorA, self.__jugadorB]  # Lista de jugadores
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
        
        # Utiliza enumerate y comprensión de listas para formatear los nombres y marcadores en una cadena legible.
        score_text = "     ".join([f"{player.get_name()}: {score}" for player, score in zip(self.__jugadores, [self.__marcadorA, self.__marcadorB])])
        
        self.__pen_score.write(score_text, align="center", font=("Courier", 15, "normal"))  # Escribe la puntuación.

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

    def __game_over(self): #Este método se llama cuando el juego llega a su fin
        self.__game_over_flag = True #indica que el juego ha terminado.
        self.__pen_score.clear() #borra cualquier contenido dibujado por ese objeto. En este caso, limpia el marcador en la pantalla.
        self.__pen_score.goto(0, 0)  # Esto asegura que el siguiente texto se escriba desde la posición inicial.
        ganador = self.jugadorB_nombre if self.__marcadorA == 20 else self.jugadorA_nombre
        perdedor = self.jugadorA_nombre if self.__marcadorA == 20 else self.jugadorB_nombre #Determina quién es el ganador del juego
        messages = [ {"role": "user", "content":  
              f"Genera un mensaje motivacional de no más de 50 caracteres felicitando a un jugador llamado {ganador} que acaba de ganar una partida de pong, y otro mensaje de 50 caracteres en donde motive al {perdedor} o sea al otro jugador a ganar en la siguiente partida "} ] 
        chat = client.chat.completions.create( 
            model="gpt-3.5-turbo", messages=messages 
        ) 
        reply = chat.choices[0].message.content 
        self.__pen_score.write(f"{reply}", align="center", font=("Courier", 10, "normal")) #para escribir en la pantalla el mensaje "Fin del juego" seguido del nombre del ganador.
        self.__wn.update() #actualizar la pantalla de Turtle después de mostrar el mensaje de fin de juego.

    def __repr__(self): #Este método proporciona una representación imprimible de la instancia de la clase.
        return f"PongGame(marcadorA={self.__marcadorA}, marcadorB={self.__marcadorB}, tiempo={self.__tiempo})" #Esta cadena incluye la puntuación del jugador A, la puntuación del jugador B y el tiempo transcurrido.

if __name__ == "__main__":
    # Ejecuta el juego.
    game = PongGame()  # Crea una instancia del juego.
    game.play()  # Inicia el juego.