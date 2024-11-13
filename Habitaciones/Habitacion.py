from Usuarios import Conexion as conexion

connect = conexion.conectar()  
dataBase = connect[0]
cursor = connect[1]


class Habitacion:

    def __init__(self, habitacion_id, paciente_id, estado):
        self.habitacion_id = habitacion_id
        self.paciente_id = paciente_id
        self.estado = estado
        


    def ocupar(self):
        
        sql = "UPDATE habitaciones SET id_paciente = %s, estado = %s WHERE id = %s"
        habitacion = (self.paciente_id, self.estado, self.habitacion_id)
    
        try:
            print(f"Ejecutando SQL: {sql} con datos: {habitacion}")  # Agrega esta línea para depurar
            cursor.execute(sql, habitacion)
            dataBase.commit()
            resultado = [cursor.rowcount, self]
        except Exception as e:
            print(f"Error al crear visita: {e}")  # Muestra el error si ocurre
            resultado = [0, self]
    
        return resultado