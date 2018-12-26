#Asi se declara una variable en Python
#Asi se imprime en Python
my_name = "Jorge"
print("Hello and welcome! " + my_name)
#En Python las variables son reconocidos su tipo de forma automatica, no es necesario definirlas
print(10 / 4.5)
#En Python para elevar a la potencia se usa la notacion (x ** y)
print(2**10)
#En python % es el modulo y da el residuo de una operacion
#En python para publicar un numero se debe colocar str(nombre_variable) para que se convierta en string
#El operador += declara la suma del valor acumulado en una variable + el nuevo valor

operador = 0
operador += 2
#operador debe imprimir 2
print(operador)
#el """ permite tener un parrafo multilinea en python
ejemplo = """
Hola
esto es una prueba de varias lineas
bueno depronto
puede ser
"""
print (ejemplo)

cool_number = 12+30
cool_number*5
print(cool_number)

#Una funcion se define como def nombre funcion (argumentos)
#el nivel de identacion es super importante para saber que hace y que no hace parte de una funcion


def function_name(a):
	print("Esto es una prueba")
	valor = a +1
	print (valor)

function_name(5)
print("Esto es una prueba")

