#desempaquetamiento extendido

#Definimos una lista con algunos elementos
ejemplo = [1, 2, 3, 4, 5]

# Utilizamos el desempaquetamiento extendido para asignar valores a variables individuales
primer_elemento, *resto_elementos, ultimo_elemento = ejemplo

# Mostramos los resultados
print("Primer numero:", primer_elemento)
print("Resto de numeros:", resto_elementos)
print("Último numero:", ultimo_elemento)



#Comprension de lista con condiciones
#se crea una lista con el nombre de la variable lista
lista = [numero**2 for numero in  range(0,5)] 
#La variable numero se eleva al cuadrado
#cuando se ejecute la secuencia de números, se elevan al cuadrado y se agrega el número a la lista 
#se especifica el rango de 0-4

#se imprime la lista
print(lista) 




#método estático
class Termometro: #Clase que contiene un método estático para convertir unidades de temperatura.

    def celsius_a_fahrenheit(celsius): #Método estático que convierte grados Celsius a grados Fahrenheit.
        
        return (celsius * 9/5) + 32 #La temperatura convertida a grados Fahrenheit.

# Ejemplo de uso del método estático de la clase Termometro
celsius_temperatura = 25
fahrenheit_temperatura = Termometro.celsius_a_fahrenheit(celsius_temperatura)

print("Temperatura en Fahrenheit:", fahrenheit_temperatura)  # Salida: Temperatura en Fahrenheit: 77.0


#En este ejemplo, creamos una clase llamada Termometro que contiene un método estático llamado celsius_a_fahrenheit.
#El método estático celsius_a_fahrenheit convierte grados Celsius a grados Fahrenheit utilizando la fórmula de conversión.
#El método estático puede ser llamado directamente desde la clase Termometro, sin necesidad de crear una instancia de la clase.
#En el ejemplo, cambiamos de grados Celsius (25) al método estático celsius_to_fahrenheit, y luego imprimimos el resultado de la conversión.




#desempaquetamiento de argumentos
def calcular_suma(a, b, c):
    return a + b + c

# Lista de valores
valores = [1, 2, 3]

# Desempaquetar los valores y pasarlos a la función
resultado = calcular_suma(*valores)

print("La suma es:", resultado)

#el desempaquetamiento de argumentos en funciones es una característica útil de Python que te permite pasar múltiples argumentos 
#a una función utilizando una única variable contenedora
#como una lista o una tupla luego, estos argumentos pueden ser desempaquetados dentro de la función para acceder a cada uno de ellos individualmente.

#En lugar de pasar estos argumentos uno por uno, creamos una lista valores que contiene los valores que queremos pasar a la función. 
#Luego, utilizamos el operador * para desempaquetar los valores de la lista y pasarlos como argumentos individuales a la función calcular_suma.