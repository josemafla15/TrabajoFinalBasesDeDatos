from tkinter import *
from tkinter import ttk  # Importamos ttk para el Combobox
from tkcalendar import DateEntry
from tkinter import messagebox

from Usuarios import Usuario
from Pacientes import Paciente
from Medicos import Medico
from Citas import Cita
from Visitas import Visita
from Tratamientos import Tratamiento
from RecetasMedicas import RecetaMedica
from Habitaciones import Habitacion

ventana = Tk()
ventana.title("Trabajo final BD")
ventana.geometry("500x500")

# Opciones de rol
opciones_rol = ["Recepcionista", "Admin", "Control de Calidad"]

# Variables Registro
valor_nombre = StringVar()
valor_apellidos = StringVar()
valor_correo = StringVar()
valor_contraseña = StringVar()
valor_rol = StringVar()  # Variable para el Combobox
resultados = StringVar()

# Variables Login
valor_correo_dos = StringVar()
valor_contraseña_dos = StringVar()

# Datos del usuario 
datos_usuario = []

#Variables paciente
valor_nombre_paciente = StringVar()
valor_apellido_paciente = StringVar()
valor_edad_paciente = IntVar()
valor_eps_paciente = StringVar()
valor_tipoIden_paciente = StringVar()
valor_numIden_paciente = StringVar()

#Variables medico

valor_nombre_medico = StringVar()
valor_apellido_medico = StringVar()
valor_edad_medico = IntVar()
valor_especialidad_medico = IntVar()

#Variables cita

valor_idPaciente_cita = IntVar()
valor_idMedico_cita = IntVar()
valor_fecha_cita = StringVar()
valor_hora_cita = StringVar()
valor_estado_cita = StringVar()

#Variables visita

valor_idPaciente_visita = IntVar()
valor_razon_visita = StringVar()

#Variables tratamiento

valor_idPaciente_tratamiento = IntVar()
valor_fechaInic_tratamiento = StringVar()
valor_tipo_tratamiento = StringVar()
valor_duracion_tratamiento = StringVar()

#Variables receta medica

valor_idPaciente_receta = IntVar()
valor_idTratamiento_receta = IntVar()
valor_idMedicamento_receta = IntVar()

#Variables habitacion
valor_idHabitacion_habitacion = IntVar()
valor_idPaciente_habitacion = IntVar()
valor_estado_habitacion = StringVar()

#Variables editar cita 

valor_idPaciente_editar = IntVar()
valor_idMedico_editar = IntVar()
valor_fecha_editar = StringVar()
valor_hora_editar = StringVar()
valor_estado_editar = StringVar()
valor_idCita_editar = IntVar()

#Variables ver datos paciente
valor_datosPaciente_ver = StringVar()



# Función para registrar usuario
def registrarse():

    rol_seleccionado = combobox_rol.get()
    valor_fondo = opciones_rol.index(rol_seleccionado) + 1

    usuario = Usuario.Usuario(
        valor_nombre.get(),
        valor_apellidos.get(),
        valor_correo.get(),
        valor_contraseña.get(),
        valor_fondo
    )
    
    registro = usuario.registro()

    if registro[0] >= 1:
        resultados.set("Usuario registrado")
    else:
        resultados.set("Error al crear el usuario")



def loguearse():
    usuario = Usuario.Usuario("", "", valor_correo_dos.get(), valor_contraseña_dos.get(), "")
    login = usuario.identificar()

    datos_usuario.append(login[0])
    datos_usuario.append(login[1])
    datos_usuario.append(login[2])
    datos_usuario.append(login[3])
    datos_usuario.append(login[4])
    datos_usuario.append(login[5])
    

    
    if valor_correo_dos.get() == login[3]:
            frame_texto_bienvenida.grid(row=14)
            texto_bienvenida = Label(frame_texto_bienvenida, text=f"Okay {login[1]} ingresaste a tu cuenta")
            texto_bienvenida.grid(row=14)
            siguientes_acciones(login)


def crearPaciente():
    
    paciente = Paciente.Paciente(valor_nombre_paciente.get(), valor_apellido_paciente.get(), valor_edad_paciente.get(), valor_eps_paciente.get(), valor_tipoIden_paciente.get(), valor_numIden_paciente.get())            
    creado = paciente.crear()
    
    if creado[0] >= 1:
        Label(frame_siguientes_acciones, text=f"Paciente {valor_nombre_paciente.get()} {valor_apellido_paciente.get()} creado").grid(row=14, column=0)
    else: Label(frame_siguientes_acciones, text="Fallo").grid(row=14, column=0)

    siguientes_acciones(login)
    frame_crear_paciente.grid_remove()
    frame_texto_bienvenida.grid_remove()


def crearMedico():
    # Obtener el valor seleccionado del Combobox
    especialidad_seleccionada = combobox_especialidad.get()

    # Mapeo de especialidades a valores
    especialidades_valores = {
        "Cardiología": 1,
        "Pediatría": 3,
        "Dermatología": 5
    }

    # Obtener el valor correspondiente a la especialidad
    valor_especialidad = especialidades_valores.get(especialidad_seleccionada, 0)

    # Creación del objeto Medico
    medico = Medico.Medico(
        valor_nombre_medico.get(),
        valor_apellido_medico.get(),
        valor_edad_medico.get(),
        valor_especialidad
    )
    creado = medico.crear()
    
    if creado[0] >= 1:
        Label(frame_siguientes_acciones, text=f"Médico {valor_nombre_medico.get()} creado").grid(row=14, column=0)
    else:
        Label(frame_siguientes_acciones, text="Error al crear el médico").grid(row=14, column=0)

    siguientes_acciones(login)
    frame_crear_medico.grid_remove()
    frame_texto_bienvenida.grid_remove()


def crearCita():
    # Obtención de los valores de las variables de entrada
    id_paciente = valor_idPaciente_cita.get()
    id_medico = valor_idMedico_cita.get()
    fecha_cita = valor_fecha_cita.get()
    hora_cita = valor_hora_cita.get()
    estado_cita = valor_estado_cita.get()

    # Creación de la cita
    cita = Cita.Cita(id_paciente, id_medico, fecha_cita, hora_cita, estado_cita)            
    creado = cita.crear()

    # Verificación si la cita fue creada correctamente
    if creado[0] >= 1:
        Label(frame_siguientes_acciones, text="         Cita creada         ").grid(row=14, column=0)
    else:
        Label(frame_siguientes_acciones, text="Fallo").grid(row=14, column=0)
    
    # Llamada a la siguiente acción
    siguientes_acciones(login)

    # Ocultación de las pantallas actuales
    frame_crear_cita.grid_remove()
    frame_texto_bienvenida.grid_remove()


def crearVisita():
    
    
    visita = Visita.Visita(valor_idPaciente_visita.get(), valor_razon_visita.get())            
    creado = visita.crear()
    
    if creado[0] >= 1:
        Label(frame_siguientes_acciones, text=f"         Visita creada         ").grid(row=14, column=0)
    else: Label(frame_siguientes_acciones, text="Fallo").grid(row=14, column=0)

    siguientes_acciones(login)
    frame_crear_visita.grid_remove()
    frame_texto_bienvenida.grid_remove()


