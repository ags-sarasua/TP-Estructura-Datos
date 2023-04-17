
from Matrices import *

class login():
    def __init__(self,usuario,contrasenia):
        self.usuario=usuario
        self.contrasenia=contrasenia
    
    # Que exista el usuario,contrasenia       y que sino la vuelva a pedir

class persona:
    def __init__(self,DNI,nombre,sexo,fecha_de_nacimiento,pais):
        self.DNI=DNI
        self.nombre=nombre
        self.sexo=sexo
        self.fecha_de_nacimiento=fecha_de_nacimiento
        self.pais=pais
        
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
    
    #chequear legajo: que sea un numero y de 4 digitos (y que no hay dos repetidos)
    #chequear sector: que sea un sector preexistente

class avion:
    def __init__(self,nro_serie,modelo,fecha_alta,nro_vuelos_actuales,estado):
        self.nro_avion=nro_serie
        self.modelo=modelo
        self.fecha_alta=fecha_alta
        self.nro_vuelos_actuales=nro_vuelos_actuales
        self.estado=estado
        
        #nro_serie: int
        #nro_serie: int 10 digitos
        #modelo: string
        #fecha_alta: fecha
        #nro_vuelos_actuales: 0 o 1
        #estado: Servicio, Fuera de servicio

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
    
        
class viaje:
    def __init__(self,nro_viaje,nro_vuelo:vuelo,nro_serie:avion,fecha):
        self.nro_viaje=nro_viaje
        self.nro_vuelo=nro_vuelo
        self.nro_avion=nro_serie
        self.fecha=fecha
        self.num_pasajeros=[]
        
    #nro_vuelo: exista en vuelo
    #nro_serie: exista en avion
    #fecha:fecha 

class reserva:
    def __init__(self,nro_factura,cliente:persona,empleado:empleado,nro_viaje:viaje,monto):
        self.cliente=nro_factura
        self.cliente=cliente
        self.empleado=empleado
        self.nro_viaje=nro_viaje
        self.monto=monto
        
    #nro_factura: nro de 4 digitos
    #cliente: que exista en la clase persona
    #empleado: que este en la clase empleado
    #viaje: que exista en viaje
    #monto: int que coincida con el precio del vuelo
        
