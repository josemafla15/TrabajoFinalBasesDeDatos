from Usuarios import Conexion as conexion
import datetime

connect = conexion.conectar()  
dataBase = connect[0]
cursor = connect[1]

class Visita:

    def __init__(self, paciente_id, razon):
        self.paciente_id = paciente_id
        self.razon = razon

    def crear(self):
        

        sql = "INSERT INTO visitas VALUES (null, %s, %s)"
        visita = (self.paciente_id, self.razon)
    
        try:
            print(f"Ejecutando SQL: {sql} con datos: {visita}")  # Agrega esta línea para depurar
            cursor.execute(sql, visita)
            dataBase.commit()
            resultado = [cursor.rowcount, self]
        except Exception as e:
            print(f"Error al crear visita: {e}")  # Muestra el error si ocurre
            resultado = [0, self]
    
        return resultado

       