def crearTratamiento():
    tratamiento = Tratamiento.Tratamiento(valor_idPaciente_tratamiento.get(), valor_fechaInic_tratamiento.get(), valor_tipo_tratamiento.get(), valor_duracion_tratamiento.get())            
    creado = tratamiento.crear()
    
    if creado[0] >= 1:
        Label(frame_siguientes_acciones, text=f"         Tratamiento creado         ").grid(row=14, column=0)
    else: Label(frame_siguientes_acciones, text="Fallo").grid(row=14, column=0)

    siguientes_acciones(login)
    frame_crear_tratamiento.grid_remove()
    frame_texto_bienvenida.grid_remove()   


def crearRecetaMedica():
    recetaMedica = RecetaMedica.RecetaMedica(
        valor_idPaciente_receta.get(),
        valor_idTratamiento_receta.get(),
        valor_idMedicamento_receta.get()  # Valor obtenido del menú desplegable (1, 2, o 3)
    )
    creado = recetaMedica.crear()

    if creado[0] >= 1:
        Label(frame_siguientes_acciones, text="         Receta médica creada         ").grid(row=14, column=0)
    else:
        Label(frame_siguientes_acciones, text="Fallo").grid(row=14, column=0)

    siguientes_acciones(login)
    frame_crear_recetaMedica.grid_remove()
    frame_texto_bienvenida.grid_remove() 

def ocuparHabitacion():
    habitacion = Habitacion.Habitacion(valor_idHabitacion_habitacion.get(), valor_idPaciente_habitacion.get(), valor_estado_habitacion.get())            
    ocupada = habitacion.ocupar()
    
    if ocupada[0] >= 1:
        Label(frame_siguientes_acciones, text=f"Habitacion ocupada").grid(row=14, column=0)
    else: Label(frame_siguientes_acciones, text="Fallo").grid(row=14, column=0)

    siguientes_acciones(login)
    frame_ocupar_habitacion.grid_remove()
    frame_texto_bienvenida.grid_remove()


def editarCita():
    # Obtención de los valores de las variables de entrada
    id_cita = valor_idCita_editar.get()  # ID de la cita a editar
    id_paciente = valor_idPaciente_editar.get()
    id_medico = valor_idMedico_editar.get()
    fecha_cita = valor_fecha_editar.get()
    hora_cita = valor_hora_editar.get()
    estado_cita = valor_estado_editar.get()

    # Crear instancia de Cita y asignar valores
    cita = Cita.Cita(id_paciente, id_medico, fecha_cita, hora_cita, estado_cita)
    
    # Editar la cita con el ID proporcionado
    editado = cita.editar(id_cita)

    # Verificación si la cita fue editada correctamente
    if editado[0] >= 1:
        Label(frame_siguientes_acciones, text="Cita editada correctamente").grid(row=14, column=0)
    else:
        Label(frame_siguientes_acciones, text="Fallo al editar la cita").grid(row=14, column=0)
    
    # Llamada a la siguiente acción
    siguientes_acciones(login)

    # Ocultación de las pantallas actuales
    frame_editar_cita.grid_remove()
    frame_texto_bienvenida.grid_remove()

def obtenerVisitasPaciente(id_paciente):
    # Crear una instancia de Paciente
    paciente = Paciente.Paciente("", "", "", "", "", "")  # Usar valores vacíos o predeterminados

    # Obtener visitas del paciente
    visitas = paciente.obtenerVisitas(id_paciente)
    frame_texto_bienvenida.grid_remove()
    frame_siguientes_acciones.grid_remove()
    return visitas


def obtenerCitasPaciente(id_paciente):
    # Crear una instancia de la clase Paciente (aunque no necesitamos todos los atributos aquí)
    paciente = Paciente.Paciente(id_paciente, "", "", "", "", "")  # Los otros atributos se dejan vacíos si no son necesarios

    # Llamar al método obtenerCitas de la clase Paciente
    return paciente.obtenerCitas(id_paciente)

def obtenerRecetasPaciente(id_paciente):
    # Crear una instancia de la clase Paciente
    paciente = Paciente.Paciente("", "", "", "", "", "")  # Aquí solo pasas los atributos no relacionados con id_paciente

    # Llamar al método obtenerRecetas y pasarle id_paciente
    return paciente.obtenerRecetas(id_paciente)

def obtenerHabitacionPaciente(id_paciente):
    # Crear una instancia de la clase Paciente
    paciente = Paciente.Paciente("", "", "", "", "", "")  # Atributos no relacionados con id_paciente

    # Llamar al método obtenerHabitacionPaciente y pasarle el id_paciente
    return paciente.obtenerHabitacionPaciente(id_paciente)

def obtenerTratamientosPaciente(id_paciente):
    # Crear una instancia de la clase Paciente
    paciente = Paciente.Paciente("", "", "", "", "", "")  # Atributos no relacionados con id_paciente

    # Llamar al método obtenerTratamientosPaciente y pasarle el id_paciente
    return paciente.obtenerTratamientosPaciente(id_paciente)

    









