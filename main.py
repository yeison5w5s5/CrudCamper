from os import system
from modulos import camper, trainer
import json

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
            with open("modulos/storage/camper.json", "r") as f:
                camper.camper=json.loads(f.read())
                f.close()
                system("clear")
                camper.mcamper()
        case(2):
            with open("modulos/storage/trainer.json", "r") as f:
                trainer.trainer=json.loads(f.read())
                f.close()
                system("clear")
                trainer.mtrainer()
        case(3):
            system("clear")
            print("\t===Fin===")
            Ban=False
        case(_):
            print("otra vez")