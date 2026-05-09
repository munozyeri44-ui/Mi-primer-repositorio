#Esto es un comentario de una sola linea
"""Este es un comentario de 
varias lineas"""

#Inicializando variables
nombre="Jery Gabriela Barrero Muñoz"
edad=14
estado=True
nota=5.0

#mostrar el contenido de las variables print()
print(nombre)
print(edad)
print(estado)
print(nota)  

#Que tipo de dato contiene variable.
print(type(nombre))
print(type(edad))
print(type(estado))
print(type(nota))

#vamos a utilizar la funcion input para recoger datos por medio del teclado
nombre=input("¿como te llamas?")
edad=input("cuantos años tienes?")
estado=input("¿en que estado te encuentras?")
nota=input("¿cual es tu nota?")

#para visualizar que guardamos en las variables anteriores
print("Hola,",nombre,"un gusto conocerte")
print("Tu edad es:",edad)
print("Tu estado es:",estado)
print("Tu nota es:",nota)