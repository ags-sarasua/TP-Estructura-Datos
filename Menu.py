
from Clases1 import *


def menu():
    registrados=[]
    
    print('1) Ingresar     2) Registrarse')
    eleccion=input('')
    while eleccion!='1' and eleccion!='2':
        eleccion=input('Ingrese datos validos')
    
    if eleccion==1:
        usuario=input('DNI: ')
        contra=input('Contrasenia:  ')   
        while [usuario,contra] not in registrados:
            print('El usuario o la contrasenia son incorrectos')
            usuario=input('DNI: ')
            contra=input('Contrasenia:  ')
        for row in ## Hay que terminarlo 
        
    
    if eleccion==2:
        print('Cree su usuario')
        usuario=input('DNI: ')
        contra1=input('Contrasenia:  ')
        while [usuario,contra1] in registrados:
            print('Identidad ya existente')
            usuario=input('DNI: ')
            contra1=input('Contrasenia:  ')
             
        contra2=input('Repita su contrasenia:   ')
        while contra1 !=contra2:
            contra2=input('Repita su contrasenia:   ')
        
        registrados.append([empleado(usuario,contra1)])  ## Hay que pedirle todos los datos
        menu()
