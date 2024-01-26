from .data import camper
def guardar():
    print("guardando")
def buscar():
    print("buscando")
def eliminar():
    print("Eliminando")
def editar():
    print("Editar")
def menu():
    print("""Sistema de almacenamiento de datos para:
\t1- Crear
\t2- Buscar
\t3- Editar
\t4- Eliminar
\to- Salir""")
bandere=0
while bandere:
    opc=int(input)
    match (opc):
        case 1:
            guardar()
        case 2:
            buscar()
        case 3:
            editar()