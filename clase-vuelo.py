from datetime import date

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
    def check_inputs(nro_vuelo,precio):
        while len(nro_vuelo)!=4 or not nro_vuelo.isnumeric():
            nro_vuelo = input("Error, debe ingresar un número de 4 dígitos: ")
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
    def check_vuelo(nro_vuelo,matriz_vuelo):
        while nro_vuelo not in matriz_vuelo[:][0]:
            nro_vuelo = input("Error, el vuelo no existe. Intente de nuevo.")
    def check_avion(nro_serie,matriz_avion):        
        while nro_serie not in matriz_avion[:][0]:
            nro_vuelo = input("Error, el avión no existe. Intente de nuevo.")            
    
  