import Clases
import checks_persona_empleado
import datetime

"""
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

def validarFecha():
    año = validarNum("año", 1900, 2030)
    mes = validarNum("mes", 1, 12)
    dia = validarNum("dia", 1, 28)
    return(datetime.date(año, mes, dia))
    
fecNac = validarFecha()
"""

"""p1 = checks_persona_empleado.persona(43917641, "Balonso", "Masculino", datetime.date(2030, 3, 2), "Argentina")

pais = p1.check_pais(p1.pais)
p1.pais = pais
print(p1.pais)"""

p1 = checks_persona_empleado.empleado(43917641, "Balonso", "Masculino", datetime.date(2030, 3, 2), "Argentino", "8473","Tecnico")
p2 = checks_persona_empleado.empleado(43917641, "Balonso", "Masculino", datetime.date(2030, 3, 2), "Argentina", "8473","Piloto")

listaEmpleados = [p1, p2]

nuevo = checks_persona_empleado.empleado.checklegajo(p2.legajo, listaEmpleados)

print(nuevo)