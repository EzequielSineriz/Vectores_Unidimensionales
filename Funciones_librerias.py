import lista_personas as paq
nombres1 = []
nombres1 = paq.nombres
emails1 = paq.emails
edades1 = paq.edades
telefonos1 = paq.telefonos
direccion1 = paq.address
codigo_postal1 = paq.codigos_postales
paises1 = paq.paises
def cabecera_menu():
    print("Nombres  ||      Emails    ||      Edades    ||      Telefonos    ||     Direccion     ||    CodigoPostal     ||    Pais     ||")

def importar_listas(nombres:list, emails:list, edades:list, telefonos:list, direccion:list, codigo_postal:list,paises:list)->list:
    cabecera_menu()
    for i in range (len(nombres1)):
        print(nombres[i], "||", emails[i], "||", edades[i], "||", telefonos[i], "||", direccion[i],"||",codigo_postal[i],"||", paises[i] )
        
    

#importar_listas(nombres1, emails1, edades1, telefonos1, direccion1, codigo_postal1, paises1)

def listar_usuarios_mexico(paises:list,nombres:list, emails:list, edades:list, telefonos:list, codigos_postales:list):
    "Función para listar datos de usuarios de México"
    for i in range(len(paises)):
        if paises[i] == 'Mexico':
            print(f'Nombre: {nombres[i]}, Email: {emails[i]}, Telefono: {telefonos[i]}, Edad: {edades[i]}, Codigo Postal: {codigos_postales[i]}')


#listar_usuarios_mexico(paises1,nombres1, emails1, edades1, telefonos1, codigo_postal1)




def listar_datos_brasil(paises:list, nombres:list, emails:list, telefonos:list):
    "Función para listar nombre, mail y teléfono de los usuarios de Brasil"
    for i in range(len(paises)):
        if paises[i] == 'Brazil':
            print(f'Nombre: {nombres[i]}, Email: {emails[i]}, Telefono: {telefonos[i]}')





def listar_usuario_mas_joven(edades:list, nombres:list, emails:list, telefonos:list, paises:list,codigos_postales:list):
    "Función para listar el usuario más joven"
    edad_minima = min(edades)
    for i in range(len(edades)):
        if edades[i] == edad_minima:
            print(f'Nombre: {nombres[i]}, Email: {emails[i]}, Telefono: {telefonos[i]}, Edad: {edades[i]}, Pais: {paises[i]}, Codigo Postal: {codigos_postales[i]}')


def promedio_edad(edades:list)-> int | float:
    "Función para obtener el promedio de edad de los usuarios"
    promedio = sum(edades) / len(edades)
    print(f'El promedio de edad es: {promedio} años')


def mayor_edad_brasil(paises:list, nombres:list, emails:list, telefonos:list, edades:list, codigos_postales:list):
    "Funcion para listar el usuario de mayor edad en Brazil"
    mayor_edad = -1
    indice_mayor = -1
    for i in range(len(paises)):
        if paises[i] == 'Brazil' and edades[i] > mayor_edad:
            mayor_edad = edades[i]
            indice_mayor = i
    if indice_mayor != -1:
        print(f'Nombre: {nombres[indice_mayor]}, Email: {emails[indice_mayor]}, Telefono: {telefonos[indice_mayor]}, Edad: {edades[indice_mayor]}, Codigo Postal: {codigos_postales[indice_mayor]}')


def listar_usuarios_mexico_brasil_cp_mayor_8000(paises:list, nombres:list, emails:list, telefonos:list, codigos_postales:list):
    "Función para listar usuarios de Mexico y Brasil cuyo codigo postal sea mayor a 8000"
    for i in range(len(paises)):
        if (paises[i] == 'Mexico' or paises[i] == 'Brazil') and codigos_postales[i] > 8000:
            print(f'Nombre: {nombres[i]}, Email: {emails[i]}, Teléfono: {telefonos[i]}, Código Postal: {codigos_postales[i]}')

def listar_italianos_mayores_40(paises:list, edades:list, nombres:list, emails:list, telefonos:list):
    "Funcion para listar nombre, mail y telefono de los usuarios italianos mayores de 40 años "
    for i in range(len(paises)):
        if paises[i] == 'Italia' and edades[i] > 40:
            print(f'Nombre: {nombres[i]}, Email: {emails[i]}, Teléfono: {telefonos[i]}')
    


def menu():
    bandera_lista = False
    "Menu de opciones"
    while True:
        print("\nMenu de Opciones:")
        print("1- Listar los datos..")
        print("2- Listar los datos de los usuarios de Mexico")
        print("3- Listar los nombre, mail y telefono de los usuarios de Brasil")
        print("4- Listar los datos del/los usuario/s mas joven/es")
        print("5- Obtener un promedio de edad de los usuarios")
        print("6- De los usuarios de Brasil, listar los datos del usuario de mayor edad")
        print("7- Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000")
        print("8- Listar nombre, mail y telefono de los usuarios italianos mayores a 40 años")
        print("9- Salir")
        opcion = int(input("Ingrese un opcion: "))
        if opcion == 1:
            importar_listas(nombres1, emails1, edades1, telefonos1, direccion1, codigo_postal1, paises1)
            bandera_lista = True
        elif opcion == 2 and bandera_lista == True:
            listar_usuarios_mexico(paises1,nombres1, emails1, edades1, telefonos1, codigo_postal1)
        elif opcion == 3 and bandera_lista == True:
            listar_datos_brasil(paises1, nombres1, emails1, telefonos1)
        elif opcion == 4 and bandera_lista == True:
            listar_usuario_mas_joven(edades1, nombres1, emails1, telefonos1, paises1,codigo_postal1)
        elif opcion == 5 and bandera_lista == True:
            promedio_edad(edades1)
        elif opcion == 6 and bandera_lista == True:
            mayor_edad_brasil(paises1, nombres1, emails1, telefonos1, edades1, codigo_postal1)
        elif opcion == 7 and bandera_lista == True:
            listar_usuarios_mexico_brasil_cp_mayor_8000(paises1, nombres1, emails1, telefonos1, codigo_postal1)
        elif opcion == 8 and bandera_lista == True:
            listar_italianos_mayores_40(paises1, edades1, nombres1, emails1, telefonos1)
        elif opcion == 9:
            print("Saliendo del programa...")
            break
        else:
            print("Tienes que cargar la lista para efectuar esta funcion.")

