from Usuarios import Conexion as conexion
import datetime

connect = conexion.conectar()  
dataBase = connect[0]
cursor = connect[1]

class Cita:

    def __init__(self, paciente_id, medico_id, fecha, hora, estado):
        self.paciente_id = paciente_id
        self.medico_id = medico_id
        self.fecha = fecha
        self.hora = hora 
        self.estado = estado
    
    def crear(self):
        

        sql = "INSERT INTO citas VALUES (null, %s, %s, %s, %s, %s)"
        cita = (self.paciente_id, self.medico_id, self.fecha, self.hora, self.estado)
    
        try:
            print(f"Ejecutando SQL: {sql} con datos: {cita}")  # Agrega esta línea para depurar
            cursor.execute(sql, cita)
            dataBase.commit()
            resultado = [cursor.rowcount, self]
        except Exception as e:
            print(f"Error al crear paciente: {e}")  # Muestra el error si ocurre
            resultado = [0, self]
    
        return resultado


    def editar(self, id_cita):
    
        sql = """
        UPDATE citas 
        SET paciente_id = %s, medico_id = %s, fecha = %s, hora = %s, estado = %s 
        WHERE id = %s
        """
        cita = (self.paciente_id, self.medico_id, self.fecha, self.hora, self.estado, id_cita)
    
        try:
            print(f"Ejecutando SQL: {sql} con datos: {cita}")  # Mensaje para depuración
            cursor.execute(sql, cita)
            dataBase.commit()
            resultado = [cursor.rowcount, self]
        except Exception as e:
            print(f"Error al editar la cita: {e}")  # Mensaje de error
            resultado = [0, self]
    
        return resultado
    

    