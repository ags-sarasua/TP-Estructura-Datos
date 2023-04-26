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

class login():
    def __init__(self,usuario,contrasenia):
        self.usuario=usuario
        self.contrasenia=contrasenia

def login (usuario,contrasenia):
        archivo=open( "Usuarios.txt" ,'a',encoding='utf-8')
        for linea in archivo:
            usu,contra=linea.strip().split(".")
            while usu==usuario and contra!=contrasenia:
                contrasenia=input(("Ingrese la contraseña nuevamente"))
            if usu!= usuario:
                archivo.write(f"\n{usuario}.{contrasenia}")
                print("Se creó el usuario")
                return True 
            if usu==usuario and contra==contrasenia:
                return True
        archivo.close()

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
            for e in lista_empleado:
                if(e.legajo == legajo):
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


class avion: #Chequeado funciona bien
    def __init__(self,nro_serie,modelo,fecha_alta,nro_vuelos_actuales,estado):
        self.nro_avion=nro_serie
        self.modelo=modelo
        self.fecha_alta=fecha_alta
        self.nro_vuelos_actuales=nro_vuelos_actuales
        self.estado=estado
        print('Se creo bien')

        
    @staticmethod
    def check_nro_serie(nro_serie):
        while(len(nro_serie)!=10 or nro_serie.isnumeric() is not True ):
            nro_serie=input('Ingrese nuevamente el nro de serie:    ')
        return nro_serie
    @staticmethod
    def check_nro_vuelos_actuales(nro_vuelos_actuales):    
        while(nro_vuelos_actuales!='1' and nro_vuelos_actuales!='0'):
            nro_vuelos_actuales=input('Ingrese nuevamente el nro de vuelos actuales:    ')
        return nro_vuelos_actuales
    @staticmethod
    def check_estado(estado):    
        while(estado not in ['En servicio','Fuera de servicio']):
            estado=input('Ingrese nuevamente el estado del avion:    ')
        return estado
        

    def eliminarAvion(nro_serie,matriz_aviones):
        for i in matriz_aviones:
            if i[0]==nro_serie:
                matriz_aviones.pop(i)
        return matriz_aviones

class vuelo:
    def __init__(self,nro_vuelo,hora,aeropuerto_salida,aeropuerto_llegada,nro_serie:avion,legajo_piloto,precio):
        self.nro_vuelo=nro_vuelo
        self.hora=hora
        self.aeropuerto_salida=aeropuerto_salida
        self.aeropuerto_llegada=aeropuerto_llegada
        self.nro_serie=nro_serie
        self.legajo_piloto=legajo_piloto
        self.precio=precio
    
    #nro_vuelo: 4 digitos numericos
    #hora: que sea una hora
    #aeropuerto salida/llegada: que sea un string
    #nro_avion: que sea un objeto de la clase avion
    #piloto: que el legajo pertenezca a un empleado del sector piloto
    #precio: int mayor a 0  
  
    @staticmethod
    def check_inputs_vuelo(nro_vuelo,precio):
        while len(nro_vuelo)!=4 or not nro_vuelo.isnumeric():
            nro_vuelo = input("Error, debe ingresar un número de 4 dígitos: ")
        while precio < 0 or not precio.isnumeric():
            precio = input("El precio tiene que ser un número positivo")
    def check_piloto(legajo_piloto,matriz_empleado):
        """while legajo_piloto not in matriz_empleado[:][-2] and matriz_empleado[:][-1] != "Piloto":
            matriz = input("Error, este piloto no existe. Intente de nuevo.")"""        
        chequear == False
        while (not chequear):
            for i in matriz_empleado:
                if i[-2] == legajo_piloto:
                    if i[-1] == "Piloto":
                        chequear = True
            legajo_piloto = input("Error, no es un piloto")
    
        
class viaje:
    def __init__(self,nro_viaje,nro_vuelo:vuelo,nro_serie:avion,fecha):
        self.nro_viaje=nro_viaje
        self.nro_vuelo=nro_vuelo
        self.nro_avion=nro_serie
        self.fecha=fecha
        self.num_pasajeros=[]
    

    def eliminarViaje(nro_viaje,matriz_viajes):
        for i in matriz_viajes:
            if i[0]==nro_viaje:
                matriz_viajes.pop(i)
        return matriz_viajes


    @staticmethod
    def check_vuelo(nro_vuelo,matriz_vuelo):
        while nro_vuelo not in matriz_vuelo[:][0]:
            nro_vuelo = input("Error, el vuelo no existe. Intente de nuevo.")
    def check_avion(nro_serie,matriz_avion):        
        while nro_serie not in matriz_avion[:][0]:
            nro_vuelo = input("Error, el avión no existe. Intente de nuevo.")  


class reserva:  #Chequeado
    def __init__(self,nro_reserva,DNI_cliente,legajo_empleado,nro_viaje,monto):
        self.nro_reserva=nro_reserva
        self.DNI_cliente=DNI_cliente
        self.empleado=legajo_empleado
        self.nro_viaje=nro_viaje
        self.monto=monto
        print('Se ejecuto bien')
        
    @staticmethod
    def check_nro_reserva(nro_reserva):
        while(nro_reserva.isnumeric()!=True or len(nro_reserva)!=4):
            nro_reserva=input('Ingrese nuevamente su nro de factura:    ')
        return nro_reserva
    
    @staticmethod
    def check_cliente(DNI_pasajero,lista_pasajero):
        while(True):
            for pasajero in lista_pasajero:
                if pasajero.DNI==DNI_pasajero:
                    return DNI_pasajero    
            DNI_pasajero=input('Ingrese nuevamente su DNI:    ')
    
    @staticmethod
    def check_empleado(legajo_empleado,lista_empleado):
        while(True):
            for empleado in lista_empleado:
                if empleado.legajo==legajo_empleado:
                    return legajo_empleado
            legajo_empleado=input('Ingrese nuevamente su Legajo:    ')
            
    @staticmethod
    def check_viaje(nro_viaje,lista_viaje):
        while(True):
            for viaje in lista_viaje:
                if viaje.nro_viaje==nro_viaje:
                    return nro_viaje
            nro_viaje=input('Ingrese nuevamente el nro de viaje:    ')        
        return nro_viaje
    
    @staticmethod
    def check_monto(monto,nro_viaje,lista_viaje,lista_vuelo):
        for viaje in lista_viaje:
            if viaje.nro_viaje==nro_viaje:
                for vuelo in lista_vuelo:
                    if viaje.nro_vuelo==vuelo.nro_vuelo:
                        while(True):
                            if vuelo.monto==monto:
                                return monto
                            else:
                                monto=input('Monto incorrecto, ingrese nuevamente su monto:    ')

    def eliminarReserva(nro_reserva,lista_reserva):
        for reserva in lista_reserva:
            if reserva.nro_reserva==nro_reserva:
                lista_reserva.pop(reserva)
                print('Se ha eliminado la reserva nro {}'.format(reserva.nro_reserva))
    
        