def siguientes_acciones(login):
    
    def crearPacienteBotones():
        frame_crear_paciente.grid(row=1)

        Label(frame_crear_paciente, text="Nombre: ").grid(row=0, column=0)
        entry_nombre = Entry(frame_crear_paciente, textvariable=valor_nombre_paciente)
        entry_nombre.grid(row=0, column=1, sticky=NW)

        Label(frame_crear_paciente, text="Apellido: ").grid(row=1, column=0)
        entry_apellido = Entry(frame_crear_paciente, textvariable=valor_apellido_paciente)
        entry_apellido.grid(row=1, column=1, sticky=NW)

        Label(frame_crear_paciente, text="Edad: ").grid(row=2, column=0)
        entry_edad = Entry(frame_crear_paciente, textvariable=valor_edad_paciente)
        entry_edad.grid(row=2, column=1, sticky=NW)
        
        Label(frame_crear_paciente, text="Eps: ").grid(row=3, column=0)
        entry_eps = Entry(frame_crear_paciente, textvariable=valor_eps_paciente)
        entry_eps.grid(row=3, column=1, sticky=NW)

        Label(frame_crear_paciente, text="Tipo identificacion: ").grid(row=4, column=0)
        entry_tipoIden = Entry(frame_crear_paciente, textvariable=valor_tipoIden_paciente)
        entry_tipoIden.grid(row=4, column=1, sticky=NW)

        Label(frame_crear_paciente, text="Numero identificacion: ").grid(row=5, column=0)
        entry_numIden = Entry(frame_crear_paciente, textvariable=valor_numIden_paciente)
        entry_numIden.grid(row=5, column=1, sticky=NW)

        Label(frame_crear_paciente, text="").grid(row=6, column=0)
        boton_crear = Button(frame_crear_paciente, text="Crear paciente")
        boton_crear.config(
            command=crearPaciente,
             bg="green",
              fg="white",
              relief="solid",
              bd=2
        )
        boton_crear.grid(row=6, column=1, sticky=NW)
        frame_siguientes_acciones.grid_remove()


    def crearMedicoBotones():
        frame_crear_medico.grid(row=1)

        Label(frame_crear_medico, text="Nombre: ").grid(row=0, column=0)
        entry_nombre = Entry(frame_crear_medico, textvariable=valor_nombre_medico)
        entry_nombre.grid(row=0, column=1, sticky=NW)

        Label(frame_crear_medico, text="Apellido: ").grid(row=1, column=0)
        entry_apellido = Entry(frame_crear_medico, textvariable=valor_apellido_medico)
        entry_apellido.grid(row=1, column=1, sticky=NW)

        Label(frame_crear_medico, text="Edad: ").grid(row=2, column=0)
        entry_edad = Entry(frame_crear_medico, textvariable=valor_edad_medico)
        entry_edad.grid(row=2, column=1, sticky=NW)

        # Menú desplegable para la especialidad
        Label(frame_crear_medico, text="Especialidad: ").grid(row=3, column=0)
        especialidades = ["Cardiología", "Pediatría", "Dermatología"]
        global combobox_especialidad
        combobox_especialidad = ttk.Combobox(frame_crear_medico, values=especialidades, state="readonly", width=30)
        combobox_especialidad.set("Selecciona una especialidad")
        combobox_especialidad.grid(row=3, column=1)

        Label(frame_crear_medico, text="").grid(row=6, column=0)
        boton_crear = Button(frame_crear_medico, text="Crear medico")
        boton_crear.config(
            command=crearMedico,
            bg="green",
            fg="white",
            relief="solid",
            bd=2
        )
        boton_crear.grid(row=6, column=1, sticky=NW)
        frame_siguientes_acciones.grid_remove()
        frame_login.grid_remove()


    
    def crearCitaBotones():
        frame_crear_cita.grid(row=1)

        Label(frame_crear_cita, text="Id Paciente: ").grid(row=0, column=0)
        entry_nombre = Entry(frame_crear_cita, textvariable=valor_idPaciente_cita)
        entry_nombre.grid(row=0, column=1, sticky=NW)

        Label(frame_crear_cita, text="Id Medico: ").grid(row=1, column=0)
        entry_apellido = Entry(frame_crear_cita, textvariable=valor_idMedico_cita)
        entry_apellido.grid(row=1, column=1, sticky=NW)

        # Selección de Fecha con DateEntry
        Label(frame_crear_cita, text="Fecha cita: ").grid(row=2, column=0)
        calendario_fecha = DateEntry(frame_crear_cita, width=18, background='darkblue', foreground='white', borderwidth=2)
        calendario_fecha.grid(row=2, column=1, sticky=NW)

        # Selección de Hora con Spinbox
        Label(frame_crear_cita, text="Hora cita: ").grid(row=3, column=0)
        spin_horas = Spinbox(frame_crear_cita, from_=0, to=23, width=5, format="%02.0f")
        spin_horas.grid(row=3, column=1, sticky=NW)
        spin_minutos = Spinbox(frame_crear_cita, from_=0, to=59, width=5, format="%02.0f")
        spin_minutos.grid(row=3, column=2, sticky=NW)

        Label(frame_crear_cita, text="Estado: ").grid(row=4, column=0)
        entry_estado = Entry(frame_crear_cita, textvariable=valor_estado_cita)
        entry_estado.grid(row=4, column=1, sticky=NW)

        # Asignación de la fecha y hora seleccionadas a las variables de valor
        def asignar_fecha_y_hora():
            # Asignar el valor de la fecha seleccionada
            valor_fecha_cita.set(calendario_fecha.get_date())  # Actualiza la variable de fecha con la fecha seleccionada

            # Asignar el valor de la hora seleccionada
            hora = f"{spin_horas.get()}:{spin_minutos.get()}"
            valor_hora_cita.set(hora)  # Actualiza la variable de hora con el valor de la hora seleccionada

        # Botón para crear cita
        boton_crear_cita = Button(
            frame_crear_cita, 
            text="Crear cita",
            command=lambda: [asignar_fecha_y_hora(), crearCita()]  # Primero asignar fecha y hora, luego crear la cita
        )
        boton_crear_cita.config(bg="green", fg="white", relief="solid", bd=2)
        boton_crear_cita.grid(row=5, column=1, sticky=NW)

        frame_siguientes_acciones.grid_remove()
        frame_login.grid_remove()
    

    def crearVisitaBotones():
        frame_crear_visita.grid(row=1)
    
        Label(frame_crear_visita, text="Id Paciente: ").grid(row=0, column=0)
        entry_nombre = Entry(frame_crear_visita, textvariable=valor_idPaciente_visita)
        entry_nombre.grid(row=0, column=1, sticky=NW)
    
        Label(frame_crear_visita, text="Razon: ").grid(row=1, column=0)
        entry_razon = Entry(frame_crear_visita, textvariable=valor_razon_visita, width=40)  # Aumenté el tamaño de la entrada
        entry_razon.grid(row=1, column=1, sticky=NW)
    
        Label(frame_crear_visita, text="").grid(row=2, column=0)
        boton_crear_visita = Button(frame_crear_visita, text="Crear visita")
        boton_crear_visita.config(
            command=crearVisita,
            bg="green",
            fg="white",
            relief="solid",
            bd=2
        )
        boton_crear_visita.grid(row=3, column=1, sticky=NW)
        frame_siguientes_acciones.grid_remove()
        frame_login.grid_remove()

    def crearTratamientoBotones():
        frame_crear_tratamiento.grid(row=1)

        Label(frame_crear_tratamiento, text="Id Paciente: ").grid(row=0, column=0)
        entry_nombre = Entry(frame_crear_tratamiento, textvariable=valor_idPaciente_tratamiento)
        entry_nombre.grid(row=0, column=1, sticky=NW)


        # Selección de Fecha con DateEntry
        Label(frame_crear_tratamiento, text="Fecha Inicio: ").grid(row=1, column=0)
        fehcaInicio = DateEntry(frame_crear_tratamiento, width=18, background='darkblue', foreground='white', borderwidth=2)
        fehcaInicio.grid(row=1, column=1, sticky=NW)

        Label(frame_crear_tratamiento, text="Tipo: ").grid(row=2, column=0)
        entry_nombre = Entry(frame_crear_tratamiento, textvariable=valor_tipo_tratamiento)
        entry_nombre.grid(row=2, column=1, sticky=NW)

        Label(frame_crear_tratamiento, text="Duracion: ").grid(row=3, column=0)
        entry_nombre = Entry(frame_crear_tratamiento, textvariable=valor_duracion_tratamiento)
        entry_nombre.grid(row=3, column=1, sticky=NW)

        def asignar_fecha_y_hora():
            # Asignar el valor de la fecha seleccionada
            valor_fechaInic_tratamiento.set(fehcaInicio.get_date())

        # Botón para crear cita
        boton_crear_tratamiento = Button(
            frame_crear_tratamiento, 
            text="Crear tratamiento",
            command=lambda:[asignar_fecha_y_hora(), crearTratamiento()]  # Primero asignar fecha y hora, luego crear la cita
        )
        boton_crear_tratamiento.config(bg="green", fg="white", relief="solid", bd=2)
        boton_crear_tratamiento.grid(row=5, column=1, sticky=NW)


       
        frame_siguientes_acciones.grid_remove()
        frame_login.grid_remove()


    def crearRecetaMedicaBotones():
        frame_crear_recetaMedica.grid(row=1)

        # Campo para el ID del paciente
        Label(frame_crear_recetaMedica, text="Paciente id: ").grid(row=0, column=0)
        entry_nombre = Entry(frame_crear_recetaMedica, textvariable=valor_idPaciente_receta)
        entry_nombre.grid(row=0, column=1, sticky=NW)

        # Campo para el ID del tratamiento
        Label(frame_crear_recetaMedica, text="Tratamiento id: ").grid(row=1, column=0)
        entry_apellido = Entry(frame_crear_recetaMedica, textvariable=valor_idTratamiento_receta)
        entry_apellido.grid(row=1, column=1, sticky=NW)

        # Opciones de medicamentos y sus valores correspondientes
        opciones_medicamento = ["Ibuprofeno", "Paracetamol", "Dolex Niños"]
        valores_medicamento = {"Ibuprofeno": 1, "Paracetamol": 2, "Dolex Niños": 3}

        # Variable para el texto visible del OptionMenu
        opcion_seleccionada = StringVar()
        opcion_seleccionada.set(opciones_medicamento[0])  # Valor por defecto: "Ibuprofeno"

        # Función para actualizar el valor numérico en `valor_idMedicamento_receta`
        def actualizar_medicamento(*args):
            medicamento = opcion_seleccionada.get()  # Obtiene el nombre del medicamento seleccionado
            valor_idMedicamento_receta.set(valores_medicamento[medicamento])  # Asigna el valor numérico correspondiente

        # Crear el OptionMenu
        menu_medicamento = OptionMenu(
            frame_crear_recetaMedica,
            opcion_seleccionada,
            *opciones_medicamento,
            command=lambda _: actualizar_medicamento()
        )
        menu_medicamento.grid(row=2, column=1, sticky=NW)

        # Botón para crear la receta médica
        boton_crear_receta = Button(frame_crear_recetaMedica, text="Crear receta médica")
        boton_crear_receta.config(
            command=crearRecetaMedica,
            bg="green",
            fg="white",
            relief="solid",
            bd=2
        )
        boton_crear_receta.grid(row=3, column=1, sticky=NW)

        frame_siguientes_acciones.grid_remove()
        frame_login.grid_remove()


    def ocuparHabitacionBotones():
        frame_ocupar_habitacion.grid(row=1)

        Label(frame_ocupar_habitacion, text="Id habitacion: ").grid(row=0, column=0)
        entry_nombre = Entry(frame_ocupar_habitacion, textvariable=valor_idHabitacion_habitacion)
        entry_nombre.grid(row=0, column=1, sticky=NW)

        Label(frame_ocupar_habitacion, text="Id paciente: ").grid(row=1, column=0)
        entry_apellido = Entry(frame_ocupar_habitacion, textvariable=valor_idPaciente_habitacion)
        entry_apellido.grid(row=1, column=1, sticky=NW)

        Label(frame_ocupar_habitacion, text="Estado: ").grid(row=2, column=0)
        entry_apellido = Entry(frame_ocupar_habitacion, textvariable=valor_estado_habitacion)
        entry_apellido.grid(row=2, column=1, sticky=NW)

        boton_ocupar_habitacion = Button(frame_ocupar_habitacion, text="Ocupar habitacion")
        boton_ocupar_habitacion.config(
            command=ocuparHabitacion,
            bg="green",
            fg="white",
            relief="solid",
            bd=2
        )
        boton_ocupar_habitacion.grid(row=3, column=1, sticky=NW)

        frame_siguientes_acciones.grid_remove()
        frame_login.grid_remove()


    def editarCitaBotones():
        frame_editar_cita.grid(row=1)

        # Campo para ingresar el ID de la cita a editar
        Label(frame_editar_cita, text="Id Cita a Editar: ").grid(row=0, column=0)
        entry_id_cita = Entry(frame_editar_cita, textvariable=valor_idCita_editar)
        entry_id_cita.grid(row=0, column=1, sticky=NW)

        # Campos de ingreso para editar cita
        Label(frame_editar_cita, text="Id Paciente: ").grid(row=1, column=0)
        entry_nombre = Entry(frame_editar_cita, textvariable=valor_idPaciente_editar)
        entry_nombre.grid(row=1, column=1, sticky=NW)

        Label(frame_editar_cita, text="Id Medico: ").grid(row=2, column=0)
        entry_apellido = Entry(frame_editar_cita, textvariable=valor_idMedico_editar)
        entry_apellido.grid(row=2, column=1, sticky=NW)

        # Selección de Fecha con DateEntry
        Label(frame_editar_cita, text="Fecha cita: ").grid(row=3, column=0)
        calendario_fecha = DateEntry(frame_editar_cita, width=18, background='darkblue', foreground='white', borderwidth=2)
        calendario_fecha.grid(row=3, column=1, sticky=NW)

        # Selección de Hora con Spinbox
        Label(frame_editar_cita, text="Hora cita: ").grid(row=4, column=0)
        spin_horas = Spinbox(frame_editar_cita, from_=0, to=23, width=5, format="%02.0f")
        spin_horas.grid(row=4, column=1, sticky=NW)
        spin_minutos = Spinbox(frame_editar_cita, from_=0, to=59, width=5, format="%02.0f")
        spin_minutos.grid(row=4, column=2, sticky=NW)

        Label(frame_editar_cita, text="Estado: ").grid(row=5, column=0)
        entry_estado = Entry(frame_editar_cita, textvariable=valor_estado_editar)
        entry_estado.grid(row=5, column=1, sticky=NW)

        # Asignación de la fecha y hora seleccionadas a las variables de valor
        def asignar_fecha_y_hora():
            valor_fecha_editar.set(calendario_fecha.get_date())
            hora = f"{spin_horas.get()}:{spin_minutos.get()}"
            valor_hora_editar.set(hora)

        # Botón para editar cita
        boton_editar_cita = Button(
            frame_editar_cita, 
            text="Editar cita",
            command=lambda: [asignar_fecha_y_hora(), editarCita()]  # Solo la edición de cita
        )
        boton_editar_cita.config(bg="blue", fg="white", relief="solid", bd=2)
        boton_editar_cita.grid(row=6, column=1, sticky=NW)

        # Ocultar otras pantallas que no sean necesarias en este contexto
        frame_siguientes_acciones.grid_remove()
        frame_login.grid_remove()


    def verVisitasPaciente():
        # Ocultar el frame_siguientes_acciones al hacer clic en "Ver visitas"
        frame_siguientes_acciones.grid_forget()  # Esto hace que desaparezca el frame

        # Redirigir al frame de ver visitas
        frame_ver_visitas.grid(row=0, column=0, sticky="nsew")

        # Configurar el grid de la ventana principal para que expanda el frame_ver_visitas
        ventana.rowconfigure(0, weight=1)  # Ajustar la ventana principal para que expanda el frame
        ventana.columnconfigure(0, weight=1)

        # Asegúrate de que las filas y columnas de frame_ver_visitas se expandan adecuadamente
        frame_ver_visitas.rowconfigure(0, weight=0)  # Fila para el ID del paciente (fija)
        frame_ver_visitas.rowconfigure(1, weight=0)  # Fila para el botón (fija)
        frame_ver_visitas.rowconfigure(2, weight=1)  # Fila para mostrar las visitas (expandible)
        frame_ver_visitas.columnconfigure(0, weight=1)  # Columna para el ID del paciente (expandible)
        frame_ver_visitas.columnconfigure(1, weight=1)  # Columna para el ID del paciente (expandible)
        frame_ver_visitas.columnconfigure(2, weight=0)  # Columna para el botón (fija)

        # Función para mostrar las visitas del paciente
        def mostrarDatosPacienteBoton():
            id_paciente = valor_datosPaciente_ver.get().strip()  # Obtener el ID del paciente y eliminar espacios

            # Verificar si el campo está vacío
            if not id_paciente:
                Label(frame_ver_visitas, text="Por favor ingresa un ID de paciente válido.", fg="red").grid(row=3, column=0, columnspan=3, sticky="nw", pady=10)
                return

            # Validar si es un número
            if not id_paciente.isdigit():
                Label(frame_ver_visitas, text="El ID debe ser un número válido.", fg="red").grid(row=3, column=0, columnspan=3, sticky="nw", pady=10)
                return

            # Convertir a entero y obtener visitas
            id_paciente = int(id_paciente)
            visitas = obtenerVisitasPaciente(id_paciente)

            # Limpiar resultados previos sin eliminar los campos de entrada y botón
            for widget in frame_ver_visitas.grid_slaves():
                if int(widget.grid_info()["row"]) > 1:
                    widget.grid_forget()

            # Mostrar las visitas del paciente si las hay
            if visitas:
                for index, visita in enumerate(visitas):
                    Label(frame_ver_visitas, text=f"Visita {index + 1}: {visita[1]}").grid(row=4 + index, column=0, columnspan=2, sticky="nw", pady=5)
            else:
                Label(frame_ver_visitas, text="No se encontraron visitas para este paciente.", fg="red").grid(row=4, column=0, columnspan=2, sticky="nw", pady=10)

            # Agregar el botón "Volver"
            def volver():
                # Ocultar el frame_ver_visitas
                frame_ver_visitas.grid_forget()

                # Volver a mostrar el frame_siguientes_acciones
                frame_siguientes_acciones.grid(row=0, column=0)

            # Crear el botón "Volver"
            boton_volver = Button(
                frame_ver_visitas,
                text="Volver",
                command=volver,
                bg="blue",
                fg="white",
                relief="solid",
                bd=2
            )
            boton_volver.grid(row=5 + len(visitas), column=0, columnspan=2, pady=10)

        # Campo para ingresar el ID del paciente
        Label(frame_ver_visitas, text="Id Paciente: ").grid(row=0, column=0, pady=10)
        entry_id_paciente = Entry(frame_ver_visitas, textvariable=valor_datosPaciente_ver)
        entry_id_paciente.grid(row=0, column=1, sticky="nw", padx=10)

        # Botón para mostrar las visitas
        boton_ver_visitas = Button(
            frame_ver_visitas,
            text="Ver visitas",
            command=mostrarDatosPacienteBoton,
            bg="blue",
            fg="white",
            relief="solid",
            bd=2
        )
        boton_ver_visitas.grid(row=0, column=2, sticky="nw", padx=10)

    def verCitasPaciente():
        # Ocultar el frame_siguientes_acciones al hacer clic en "Ver citas"
        frame_siguientes_acciones.grid_forget()  # Esto hace que desaparezca el frame

        # Redirigir al frame de ver citas
        frame_ver_citas.grid(row=0, column=0, sticky="nsew")

        # Configurar el grid de la ventana principal para que expanda el frame_ver_datos
        ventana.rowconfigure(0, weight=1)  # Ajustar la ventana principal para que expanda el frame
        ventana.columnconfigure(0, weight=1)

        # Asegurarse de que las filas y columnas de frame_ver_datos se expandan adecuadamente
        frame_ver_citas.rowconfigure(0, weight=0)  # Fila para el ID del paciente (fija)
        frame_ver_citas.rowconfigure(1, weight=0)  # Fila para el botón (fija)
        frame_ver_citas.rowconfigure(2, weight=1)  # Fila para mostrar las citas (expandicframe_ver_citas
        frame_ver_citas.columnconfigure(0, weight=1)  # Columna para el ID del paciente (expandible)
        frame_ver_citas.columnconfigure(1, weight=1)  # Columna para el ID del paciente (expandible)
        frame_ver_citas.columnconfigure(2, weight=0)  # Columna para el botón (fija)

        def mostrarDatosCitasBoton():
            id_paciente = valor_datosPaciente_ver.get().strip()  # Obtener el ID del paciente

            if not id_paciente:
                print("ID de paciente vacío.")
                Label(frame_ver_citas, text="Por favor ingresa un ID de paciente válido.", fg="red").grid(row=3, column=0, columnspan=3, sticky=NW, pady=10)
                return

            # Convertir a entero y obtener citas
            id_paciente = int(id_paciente)
            citas = obtenerCitasPaciente(id_paciente)  # Usar la función para obtener las citas

            # Limpiar resultados previos
            for widget in frame_ver_citas.grid_slaves():
                if int(widget.grid_info()["row"]) > 1:
                    widget.grid_forget()

            # Mostrar las citas del paciente si las hay
            if citas:
                for index, cita in enumerate(citas):
                    Label(frame_ver_citas, text=f"Cita {index + 1}: Fecha: {cita[1]} Hora: {cita[2]} Estado: {cita[3]}").grid(row=4 + index, column=0, columnspan=2, sticky=NW, pady=5)
            else:
                Label(frame_ver_citas, text="No se encontraron citas para este paciente.", fg="red").grid(row=4, column=0, columnspan=2, sticky=NW, pady=10)

            # Agregar el botón "Volver"
            def volver():
                # Ocultar el frame_ver_datos
                frame_ver_citas.grid_forget()

                # Volver a mostrar el frame_siguientes_acciones
                frame_siguientes_acciones.grid(row=0, column=0)

            # Crear el botón "Volver"
            boton_volver = Button(
                frame_ver_citas,
                text="Volver",
                command=volver,
                bg="blue",
                fg="white",
                relief="solid",
                bd=2
            )
            boton_volver.grid(row=4 + len(citas), column=0, columnspan=2, pady=10)

        # Campo para ingresar el ID del paciente
        Label(frame_ver_citas, text="Id Paciente: ").grid(row=0, column=0, pady=10)
        entry_id_paciente = Entry(frame_ver_citas, textvariable=valor_datosPaciente_ver)
        entry_id_paciente.grid(row=0, column=1, sticky=NW, padx=10)

        # Botón para mostrar las citas, debe estar cerca del campo de entrada
        boton_ver_citas = Button(
            frame_ver_citas,
            text="Ver citas",
            command=mostrarDatosCitasBoton
        )
        boton_ver_citas.config(bg="blue", fg="white", relief="solid", bd=2)
        boton_ver_citas.grid(row=0, column=2, sticky=NW, padx=10)

        # Configurar para expandir el contenido dentro del frame_ver_datos
        frame_ver_citas.rowconfigure(0, weight=0)  # Fila para el ID
        frame_ver_citas.rowconfigure(1, weight=0)  # Fila para el botón
        frame_ver_citas.rowconfigure(2, weight=1)  # Fila para las citas, expandible


    def verRecetasPaciente():
        # Ocultar el frame_siguientes_acciones al hacer clic en "Ver recetas"
        frame_siguientes_acciones.grid_forget()  # Esto hace que desaparezca el frame

        # Redirigir al frame de ver recetas
        frame_ver_recetas.grid(row=0, column=0, sticky="nsew")

        # Configurar el grid de la ventana principal para que expanda el frame_ver_datos
        ventana.rowconfigure(0, weight=1)  # Ajustar la ventana principal para que expanda el frame
        ventana.columnconfigure(0, weight=1)

        # Asegurarse de que las filas y columnas de frame_ver_datos se expandan adecuadamente
        frame_ver_recetas.rowconfigure(0, weight=0)  # Fila para el ID del paciente (fija)
        frame_ver_recetas.rowconfigure(1, weight=0)  # Fila para el botón (fija)
        frame_ver_recetas.rowconfigure(2, weight=1)  # Fila para mostrar las recetas (expandireframe_ver_recetas
        frame_ver_recetas.columnconfigure(0, weight=1)  # Columna para el ID del paciente (expandible)
        frame_ver_recetas.columnconfigure(1, weight=1)  # Columna para el ID del paciente (expandible)
        frame_ver_recetas.columnconfigure(2, weight=0)  # Columna para el botón (freframe_ver_recetas

        def mostrarDatosRecetasBoton():
            id_paciente = valor_datosPaciente_ver.get().strip()  # Obtener el ID del paciente

            if not id_paciente:
                print("ID de paciente vacío.")
                Label(frame_ver_recetas, text="Por favor ingresa un ID de paciente válido.", fg="red").grid(row=3, column=0, columnspan=3, sticky=NW, pady=10)
                return

            # Convertir a entero y obtener recetas
            id_paciente = int(id_paciente)
            recetas = obtenerRecetasPaciente(id_paciente)  # Usar la función para obtener las recetas

            # Limpiar resultados previos
            for widget in frame_ver_recetas.grid_slaves():
                if int(widget.grid_info()["row"]) > 1:
                    widget.grid_forget()

            # Mostrar las recetas del paciente si las hay
            if recetas:
                for index, receta in enumerate(recetas):
                    # Dado que solo recibimos 4 campos, ajustamos el acceso a la tupla
                    receta_id = receta[0]
                    receta_paciente_id = receta[1]
                    receta_tratamiento_id = receta[2]
                    receta_medicamento_id = receta[3]

                    # Mostrar los detalles de la receta
                    Label(frame_ver_recetas, text=f"Receta {index + 1}: ID Receta: {receta_id} | ID Tratamiento: {receta_tratamiento_id} | ID Medicamento: {receta_medicamento_id}").grid(
                        row=4 + index, column=0, columnspan=2, sticky=NW, pady=5)
            else:
                Label(frame_ver_recetas, text="No se encontraron recetas para este paciente.", fg="red").grid(row=4, column=0, columnspan=2, sticky=NW, pady=10)

            # Agregar el botón "Volver"
            def volver():
                # Ocultar el frame_ver_datos
                frame_ver_recetas.grid_forget()

                # Volver a mostrar el frame_siguientes_acciones
                frame_siguientes_acciones.grid(row=0, column=0)

            # Crear el botón "Volver"
            boton_volver = Button(
                frame_ver_recetas,
                text="Volver",
                command=volver,
                bg="blue",
                fg="white",
                relief="solid",
                bd=2
            )
            boton_volver.grid(row=4 + len(recetas), column=0, columnspan=2, pady=10)

        # Campo para ingresar el ID del paciente
        Label(frame_ver_recetas, text="Id Paciente: ").grid(row=0, column=0, pady=10)
        entry_id_paciente = Entry(frame_ver_recetas, textvariable=valor_datosPaciente_ver)
        entry_id_paciente.grid(row=0, column=1, sticky=NW, padx=10)

        # Botón para mostrar las recetas, debe estar cerca del campo de entrada
        boton_ver_recetas = Button(
            frame_ver_recetas,
            text="Ver recetas",
            command=mostrarDatosRecetasBoton
        )
        boton_ver_recetas.config(bg="blue", fg="white", relief="solid", bd=2)
        boton_ver_recetas.grid(row=0, column=2, sticky=NW, padx=10)

        # Configurar para expandir el contenido dentro del frame_ver_datos
        frame_ver_recetas.rowconfigure(0, weight=0)  # Fila para el ID
        frame_ver_recetas.rowconfigure(1, weight=0)  # Fila para el botón
        frame_ver_recetas.rowconfigure(2, weight=1)  # Fila para las recetas, expandible


    def verHabitacionPaciente():
        # Ocultar el frame_siguientes_acciones al hacer clic en "Ver habitación"
        frame_siguientes_acciones.grid_forget()  # Ocultar el frame actual

        # Redirigir al frame de ver habitación
        frame_ver_habitacion.grid(row=0, column=0, sticky="nsew")

        # Configurar el grid de la ventana principal para que expanda el frame_ver_habitacion
        ventana.rowconfigure(0, weight=1)
        ventana.columnconfigure(0, weight=1)

        # Asegurarse de que las filas y columnas de frame_ver_habitacion se expandan adecuadamente
        frame_ver_habitacion.rowconfigure(0, weight=0)  # Fila para el ID del paciente
        frame_ver_habitacion.rowconfigure(1, weight=0)  # Fila para el botón
        frame_ver_habitacion.rowconfigure(2, weight=1)  # Fila para mostrar la habitación
        frame_ver_habitacion.columnconfigure(0, weight=1)
        frame_ver_habitacion.columnconfigure(1, weight=1)
        frame_ver_habitacion.columnconfigure(2, weight=0)

        def mostrarDatosHabitacionBoton():
            id_paciente = valor_datosPaciente_ver.get().strip()  # Obtener el ID del paciente

            if not id_paciente:
                print("ID de paciente vacío.")
                Label(frame_ver_habitacion, text="Por favor ingresa un ID de paciente válido.", fg="red").grid(row=3, column=0, columnspan=3, sticky="nw", pady=10)
                return

            # Convertir a entero y obtener información de la habitación
            id_paciente = int(id_paciente)
            habitacion = obtenerHabitacionPaciente(id_paciente)  # Usar la función para obtener la habitación

            # Limpiar resultados previos
            for widget in frame_ver_habitacion.grid_slaves():
                if int(widget.grid_info()["row"]) > 1:
                    widget.grid_forget()

            # Mostrar los datos de la habitación si existen
            if habitacion:
                for index, hab in enumerate(habitacion):
                    habitacion_id = hab[0]
                    habitacion_estado = hab[1]

                    # Mostrar los detalles de la habitación
                    Label(frame_ver_habitacion, text=f"ID Habitación: {habitacion_id} | Estado: {habitacion_estado}").grid(
                        row=4 + index, column=0, columnspan=2, sticky="nw", pady=5)
            else:
                Label(frame_ver_habitacion, text="No se encontró ninguna habitación para este paciente.", fg="red").grid(row=4, column=0, columnspan=2, sticky="nw", pady=10)

            # Agregar el botón "Volver"
            def volver():
                # Ocultar el frame_ver_habitacion
                frame_ver_habitacion.grid_forget()

                # Volver a mostrar el frame_siguientes_acciones
                frame_siguientes_acciones.grid(row=0, column=0)

            # Crear el botón "Volver"
            boton_volver = Button(
                frame_ver_habitacion,
                text="Volver",
                command=volver,
                bg="blue",
                fg="white",
                relief="solid",
                bd=2
            )
            boton_volver.grid(row=4 + len(habitacion), column=0, columnspan=2, pady=10)

        # Campo para ingresar el ID del paciente
        Label(frame_ver_habitacion, text="Id Paciente: ").grid(row=0, column=0, pady=10)
        entry_id_paciente = Entry(frame_ver_habitacion, textvariable=valor_datosPaciente_ver)
        entry_id_paciente.grid(row=0, column=1, sticky="nw", padx=10)

        # Botón para mostrar la habitación, debe estar cerca del campo de entrada
        boton_ver_habitacion = Button(
            frame_ver_habitacion,
            text="Ver habitación",
            command=mostrarDatosHabitacionBoton
        )
        boton_ver_habitacion.config(bg="blue", fg="white", relief="solid", bd=2)
        boton_ver_habitacion.grid(row=0, column=2, sticky="nw", padx=10)

        # Configurar para expandir el contenido dentro del frame_ver_habitacion
        frame_ver_habitacion.rowconfigure(0, weight=0)  # Fila para el ID
        frame_ver_habitacion.rowconfigure(1, weight=0)  # Fila para el botón
        frame_ver_habitacion.rowconfigure(2, weight=1)  # Fila para la información de la habitación, expandible


    def verTratamientosPaciente():
        # Ocultar el frame_siguientes_acciones al hacer clic en "Ver tratamientos"
        frame_siguientes_acciones.grid_forget()

        # Redirigir al frame de ver tratamientos
        frame_ver_tratamientos.grid(row=0, column=0, sticky="nsew")

        ventana.rowconfigure(0, weight=1)
        ventana.columnconfigure(0, weight=1)

        frame_ver_tratamientos.rowconfigure(0, weight=0)
        frame_ver_tratamientos.rowconfigure(1, weight=0)
        frame_ver_tratamientos.rowconfigure(2, weight=1)
        frame_ver_tratamientos.columnconfigure(0, weight=1)
        frame_ver_tratamientos.columnconfigure(1, weight=1)
        frame_ver_tratamientos.columnconfigure(2, weight=0)

        def mostrarDatosTratamientosBoton():
            id_paciente = valor_datosPaciente_ver.get().strip()

            if not id_paciente:
                print("ID de paciente vacío.")
                Label(frame_ver_tratamientos, text="Por favor ingresa un ID de paciente válido.", fg="red").grid(row=3, column=0, columnspan=3, sticky="NW", pady=10)
                return

            id_paciente = int(id_paciente)
            tratamientos = obtenerTratamientosPaciente(id_paciente)

            for widget in frame_ver_tratamientos.grid_slaves():
                if int(widget.grid_info()["row"]) > 1:
                    widget.grid_forget()

            if tratamientos:
                for index, tratamiento in enumerate(tratamientos):
                    tratamiento_id = tratamiento[0]
                    fecha_inicio = tratamiento[1]
                    tipo_tratamiento = tratamiento[2]
                    duracion_tratamiento = tratamiento[3]

                    Label(frame_ver_tratamientos, text=f"Tratamiento {index + 1}: ID Tratamiento: {tratamiento_id} | Fecha Inicio: {fecha_inicio} | Tipo: {tipo_tratamiento} | Duración: {duracion_tratamiento}").grid(
                        row=4 + index, column=0, columnspan=2, sticky="NW", pady=5
                    )
            else:
                Label(frame_ver_tratamientos, text="No se encontraron tratamientos para este paciente.", fg="red").grid(row=4, column=0, columnspan=2, sticky="NW", pady=10)

            def volver():
                frame_ver_tratamientos.grid_forget()
                frame_siguientes_acciones.grid(row=0, column=0)

            boton_volver = Button(
                frame_ver_tratamientos,
                text="Volver",
                command=volver,
                bg="blue",
                fg="white",
                relief="solid",
                bd=2
            )
            boton_volver.grid(row=4 + len(tratamientos), column=0, columnspan=2, pady=10)

        Label(frame_ver_tratamientos, text="Id Paciente: ").grid(row=0, column=0, pady=10)
        entry_id_paciente = Entry(frame_ver_tratamientos, textvariable=valor_datosPaciente_ver)
        entry_id_paciente.grid(row=0, column=1, sticky="NW", padx=10)

        boton_ver_tratamientos = Button(
            frame_ver_tratamientos,
            text="Ver tratamientos",
            command=mostrarDatosTratamientosBoton
        )
        boton_ver_tratamientos.config(bg="blue", fg="white", relief="solid", bd=2)
        boton_ver_tratamientos.grid(row=0, column=2, sticky="NW", padx=10)

        frame_ver_tratamientos.rowconfigure(0, weight=0)
        frame_ver_tratamientos.rowconfigure(1, weight=0)
        frame_ver_tratamientos.rowconfigure(2, weight=1)

    frame_siguientes_acciones.grid(row=1)
    Label(frame_siguientes_acciones,text="Crear paciente").grid(row=0, column=0)
    boton_crear = Button(frame_siguientes_acciones, text="Crear")
    boton_crear.config(
         command=crearPacienteBotones,
         bg="green",
         fg="white"
    )
    boton_crear.grid(row=0, column=1, sticky=NW)

    Label(frame_siguientes_acciones, text="Crear medico").grid(row=1, column=0)
    boton_crear_medico = Button(frame_siguientes_acciones, text="Crear")
    boton_crear_medico.config(
         command=crearMedicoBotones,
         bg="green",
         fg="white"
    )
    boton_crear_medico.grid(row=1, column=1)

    Label(frame_siguientes_acciones, text="Crear cita").grid(row=2, column=0)
    boton_crear_cita = Button(frame_siguientes_acciones, text="Crear")
    boton_crear_cita.config(
         command=crearCitaBotones,
         bg="green",
         fg="white"
    )
    boton_crear_cita.grid(row=2, column=1)

    

    Label(frame_siguientes_acciones, text="Crear visita").grid(row=3, column=0)
    boton_crear_visita = Button(frame_siguientes_acciones, text="Crear")
    boton_crear_visita.config(
         command=crearVisitaBotones,
         bg="green",
         fg="white"
    )
    boton_crear_visita.grid(row=3, column=1)

    Label(frame_siguientes_acciones, text="Crear tratamiento").grid(row=4, column=0)
    boton_crear_tratamiento = Button(frame_siguientes_acciones, text="Crear")
    boton_crear_tratamiento.config(
         command=crearTratamientoBotones,
         bg="green",
         fg="white"
    )
    boton_crear_tratamiento.grid(row=4, column=1)

    Label(frame_siguientes_acciones, text="Crear receta medica").grid(row=5, column=0)
    boton_crear_recetaMedica = Button(frame_siguientes_acciones, text="Crear")
    boton_crear_recetaMedica.config(
         command=crearRecetaMedicaBotones,
         bg="green",
         fg="white"
    )
    boton_crear_recetaMedica.grid(row=5, column=1)

    Label(frame_siguientes_acciones, text="Ocupar habitacion").grid(row=6, column=0)
    boton_ocupar_habitacion = Button(frame_siguientes_acciones, text="Ocupar")
    boton_ocupar_habitacion.config(
         command=ocuparHabitacionBotones,
         bg="green",
         fg="white"
    )
    boton_ocupar_habitacion.grid(row=6, column=1)

    Label(frame_siguientes_acciones, text="Editar cita").grid(row=7, column=0)
    boton_editar_cita = Button(frame_siguientes_acciones, text="Editar")
    boton_editar_cita.config(
         command=editarCitaBotones,
         bg="green",
         fg="white"
    )
    boton_editar_cita.grid(row=7, column=1)

    Label(frame_siguientes_acciones, text="Ver datos paciente ").grid(row=8, column=0)
    boton_ver_datos = Button(frame_siguientes_acciones, text="Ver")
    boton_ver_datos.config(
         command=verVisitasPaciente,
         bg="green",
         fg="white"
    )
    boton_ver_datos.grid(row=8, column=1)

    Label(frame_siguientes_acciones, text="Ver citas paciente ").grid(row=9, column=0)
    boton_ver_datos = Button(frame_siguientes_acciones, text="Ver")
    boton_ver_datos.config(
         command=verCitasPaciente,
         bg="green",
         fg="white"
    )
    boton_ver_datos.grid(row=9, column=1)

    Label(frame_siguientes_acciones, text="Ver recetas medicas paciente ").grid(row=10, column=0)
    boton_ver_datos = Button(frame_siguientes_acciones, text="Ver")
    boton_ver_datos.config(
         command=verRecetasPaciente,
         bg="green",
         fg="white"
    )
    boton_ver_datos.grid(row=10, column=1)

    Label(frame_siguientes_acciones, text="Ver habitacion del paciente ").grid(row=11, column=0)
    boton_ver_datos = Button(frame_siguientes_acciones, text="Ver")
    boton_ver_datos.config(
         command=verHabitacionPaciente,
         bg="green",
         fg="white"
    )
    boton_ver_datos.grid(row=11, column=1)


    Label(frame_siguientes_acciones, text="Ver tratameintos del paciente ").grid(row=12, column=0)
    boton_ver_datos = Button(frame_siguientes_acciones, text="Ver")
    boton_ver_datos.config(
         command=verTratamientosPaciente,
         bg="green",
         fg="white"
    )
    boton_ver_datos.grid(row=12, column=1)


    Label(frame_siguientes_acciones, textvariable=datos_usuario).grid(row=13, column=0)

    
    frame_login.grid_remove()




