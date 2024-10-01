#Ejercicio 1: Desarrollar una función que pida 10 nombres de manera secuencial, los
#guarde en una lista y la retorne. El programa principal debe invocar a la función y
#mostrar por pantalla el retorno

""" def ingreso_nombres(cant_pedidas:int):
    lista_nombres = []
    for i in range(cant_pedidas):
        nombre = input("Ingresa un nombre: ")
        lista_nombres.append(nombre)
        
    return lista_nombres

lista_nombre_a = []
cantidad_pedidos = 5
lista_nombre_a = ingreso_nombres(cantidad_pedidos)
print(lista_nombre_a) """

#Ejercicio 2: Desarrollar una función que inicialice una lista de 10 números en 0, pida
#posición y número a guardar al usuario, lo guarde en una lista en la posición
#solicitada aleatoriamente y la retorne. El programa principal debe invocar a la
#función y mostrar por pantalla el retorno.
""" 
def lista_diez():
    lista_numeros = [0] * 10
    corte = "s"
    while corte == "s":
        numero = int (input("Ingrese un numero para agregar a la lista: "))
        posicion = int(input("Ingrese en la posicion que desar cambiarla: "))
        while posicion > 10:
            posicion = int(input("Error. Ingrese una posicion valida: "))
        lista_numeros[posicion] = numero
        corte = input("Desea seguir ingresando s/n: ")
    return lista_numeros


lista = []
lista = lista_diez()
print (lista)
 """

#Ejercicio 3: Desarrollar una función que pida 10 números dentro de un rango
#especificado, validar los números solicitados dentro de ese rango, guardar en una
#lista y retornarla. El programa principal debe invocar a la función y mostrar por
#pantalla el retorno.
""" 
def input_min_max(minimo:int, maximo: int, cant_elem_lista:int):
    lista_numeros = []
    for i in range(cant_elem_lista):
        numero = int(input(f"Ingrese un numero entre ({minimo}) y ({maximo}) : "))
        while numero < minimo or numero > maximo:
            numero = int(input(f"Error ingrese dentro de los rangos validos min({minimo}) y max({maximo}) : "))
        lista_numeros.append(numero)
    return lista_numeros

minimo = 18
maximo = 80
cant_pedidos = 5
lista = []
lista = input_min_max (minimo, maximo, cant_pedidos)
print (lista)
 """
#Ejercicio 4: Desarrollar una función que reciba por parámetro, una lista de números
#y un número especificado. La misma debe buscar el número especificado en la lista
#y retornar “True” si existe.


""" def buscar_datos(lista:list, numero:int)->bool:
    retorno = False
    for i in range(len(lista)):
        if lista[i] == numero:
            retorno = True
    return retorno

lista = [13,50,20,40,55]
lista = buscar_datos(lista, 50)

if lista:
    print(lista)

 """

#Ejercicio 5: Dadas las siguientes listas:
#Nombres=["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Ped
#ro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
#edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]
#Desarrollar una función que reciba por parámetro la lista de edades, busque a las
#personas de menor edad (puede ser más de una) y las retorne. El programa
#principal deberá mostrar nombre y edad de los menores.

# Listas proporcionadas
#nombres = ["Ana", "Luis", "Juan", "Sol", "Roberto", "Sonia", "Ulises", "Sofia", "Maria", "Pedro", "Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
#edades = [23, 45, 34, 23, 46, 23, 45, 67, 37, 68, 25, 55, 45, 27, 43]

# Función para buscar a las personas con menor edad

""" # Listas proporcionadas
nombres = ["Ana", "Luis", "Juan", "Sol", "Roberto", "Sonia", "Ulises", "Sofia", "Maria", "Pedro", "Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23, 45, 34, 23, 46, 23, 45, 67, 37, 68, 25, 55, 45, 27, 43]


def buscar_menores(nombres:list, edades:list)->list | None:
    edad_menor = edades[0]
    

    # Buscar las personas con esa edad mínima
    for i in range(len(edades)):
        if edades[i] < edad_menor:
            edad_menor = edades[i]
    for i in range(len(edades)):
        if edades[i] == edad_menor:
            print ("el nombre del alumno de menor edad es:" ,nombres[i])

       
    return 
# Programa principal
menores = buscar_menores(nombres, edades)

# Mostrar el resultado
print (menores) """
#Ejercicio 6: Analizar los datos del archivo listas_personas.py. Utilizando el archivo
#listas_personas.py. Importar los nombres a una lista. Realizar una función que
#muestre los mismos.


import lista_personas as paq
nombres1 = paq.nombres

def mostrar_lista(lista:list):
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            print(lista[i][j], end=" ")
        print ("")

print(nombres1[1][0]) #6