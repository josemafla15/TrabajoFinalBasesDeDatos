from Usuarios import Conexion as conexion
import datetime

connect = conexion.conectar()  
dataBase = connect[0]
cursor = connect[1]


class RecetaMedica: 
    def __init__(self, paciente_id, tratamiento_id, medicamento_id):
        self.paciente_id = paciente_id
        self.tratamiento_id = tratamiento_id
        self.medicamento_id = medicamento_id 
        

    def crear(self):
    
        sql = "INSERT INTO recetas_medicas VALUES (null, %s, %s, %s)"
        recetaMedica = (self.paciente_id, self.tratamiento_id, self.medicamento_id)

        try:
            print(f"Ejecutando SQL: {sql} con datos: {recetaMedica}")  # Agrega esta línea para depurar
            cursor.execute(sql, recetaMedica)
            dataBase.commit()
            resultado = [cursor.rowcount, self]
        except Exception as e:
            print(f"Error al crear visita: {e}")  # Muestra el error si ocurre
            resultado = [0, self]

        return resultado