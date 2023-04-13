# TP-Estructura-Datos

Clases 

Aeropuerto: información general sobre el aeropuerto, nombre, ubicación. (EL MAIN)
Avión: modelo: el modelo del avión (cadena de caracteres),fabricante: el fabricante del avión (cadena de caracteres), capacidad: la cantidad de pasajeros que el avión puede transportar (entero).
Vuelo (Padre): representa un vuelo y contiene información sobre número de vuelo, origen, destino, hora de salida, llegada, fecha de alta y fecha de baja.  
Viaje (Hijo): un vuelo de un día específico. Tiene hora de salida, llegada, estado del vuelo y puerta.
Aerolínea: cada una puede tener el permiso o no de mantener vuelos regulares en el aeropuerto. Cada aerolínea tiene sus aviones y, por ende, sus vuelos.
Ticket: Reserva del vuelo que compró el pasajero. 
Cliente: información, número de pasaporte y asiento
Persona: nombre, dni datos básicos
Empleado: tipo de trabajo, sueldo, credencial
Terminal: A,B,C es un conjunto de puertas según destinos
Ciudad:
País:

Opcionales: salas vip

Posible Herencia:
Persona
Cliente
Empleado
Aeropuerto
Terminal
Avión
Vuelo
Vuelo (posible herencia múltiple)
Aeropuerto
Avión
Viaje
Vuelo
Ticket
Aerolínea
Ticket

Métodos
Aeropuerto
__init__(self, nombre, ubicación): constructor que inicializa los atributos de la clase Aeropuerto con un nombre y ubicación específicos.
obtener_nombre(self): método que devuelve el nombre del aeropuerto.
obtener_ubicacion(self): método que devuelve la ubicación del aeropuerto.
agregar_terminal(self, terminal): método que agrega una nueva terminal al aeropuerto.
obtener_terminales(self): método que devuelve una lista de todas las terminales del aeropuerto.
agregar_vuelo(self, vuelo): Método que agrega un objeto de la clase Vuelo a la lista de vuelos del aeropuerto. El vuelo si o si tiene que ser desde o hasta nuestro aeropuerto en cuestión.
eliminar_vuelo(self, vuelo): Método que elimina un objeto de la clase Vuelo de la lista de vuelos del aeropuerto.
obtener_vuelos(self): Método que devuelve una lista de todos los vuelos que salen del aeropuerto en una fecha específica.
agregar_avion(self, nuevo_avion): método que agrega un nuevo avión al aeropuerto.
eliminar_avion(self, id_avion): método que elimina el avión correspondiente al ID especificado.
obtener_empleados(self): método que devuelve la lista de empleados que trabajan en el aeropuerto.
contratar_empleado(self, nuevo_empleado): método que contrata un nuevo empleado para trabajar en el aeropuerto.
despedir_empleado(self, dni_empleado): método que despide al empleado correspondiente al DNI especificado.


Avión 
__init__(self, modelo, capacidad): Método constructor que crea una instancia de la clase Avión con el modelo y la capacidad del avión.
realizar_vuelo(self): Método que incrementa el número de vuelos realizados por el avión.
obtener_modelo(self): método que devuelve el modelo del avión.
obtener_fabricante(self): método que devuelve el fabricante del avión.
obtener_capacidad(self): método que devuelve la capacidad del avión.
obtener_estado(self): método que devuelve el estado actual del avión (por ejemplo, "en tierra", "en vuelo", "en mantenimiento", etc.).
cambiar_estado(self, nuevo_estado): método que cambia el estado actual del avión por el valor especificado.

