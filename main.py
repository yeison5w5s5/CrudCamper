from os import system
from modulos import camper, trainer
def menu():
    print("""
    Este es el menu principal
        1- Menu Camper
        2- Menu Trainer
        3- Salir""")
Ban=True
while Ban:
    menu()
    opc=int(input("\t"))
    match(opc):
        case(1):
            system("clear")
            camper.mcamper()
        case(2):
            system("clear")
            trainer.mtrainer()
        case(3):
            system("clear")
            print("\t===Fin===")
            Ban=False
        case(_):
            print("otra vez")