def registro():
    frame_registro.grid(row=1)

    Label(frame_registro, text="Nombre: ").grid(row=0, column=0)
    nombre_entry = Entry(frame_registro, textvariable=valor_nombre)
    nombre_entry.grid(row=0, column=1)

    Label(frame_registro, text="Apellidos: ").grid(row=1, column=0)
    apellidos_entry = Entry(frame_registro, textvariable=valor_apellidos)
    apellidos_entry.grid(row=1, column=1)

    Label(frame_registro, text="Correo: ").grid(row=2, column=0)
    correo_entry = Entry(frame_registro, textvariable=valor_correo)
    correo_entry.grid(row=2, column=1)

    Label(frame_registro, text="Contraseña: ").grid(row=3, column=0)
    contraseña_entry = Entry(frame_registro, textvariable=valor_contraseña, show="*")
    contraseña_entry.grid(row=3, column=1)

    Label(frame_registro, text="Rol de usuario: ").grid(row=4, column=0)

    # Agregamos el Combobox
    global combobox_rol
    combobox_rol = ttk.Combobox(frame_registro, values=opciones_rol, textvariable=valor_rol, state="readonly")
    combobox_rol.set("Selecciona un rol")
    combobox_rol.grid(row=4, column=1)

    # Botón de registro
    boton_registro = Button(frame_registro, text="Registrarse", command=registrarse)
    boton_registro.config(bg="green", fg="white")
    boton_registro.grid(row=5, column=1)

    resultadito = Label(frame_registro, textvariable=resultados)
    resultadito.grid(row=6, column=0, columnspan=2)

    frame_main.grid_remove()

