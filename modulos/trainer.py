from os import system
from .data import trainer
import json
print("Hola")
def trainer1(codigo):
    print(f"""
    ________________________
    Codigo: {codigo}
    Nombre: {trainer[codigo-1].get('nombre')}
    Apellido: {trainer[codigo-1].get('apellido')}
    Edad: {trainer[codigo-1].get('edad')}
    Genero: {trainer[codigo-1].get('genero')}
    Materia: {trainer[codigo-1].get('materia')}
    ________________________
    """)
def tabla():
    print("""
        -codigo -- Nombre-       - Apellido -           - Edad -- Genero-         -Materia-
    """)
    for i,val in enumerate(trainer):
        print(f"""
        _____________________________________________________________________________
         -{i+1}       {val.get('nombre')}       {val.get('apellido')}           {val.get('edad')}          {val.get('genero')}          {val.get('materia')}
        _____________________________________________________________________________""")
def info():
    info1= {
        "nombre":str.upper(input("Ingrese su nombre: ")),
        "apellido":str.upper(input("Ingrese su apellido: ")),
        "edad": int(input("ingrese su edad: ")),
        "genero": str.upper(input("Ingrese su Genero: ")),
        "materia":str.upper(input("Ingrese su Materia: "))
    }
    return info1
def guardar():
    system("clear")
    info1=info()
    trainer.append(info1)
    with open("modulos/storage/trainer.json", "w") as f:
        data=json.dumps(trainer, indent=4)
        f.write(data)
        f.close()
        return "Sucessfully Camper"
def buscar():
    system("clear")
    tabla()
def editar():
    system("clear")
    system("clear")
    tabla()
    print("""
                ___________________________
                * Acualizacion del Trainer*
                ___________________________
    """)
    codigo = int(input("Ingrese el codigo del Trainer que deseas actualizar: "))
    trainer1(codigo)
    print("¿Este es el camper que deseas actualizar?")
    bandera=True
    while (bandera):
        print("1. Si")
        print("2. No")
        print("3. Salir")
        opc = int(input())
        if(opc == 1):
            info1=info()
            trainer[(codigo-1)] = info1
            with open("modulos/storage/trainer.json", "w") as f:
                data = json.dumps(trainer, indent=4)
                f.write(data)
                f.close()
                bandera = False
        elif(opc ==2):
            bandera=False
        elif(opc == 3):
            bandera = False
    return "Edit to Trainer"
def eliminar():
    system("clear")
    system("clear")
    tabla()
    print("""
                ___________________________
                * Eliminacion del camper *
                ___________________________
    """)
    codigo = int(input("Ingrese el codigo del camper que deseas actualizar: "))
    trainer1(codigo)
    print("¿Este es el camper que deseas actualizar?")
    bandera=True
    while (bandera):
        print("1. Si")
        print("2. No")
        print("3. Salir")
        opc = int(input())
        if(opc == 1):
            trainer.pop(codigo-1)
            with open("modulos/storage/trainer.json", "w") as f:
                data = json.dumps(trainer, indent=4)
                f.write(data)
                f.close()
            bandera = False
        elif opc==2:
            bandera==False
        elif opc==3:
            bandera=False

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