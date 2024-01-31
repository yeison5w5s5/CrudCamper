from os import system
import json
from .data import camper
def guardar():
    system("clear")
    info= {
        "nombre":str.upper(input("Ingrese su nombre: ")),
        "Apellido":str.upper(input("Ingrese su apellido: ")),
        "edad": int(input("ingrese su edad: ")),
        "hobies":"Comer"
    }
    camper.append(info)
    with open("modulos/storage/camper.json", "w") as f:
        data=json.dumps(camper, indent=4)
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

def mcamper():
    Ban=True
    while Ban:
        print("""
        Menu Camper
            1- Guardar camper
            2- Buscar Camper
            3- Editar Camper
            4- Eliminar Camper
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