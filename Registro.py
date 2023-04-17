
'''
Menu
1) Registro (Matriz)
2) Examen (chequear verificacion, Modificar registro)
3) Verificacion (chequear registro)
'''


class registro:

    def __init__(self, DNI: int,codigo: str,tipo_licencia: str,codigo_empleado: str):
        self.DNI=DNI
        self.codigo=codigo
        self.tipo_licencia=tipo_licencia
        #self.num_tramite=DNI+codigo_empleado+tipo_licencia

    @staticmethod
    def check_inputs(DNI,codigo,tipo_licencia):
        if len(DNI)!=8 or not DNI.isnumeric():
            raise ValueError('El DNI esta mal ingresado')
        if not codigo[:3].isupper() or not codigo[1:].isnumeric() or len(codigo)!=5:
            raise ValueError('El codigo esta mal ingresado')
        if tipo_licencia not in ['PRO','PAR']:
            raise ValueError('El tipo de licencia esta mal ingresado')
    @staticmethod
    def check_registro_previo_F(DNI,matriz_registro):
        if DNI in matriz_registro[:][0]:
            raise ValueError('Ya esta registrado')
    @staticmethod
    def check_registro_previo_V(DNI,matriz_registro):
        if DNI not in matriz_registro[:][0]:
            raise ValueError('No esta registrado')

matriz_persona=[]
inputs = []
print('1)DNI, 2)Codigo, 3)Tipo de licencia')
for i in range(3):
    user_input = str(input("Inroduzca {} :".format(i+1)))
    inputs.append(user_input)
try:
    registro.check_registro_previo_F(inputs[0],matriz_persona)
    registro.check_inputs(inputs[0], inputs[1], inputs[2])
except: print("Error: {}".format(ValueError))
else: matriz_persona.append(registro(inputs[0], inputs[1], inputs[2]))