# Función para mostrar el formulario de login
def login():
    frame_login.grid(row=1)
    Label(frame_login, text="Vamos a loguearte").grid(row=0, column=0)
    Label(frame_login, text="Correo:").grid(row=1, column=0)
    correo_entry = Entry(frame_login, textvariable=valor_correo_dos)
    correo_entry.grid(row=1, column=1)
    Label(frame_login, text="Contraseña: ").grid(row=2, column=0)
    contraseña_entry = Entry(frame_login, textvariable=valor_contraseña_dos, show="*")
    contraseña_entry.grid(row=2, column=1)

    boton_loguearse = Button(frame_login, text="Loguearse", command=loguearse)
    boton_loguearse.config(bg="green", fg="white", relief="solid", bd=2)
    boton_loguearse.grid(row=3, column=1, sticky=NW)

    frame_main.grid_remove()
    frame_registro.grid_remove()

# Frame principal
frame_main = Frame(ventana, width=250)
frame_main.grid(row=1)

titulo = Label(frame_main, text="¿Qué acción deseas realizar?")
titulo.grid(row=0, column=3, columnspan=5, sticky=NW)

boton_registro = Button(frame_main, text="Registro", command=registro)
boton_registro.config(bg="green", fg="white")
boton_registro.grid(row=1, column=0)

