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

def validarFecha():
    año = validarNum("año", 1900, 2030)
    mes = validarNum("mes", 1, 12)
    dia = validarNum("dia", 1, 28)
    return(datetime.date(año, mes, dia))

class persona:
    def __init__(self,DNI,nombre,sexo,fecha_de_nacimiento,pais):
        self.DNI=DNI
        self.nombre=nombre
        self.sexo=sexo
        self.fecha_de_nacimiento=fecha_de_nacimiento
        self.pais=pais
        
    #chequear DNI: que sea un numero y que sea de 8 digitos
    @staticmethod
    def check_DNI(DNI):
        while len(DNI)!=8 or DNI.isnumeric()==False:
            print('El DNI esta mal ingresado')
            DNI=input("Ingrese el DNI nuevamente:")    
        return DNI

    #chequear nombre: que sea un string
    @staticmethod
    def check_nombre(nombre):
        while nombre.isnumeric()==True:
            print('El nombre debe ser un string')
            nombre=input("Ingrese el nombre nuevamente:")
        return nombre

    #chequear sexo: Femenino, Masculino, Otro
    @staticmethod
    def check_sexo(sexo):
        lista=["Femenino","Masculino","Otro"]
        while sexo not in lista:
            print('El sexo ingresado no es valido')
            sexo=input("Ingrese el sexo nuevamente:")
        return sexo


    #chequear fechadenacimiento: datetime y que sea mas chica que la fecha de hoy
    @staticmethod
    def check_fecha_de_nacimiento(fechadenacimiento):
        while fechadenacimiento > datetime.date.today():
            print('la fecha ingresada no es valida')
            fechadenacimiento=validarFecha()
        return fechadenacimiento
      
    #chequear pais: string y que pertenezca a un pais real
    @staticmethod
    def check_pais(pais):
        archivo = open('Paises.txt', 'r')
        paises = archivo.read()
        archivo.close()

        while pais not in paises:
           print('El pais ingresado no es valido')
           pais=input("Ingrese el pais nuevamente:") 
        return pais 

class empleado(persona):
    def __init__(self,DNI,nombre,sexo,fecha_de_nacimiento,pais,legajo,sector):
        super().__init__(DNI,nombre,sexo,fecha_de_nacimiento,pais)
        self.legajo=legajo
        self.sector=sector
    
    #chequear legajo: que sea un numero y de 4 digitos (y que no hay dos repetidos)
    @staticmethod
    def checklegajo(legajo, lista_empleado):

        if legajo.isnumeric()==False:
                print('El legajo debe ser un número')
                legajo=input("Ingrese el legajo nuevamente:")
                legajo=empleado.checklegajo(legajo, lista_empleado)
                
        elif(len(legajo) != 4):
            print('El legajo debe tener 4 caracteres')
            legajo=input("Ingrese el legajo nuevamente:")
            legajo = empleado.checklegajo(legajo, lista_empleado)

        else:        
            for empleado in lista_empleado:
                if(empleado.legajo == legajo):
                    print('El legajo ingresado ya existe')
                    legajo=input("Ingrese el legajo nuevamente:")
                    legajo = empleado.checklegajo(legajo, lista_empleado)
                    break
                    
        return legajo
                    
        
                             
    #chequear sector: que sea un sector preexistente
    @staticmethod
    def checksector(sector):
        lista_sectores=["Piloto","Administrativo","Tecnico"]
        while sector not in lista_sectores:
            print('El sector debe ser preexistente')
            sector=input("Ingrese el sector nuevamente:")
        return sector


