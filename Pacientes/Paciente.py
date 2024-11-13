from Usuarios import Conexion as conexion
import datetime

connect = conexion.conectar()  
dataBase = connect[0]
cursor = connect[1]


class Paciente:

    def __init__(self, nombre, apellido, edad, eps, tipo_iden, num_iden):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad 
        self.eps = eps
        self.tipo_iden = tipo_iden
        self.num_iden = num_iden

    def crear(self):
        sql = "INSERT INTO pacientes VALUES (null, %s, %s, %s, %s, %s, %s)"
        paciente = (self.nombre, self.apellido, self.edad, self.eps, self.tipo_iden, self.num_iden)
    
        try:
            print(f"Ejecutando SQL: {sql} con datos: {paciente}")  # Agrega esta línea para depurar
            cursor.execute(sql, paciente)
            dataBase.commit()
            resultado = [cursor.rowcount, self]
        except Exception as e:
            print(f"Error al crear paciente: {e}")  # Muestra el error si ocurre
            resultado = [0, self]
    
        return resultado

   
    def obtenerVisitas(self, id_paciente):
        # Consulta para obtener las visitas del paciente
        sql = """
        SELECT 
            v.id AS visita_id, 
            v.razon AS razon_visita
        FROM visitas v
        WHERE v.paciente_id = %s;
        """
        cursor.execute(sql, (id_paciente,))
        resultados = cursor.fetchall()
        
        if resultados:
            return resultados  # Devuelve todas las visitas del paciente
        else:
            print("No se encontraron visitas para este paciente.")
            return None
        

    # Método para obtener las citas de un paciente
    def obtenerCitas(self, id_paciente):
        # Consulta SQL para obtener las citas del paciente
        sql = """
        SELECT 
            c.id AS cita_id, 
            c.fecha AS cita_fecha,
            c.hora AS cita_hora,
            c.estado AS cita_estado
        FROM citas c
        WHERE c.paciente_id = %s;
        """
        
        cursor.execute(sql, (id_paciente,))
        resultados = cursor.fetchall()
        
        if resultados:
            return resultados  # Devuelve todas las citas del paciente
        else:
            print("No se encontraron citas para este paciente.")
            return None
        
    def obtenerRecetas(self, id_paciente):
        # Consulta SQL para obtener las recetas del paciente desde la tabla recetas_medicas
        sql = """
        SELECT 
            id AS receta_id,
            paciente_id AS receta_paciente_id,
            tratamiento_id AS receta_tratamiento_id,
            medicamento_id AS receta_medicamento_id
        FROM recetas_medicas
        WHERE paciente_id = %s;
        """

        cursor.execute(sql, (id_paciente,))
        resultados = cursor.fetchall()

        if resultados:
            return resultados  # Devuelve las recetas del paciente
        else:
            print("No se encontraron recetas para este paciente.")
            return None
        
    def obtenerHabitacionPaciente(self, id_paciente):
        """
        Obtiene el id y estado de la habitación asignada al paciente.
        """
        sql = """
        SELECT 
            h.id AS habitacion_id,
            h.estado AS habitacion_estado
        FROM habitaciones h
        WHERE h.id_paciente = %s;
        """

        cursor.execute(sql, (id_paciente,))
        resultados = cursor.fetchall()

        if resultados:
            return resultados  # Devuelve la información de la habitación
        else:
            print("No se encontró ninguna habitación asignada para este paciente.")
            return None
        
    
    def obtenerTratamientosPaciente(self, id_paciente):
        """
        Obtiene el id, fecha de inicio, tipo y duración del tratamiento de un paciente.
        """
        sql = """
        SELECT 
            t.id AS tratamiento_id,
            t.fecha_inic AS fecha_inicio,
            t.tipo AS tipo_tratamiento,
            t.duracion AS duracion_tratamiento
        FROM tratamientos t
        WHERE t.paciente_id = %s;
        """

        cursor.execute(sql, (id_paciente,))
        resultados = cursor.fetchall()

        if resultados:
            return resultados  # Devuelve la información de los tratamientos
        else:
            print("No se encontraron tratamientos para este paciente.")
            return None