boton_login = Button(frame_main, text="Login", command=login)
boton_login.config(bg="green", fg="white")
boton_login.grid(row=1, column=3)

# Frame de registro
frame_registro = Frame(ventana, width=250)

# Frame de login
frame_login = Frame(ventana, width=250)

#FRAME SIGUIENTES_ACCIONES

frame_siguientes_acciones = Frame(ventana, width=250)

#FRAME TEXTO BIENVENIDA 
frame_texto_bienvenida = Frame(frame_siguientes_acciones, width=15)

#FRAME CREAR PACIENTE 

frame_crear_paciente = Frame(ventana, width=250)

#FRAME CREAR MEDICO 

frame_crear_medico = Frame(ventana, width=250)

#FRAME CREAR CITA 

frame_crear_cita = Frame(ventana, width=250)

#FRAME CREAR VISITA 

frame_crear_visita = Frame(ventana, width=250)

#FRAME CREAR TRATAMIENTO 

frame_crear_tratamiento = Frame(ventana, width=250)

#FRAME CREAR RECETA MEDICA 

frame_crear_recetaMedica = Frame(ventana, width=250)

#FRAME OCUPAR HABITACION

frame_ocupar_habitacion = Frame(ventana, width=250)

#FRAME editar

frame_editar_cita = Frame(ventana, width=250)

#FRAME VER VISITAS

frame_ver_visitas = Frame(ventana, width=250)

#FRAME VER CITAS

frame_ver_citas = Frame(ventana, width=250)

#FRAME VER RECETAS

frame_ver_recetas = Frame(ventana, width=250)

# FRAME VER HABITACION 

frame_ver_habitacion = Frame(ventana, width=250)

# FRAME VER TRATAMIENTOS 

frame_ver_tratamientos = Frame(ventana, width=250)

ventana.mainloop()