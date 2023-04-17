

from Matrices import *

class persona:
    def __init__(self,DNI,sexo,edad,pais):
        self.DNI=DNI
        self.sexo=sexo
        self.edad=edad
        self.pais=pais
        #cantidad de vuelos
        
class empleado(persona):
    def __init__(self,DNI,contrasenia,sexo,edad,pais,legajo):
        super.__init__(self,DNI,sexo,edad,pais)
        self.legajo=legajo
        self.contrasenia=contrasenia
        

class administrativo(empleado):
    def __init__(self,DNI,sexo,edad,pais,legajo,sector="administrativo"):
        super.__init__(self,DNI,sexo,edad,pais,legajo)
        self.sector=sector

    def asignar_puerta(self,vuelos,puertas):
        vuelo=input('Ingrese vuelo a asignar:   ')
        puerta=input('Ingrese puerta deseada:    ')
        dia=input('Ingrese el dia:  ')
        
            
class tecnico(empleado):
    def __init__(self,DNI,sexo,edad,pais,legajo,sector="tecnico"):
        super.__init__(self,DNI,sexo,edad,pais,legajo)
        self.sector=sector


class cliente(persona):
    def __init__(self,DNI,sexo,edad,pais):
        super.__init__(self,DNI,sexo,edad,pais)
    
    def verificar_buscado(self,lista_buscados):
        if self.DNI not in lista_buscados:
            return False
        else:
            return True 
    
    def verificar_ticket(self,tickets):
        if self.DNI in tickets[:][0]:
            return True
        else:
            return False
        