from modules import camper, trainer, validate
from os import system
def menu():
    print("""Sistema de almacenamiento de datos para:
\t1- Informacion camper
\t2- Infromacion Trainer
\to- Salir""")
bandera=True
while (bandera):
    menu()
    opc=int(input())
    match(opc):
        case 1:
            system("clear")
            camper.menu()