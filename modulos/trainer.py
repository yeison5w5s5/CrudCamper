from os import system
from .data import trainer
import json
def guardar():
    system("clear")
    system("clear")
    info= {
        "nombre":str.upper(input("Ingrese su nombre: ")),
        "Apellido":str.upper(input("Ingrese su apellido: ")),
        "edad": int(input("ingrese su edad: ")),
        "Genero": str.upper(input("Ingrese su nombre: ")),
        "materia":str.upper(input("Ingrese su nombre: "))
    }
    trainer.append(info)
    with open("modulos/storage/trainer.json", "w") as f:
        data=json.dumps(trainer, indent=4)
        f.write(data)
        f.close()
        return "Sucessfully Camper"
def buscar():
    system("clear")
    print("Buscando")
def editar():
    system("clear")
    print("Editando")
def eliminar():
    system("clear")
    print("Eliminando")

def mtrainer():
    Ban=True
    while Ban:
        print("""
        Menu Trainer
            1- Guardar Trainer
            2- Buscar Trainer
            3- Editar Trainer
            4- Eliminar Trainer
            5- Salir""")
        opc=int(input("\t"))
        match(opc):
            case(1):
                guardar()
            case(2):
                buscar()
            case(3):
                editar()
            case(4):
                eliminar()
            case(5):
                system("clear")
                Ban=False
            case (_):
                print("otra vez")