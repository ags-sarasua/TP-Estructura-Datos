class aeropuerto:
    def __init__(self, nombre, ubicacion, listaEmpleados, listaVuelos):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.listaEmpleados = listaEmpleados
        self.listaVuelos = listaVuelos
    def obtenerNombre (self):
        print("Nombre Aeropuerto: ", self.nombre)
    def obtenerUbicacion (self):
        print("El aeropuerto se encuentra en la ciudad de: ", self.ubicacion)

class Vuelo:
    listaVuelos = []
    def __init__(self, ID, fechaSalida, estado, origen, destino, aerolinea, fechaLlegada = None):
        if (ID not in Vuelo.listaVuelos):
            ID.append(Vuelo.listaVuelos)
        else:
            raise


        self.ID = ID
        self.fechaSalida = fechaSalida
        self.fechaLlegada = fechaLlegada
        self.estado = estado
        self.origen = origen
        self.destino = destino
        self.aerolinea = aerolinea     
    def ObtenerVuelo(self):

class Avion:
    def __init__(self, ID, modelo, fabricante, estado, capacidadCombustible)
        self.ID = ID
        self.fabricante = fabricante
        self.estado = estado
        self.capacidadCombustible = capacidadCombustible
    

            
