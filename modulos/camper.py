from os import system
import json
from .data import camper, generos
def info():
    info1= {
        "nombre":str.upper(input("Ingrese su nombre: ")),
        "apellido":str.upper(input("Ingrese su apellido: ")),
        "edad": int(input("ingrese su edad: ")),
        "genero": input("Elija su genero:\n\t"+"\t".join([f"{generos.index(i)+1}. {i}\n" for i in sorted(generos)]))
    }
    return info1

def tabla():
    print("""
        -codigo -- Nombre-       - Apellido -        - Edad -        - Genero-
    """)
    for i,val in enumerate(camper):
        print(f"""
        _____________________________________________________________________________
         -{i+1}       {val.get('nombre')}       {val.get('apellido')}           {val.get('edad')}          {val.get('genero')}
        _____________________________________________________________________________""")

def camper1(codigo):
    print(f"""
    ________________________
    Codigo: {codigo}
    Nombre: {camper[codigo-1].get('nombre')}
    Apellido: {camper[codigo-1].get('apellido')}
    Edad: {camper[codigo-1].get('edad')}
    Genero: {camper[codigo-1].get('genero')}
    ________________________
    """)

def guardar():
    system("clear")
    info1=info()
    camper.append(info1)
    with open("modulos/storage/camper.json", "w") as f:
        data=json.dumps(camper, indent=4)
        f.write(data)
        f.close()
        return "Sucessfully Camper"    
def buscar():
    system("clear")
    #numerate me da el valor y el index
    tabla()
    return "The camper is available"
def editar():
    system("clear")
    tabla()
    print("""
                ___________________________
                * Acualizacion del camper *
                ___________________________
    """)
    codigo = int(input("Ingrese el codigo del camper que deseas actualizar: "))
    camper1(codigo)
    print("¿Este es el camper que deseas actualizar?")
    bandera=True
    while (bandera):
        print("1. Si")
        print("2. No")
        print("3. Salir")
        opc = int(input())
        if(opc == 1):
            info1=info()
            camper[(codigo-1)] = info1
            with open("modulos/storage/camper.json", "w") as f:
                data = json.dumps(camper, indent=4)
                f.write(data)
                f.close()
                bandera = False
        elif(opc ==2):
            bandera=False
        elif(opc == 3):
            bandera = False
    return "Edit to camper"
def eliminar():
    system("clear")
    tabla()
    print("""
                ___________________________
                * Eliminacion del camper *
                ___________________________
    """)
    codigo = int(input("Ingrese el codigo del camper que deseas actualizar: "))
    camper1(codigo)
    print("¿Este es el camper que deseas actualizar?")
    bandera=True
    while (bandera):
        print("1. Si")
        print("2. No")
        print("3. Salir")
        opc = int(input())
        if(opc == 1):
            camper.pop(codigo-1)
            with open("modulos/storage/camper.json", "w") as f:
                data = json.dumps(camper, indent=4)
                f.write(data)
                f.close()
            bandera = False

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