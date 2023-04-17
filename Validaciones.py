"""
Persona tiene: DNI, nombre, sexo, edad, pais.
Validaciones:
DNI: 8 caracteres
nombre: distinto de vacío
sexo: H o M
fecha nacimiento: Tiene que ser tipo fecha, menor a día de hoy.
"""
def validarNum(tipoDato):
    ingresado = input("Ingrese " + tipoDato + ": ")
    while(ingresado.isnumeric() == False or len(ingresado)!=8):
        print("Error, debe ser un número")
        ingresado = input("Proba de vuelta: ")
    return ingresado

DNI = validarNum("DNI")

print("Este es:", DNI)

import datetime

def validarNum(tipoDato, min, max):
    ingresado = min - 1
    booleana = False
    while(booleana == False or ingresado < min or ingresado > max):
        try:
            ingresado = int(input("Ingrese "+ tipoDato +": "))
            booleana = True    
        except:
            print("Fecha invalida")       
    return ingresado

año = validarNum("año", 1900, 2030)
mes = validarNum("mes", 1, 12)
dia = validarNum("dia", 1, 31)

print(datetime.date(año, mes, dia))