Vuelo
__init__(self, número, aerolínea, origen, destino, fecha_salida, fecha_llegada): constructor que inicializa los atributos de la clase Vuelo con un número de vuelo, aerolínea, origen, destino, fecha de salida y fecha de llegada específicos.
obtener_numero(self): método que devuelve el número de vuelo.
obtener_aerolinea(self): método que devuelve la aerolínea del vuelo.
obtener_origen(self): método que devuelve el origen del vuelo.
obtener_destino(self): método que devuelve el destino del vuelo.
obtener_fecha_salida(self): método que devuelve la fecha de salida del vuelo.
obtener_fecha_llegada(self): método que devuelve la fecha de llegada del vuelo.
agregar_pasajero(self, pasajero): Método que agrega un objeto de la clase Pasajero a la lista de pasajeros del vuelo.
eliminar_pasajero(self, pasajero): Método que elimina un objeto de la clase Pasajero de la lista de pasajeros del vuelo.
obtener_pasajeros(self): Método que devuelve una lista de todos los pasajeros en el vuelo.
verificar_disponibilidad(self): Método que verifica si hay asientos disponibles en el vuelo.
clase viaje:
obtener_vuelo(self): método que devuelve el vuelo del viaje.
obtener_fecha(self): método que devuelve la fecha del viaje.
agregar_ticket(self, ticket): método que agrega un nuevo ticket al viaje.
obtener_tickets(self): método que devuelve una lista de todos los tickets del viaje.
obtener_distancia(self): método que devuelve la distancia entre los aeropuertos de origen y destino.
Aerolínea
__init__(self, nombre, pais, flota): constructor que inicializa los atributos de la clase Aerolínea con un nombre, país y flota específicos.
obtener_nombre(self): método que devuelve el nombre de la aerolínea.
obtener_pais(self): método que devuelve el país de la aerolínea.
obtener_flota(self): método que devuelve la flota de la aerolínea.
agregar_vuelo(self, vuelo): método que agrega un nuevo vuelo a la aerolínea.
eliminar_vuelo(self,vuelo): método que elimina un vuelo a la aerolínea.
obtener_vuelos(self): método que devuelve una lista de todos los vuelos de la aerolínea. Puede filtrarse por tiempos.
Pasajero
__init__(self, nombre, num_pasaporte, asiento_asignado): Método constructor que crea una instancia de la clase Pasajero con los datos del pasajero.
asignar_asiento(self, num_asiento): Método que asigna un número de asiento específico a un pasajero.
obtener_ticket(self): método que devuelve el objeto Ticket correspondiente al vuelo en el que el pasajero está viajando.
obtener_vuelo(self): método que devuelve el objeto Vuelo correspondiente al vuelo en el que el pasajero está viajando.
Ticket
__init__(self, viaje, pasajero, asiento): constructor que inicializa los atributos de la clase Ticket con un viaje, pasajero y asiento específicos.
obtener_viaje(self): método que devuelve el viaje asociado con el ticket.
obtener_pasajero(self): método que devuelve el pasajero asociado con el ticket.
obtener_asiento(self): método que devuelve el asiento asociado con el ticket.
obtener_codigo(self): método que devuelve el código del ticket.
obtener_precio(self): método que devuelve el precio del ticket.
cambiar_precio(self, nuevo_precio): método que cambia el precio del ticket por el valor especificado.
obtener_origen(self): método que devuelve el aeropuerto de origen del ticket.
obtener_destino(self): método que devuelve el aeropuerto de destino del ticket.
cambiar_destino(self, nuevo_destino): método que cambia el aeropuerto de destino del ticket por el valor especificado.
obtener_fecha_vuelo(self): método que devuelve la fecha de vuelo del ticket.
cambiar_fecha_vuelo(self, nueva_fecha): método que cambia la fecha de vuelo del ticket por la fecha especificada.
obtener_pasajero(self): método que devuelve el pasajero asociado al ticket.
cambiar_pasajero(self, nuevo_pasajero): método que cambia el pasajero asociado al ticket por el valor especificado.
obtener_asiento(self): método que devuelve el número de asiento del ticket.
cambiar_asiento(self, nuevo_asiento): método que cambia el número de asiento del ticket por el valor especificado.
obtener_estado(self): método que devuelve el estado del ticket (por ejemplo, "reservado", "confirmado", "cancelado", etc.).
cambiar_estado(self, nuevo_estado): método que cambia el estado del ticket por el valor especificado.
Cliente
__init__(self, nombre, apellido, correo_electronico, telefono): constructor que inicializa los atributos de la clase Cliente con un nombre, apellido, correo electrónico y teléfono específicos.
obtener_nombre(self): método que devuelve el nombre del cliente.
obtener_apellido(self): método que devuelve el apellido del cliente.
obtener_correo_electronico(self): método que devuelve el correo electrónico del cliente.
obtener_telefono(self): método que devuelve el número de teléfono del cliente.
obtener_tickets(self): método que devuelve una lista de todos los tickets asociados con el cliente.
Persona
__init__(self, nombre, apellido, fecha_nacimiento, género): constructor que inicializa los atributos de la clase Persona con un nombre, apellido, fecha de nacimiento y género específicos.
obtener_nombre(self): método que devuelve el nombre de la persona.
obtener_apellido(self): método que devuelve el apellido de la persona.
obtener_fecha_nacimiento(self): método que devuelve la fecha de nacimiento de la persona.
obtener_genero(self): método que devuelve el género de la persona.
actualizar_nombre(self, nuevo_nombre): método que actualiza el nombre de la persona.
actualizar_apellido(self, nuevo_apellido): método que actualiza el apellido de la persona.
actualizar_fecha_nacimiento(self, nueva_fecha): método que actualiza la fecha de nacimiento de la persona.
actualizar_genero(self, nuevo_genero): método que actualiza el género de la persona.
obtener_edad(self): método que devuelve la edad de la persona.
es_mayor_de_edad(self): método que verifica si la persona es mayor de edad. Devuelve True si la edad es mayor o igual a 18, de lo contrario, devuelve False
verificar_documento_identidad (self, numero_documento): método que verifica si el número de documento de identidad especificado es igual al número de documento de identidad de la persona. Devuelve True si son iguales, de lo contrario, devuelve False.
obtener_historial_: (ver proximos vuelos y anteriores)
Empleado
__init__(self, nombre, apellido, fecha_nacimiento, género, fecha_contratacion, cargo, salario): constructor que inicializa los atributos de la clase Empleado con un nombre, apellido, fecha de nacimiento, género, fecha de contratación, cargo y salario específicos.
obtener_fecha_contratacion(self): método que devuelve la fecha de contratación del empleado.
obtener_cargo(self): método que devuelve el cargo del empleado.
obtener_salario(self): método que devuelve el salario del empleado.
actualizar_fecha_contratacion(self, nueva_fecha): método que actualiza la fecha de contratación del empleado.
actualizar_cargo(self, nuevo_cargo): método que actualiza el cargo del empleado.
actualizar_salario(self, nuevo_salario): método que actualiza el salario del empleado.
asignar_terminal(self, terminal): método que asigna al empleado a la terminal especificada.
obtener_terminal_asignada(self): método que devuelve la terminal a la que está asignado el empleado.
obtener_informacion(self): método que devuelve un diccionario con la información básica del empleado (nombre, apellido, cargo y salario).
verificar_disponibilidad(self, vuelo): método que verifica si hay disponibilidad para asignar al empleado al vuelo especificado. Si hay disponibilidad, el método devuelve True, de lo contrario, devuelve False.
Terminal
__init__(self, número, aeropuerto): constructor que inicializa los atributos de la clase Terminal con un número de terminal y aeropuerto específicos.
obtener_numero(self): método que devuelve el número de la terminal.
agregar_aerolinea(self, aerolínea): método que agrega un objeto de la clase Aerolínea a la lista de aerolíneas que operan en la terminal.
eliminar_aerolinea(self, aerolínea): método que elimina un objeto de la clase Aerolínea de la lista de aerolíneas que operan en la terminal.
obtener_vuelos_salida(self, fecha): método que devuelve una lista de objetos de la clase Vuelo que tienen como terminal de salida la terminal actual y que están programados para la fecha especificada.
obtener_vuelos_llegada(self, fecha): método que devuelve una lista de objetos de la clase Vuelo que tienen como terminal de llegada la terminal actual y que están programados para la fecha especificada.
obtener_vuelos_programados(self): método que devuelve una lista de objetos de la clase Vuelo programados para la terminal.
obtener_tickets_vendidos(self): método que devuelve una lista de objetos de la clase Ticket vendidos para la terminal.
