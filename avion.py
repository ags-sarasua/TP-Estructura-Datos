
#Chequeado funciona bien

class avion:
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
    
avion.check_nro_serie('1111111111')
avion.check_nro_vuelos_actuales('1')

avion.check_estado('En servicioi')



avion1=avion(1111111111,'momo','1212',1,'En servicio')

avion2=avion('11111111','momo','1212',1,'En servicio')
print(avion1)