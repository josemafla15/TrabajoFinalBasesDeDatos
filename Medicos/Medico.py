from Usuarios import Conexion as conexion

connect = conexion.conectar()  
dataBase = connect[0]
cursor = connect[1]


class Medico:

    def __init__(self, nombre, apellido, edad, especialidad_id):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad 
        self.especialidad_id = especialidad_id
    

    def crear(self):
            sql = "INSERT INTO medicos VALUES (null, %s, %s, %s, %s)"
            medico = (self.nombre, self.apellido, self.edad, self.especialidad_id)

            try:
                print(f"Ejecutando SQL: {sql} con datos: {medico}")  # Agrega esta línea para depurar
                cursor.execute(sql, medico)
                dataBase.commit()
                resultado = [cursor.rowcount, self]
            except Exception as e:
                print(f"Error al crear paciente: {e}")  # Muestra el error si ocurre
                resultado = [0, self]

            return resultado
        