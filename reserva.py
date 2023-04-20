
#Chequeado

from Clases import *

class reserva:  #Cehqueado
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

reserva.check_nro_reserva('1221')
reserva1=reserva('1111','121212121','1111','121','1')