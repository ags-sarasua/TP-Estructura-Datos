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

