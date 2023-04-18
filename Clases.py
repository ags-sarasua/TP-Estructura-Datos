
class login():
    def __init__(self,usuario,contrasenia):
        self.usuario=usuario
        self.contrasenia=contrasenia
    
    
    
  #preguntar si hacer una clase de login o no. hicimos este codigo pero no funciona. preguntar lo de append y read

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

    def ActualizarPersona(DNI, PorCual, indice, matriz_persona):
        for i in matriz_persona:
            if i[0] == DNI and (indice-1) < len(i):
                i[indice-1] = PorCual
        return matriz_persona



    #chequear DNI: que sea un numero y que sea de 8 digitos
    #chequear nombre: que sea un string
    #chequear sexo: Femenino, Masculino, Otro
    #chequear fechadenacimiento: datetime y que sea mas chica que la fecha de hoy
    #chequear pais: string y que pertenezca a un pais real

class empleado(persona):
    def __init__(self,DNI,nombre,sexo,fecha_de_nacimiento,pais,legajo,sector):
        super.__init__(self,DNI,nombre,sexo,fecha_de_nacimiento,pais)
        self.legajo=legajo
        self.sector=sector
    

    def eliminarEmpleado(DNI,matriz_empleado):
        for i in matriz_empleado:
            if i[0]==DNI:
                matriz_empleado.pop(i)
        return matriz_empleado

    def ActualizarEmpleado(DNI, PorCual, indice, matriz_empleado):
        for i in matriz_empleado:
            if i[0] == DNI and (indice-1) < len(i):
                i[indice-1] = PorCual
        return matriz_empleado




    #chequear legajo: que sea un numero y de 4 digitos (y que no hay dos repetidos)
    #chequear sector: que sea un sector preexistente

class avion:
    def __init__(self,nro_serie,modelo,fecha_alta,nro_vuelos_actuales,estado):
        self.nro_avion=nro_serie
        self.modelo=modelo
        self.fecha_alta=fecha_alta
        self.nro_vuelos_actuales=nro_vuelos_actuales
        self.estado=estado
        
    @staticmethod
    def check_nro_serir(nro_serie):
        while(nro_serie.isnumeric()!=True or len(nro_serie!=10)):
            nro_serie=input('Ingrese nuevamente el nro de serie:    ')
        return nro_serie
    @staticmethod
    def check_nro_vuelos_actuales(nro_vuelos_actuales):    
        while(nro_vuelos_actuales!=1 and nro_vuelos_actuales!=0):
            nro_vuelos_actuales=input('Ingrese nuevamente el nro de vuelos actuales:    ')
        return nro_vuelos_actuales
    @staticmethod
    def check_estado(estado):    
        while(estado is not 'En servicio' and estado is not 'Fuera de servicio'):
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
    
<<<<<<< HEAD

=======
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
>>>>>>> 97b19173e40baded00bc1697f98370f4da89bfe9
    
        
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

class reserva:
    def __init__(self,nro_reserva,DNI_cliente:persona,empleado:empleado,nro_viaje:viaje,monto):
        self.nro_reserva=nro_reserva
        self.DNI_cliente=DNI_cliente
        self.empleado=empleado
        self.nro_viaje=nro_viaje
        self.monto=monto
    @staticmethod
    def check_nro_reserva(nro_reserva):
        while(nro_reserva.isnumeric()!=True or len(nro_reserva!=4)):
            nro_reserva=input('Ingrese nuevamente su nro de factura:    ')
        return nro_reserva
    @staticmethod
    def check_cliente(DNI_cliente,matriz_pasajero):
        while(DNI_cliente not in matriz_pasajero[:][0]):
            DNI_cliente=input('Ingrese nuevamente su DNI:    ')
        return DNI_cliente
    @staticmethod
    def check_empleado(Legajo_empleado,matriz_empleado):
        while(Legajo_empleado not in matriz_empleado[:][-2]):
            Legajo_empleado=input('Ingrese nuevamente su Legajo:    ')
        return Legajo_empleado
    @staticmethod
    def check_viaje(nro_viaje,matriz_viaje):
        while(nro_viaje not in matriz_viaje[:][0]):
            nro_viaje=input('Ingrese nuevamente el nro de viaje:    ')        
        return nro_viaje
    @staticmethod
    def check_monto(monto,viaje,matriz_viaje,matriz_vuelo):
        nro_vuelo=0
        for i in matriz_viaje:
            if i[0]==viaje:
                i[1]=nro_vuelo
        for i in matriz_vuelo:
            if i[0]==nro_vuelo:
                while(monto!=i[-1]):
                    monto=input('Monto incorrecto, ingrese nuevamente su monto:    ')
                return monto
     
    def eliminarReserva(nro_reserva,matriz_reserva):
        for i in matriz_reserva:
            if i[0]==nro_reserva:
                matriz_reserva.pop(i)
        return matriz_reserva


    
    
        
