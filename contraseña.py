import getpass
import pwinput
import os

ARCHIVO = "estudiante.txt"
CLAVE = "admin123"

def cargar_usuario():
    usuarios = {}
    if os.path.exists('usuarios.txt'):
        with open("usuarios.txt", "r") as archivo:
            for linea in archivo:
                usuario, clave = linea.strip().split(",")
                usuarios[usuario] = clave
    return usuarios

def agregar_usuario(usuario, clave):
    with open("usuarios.txt", "a") as archivo:
        archivo.write(f"{usuario},{clave}\n")

agregar_usuario("joshua", "123")

def inicio():
    print("== INICIO DE SESION ==\n")
    usuarios = cargar_usuario()
    usuario = input("Usuario: ")
    clave_ingresada = pwinput.pwinput(prompt='Ingrese la contraseña: ', mask='*')
    if usuario in usuarios and usuarios[usuario] == clave_ingresada:
        print("\nACCESO PERMITIDO")
        return True
    else:
        print("\nUSUARIO O CONTRASEÑA INCORRECTA")
        return False

inicio()