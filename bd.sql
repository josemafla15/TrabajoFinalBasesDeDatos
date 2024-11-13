CREATE DATABASE IF NOT EXISTS hospital;
USE hospital;

CREATE TABLE roles(
    id int(255) auto_increment not null,
    nombre varchar(255),
    CONSTRAINT pk_rol PRIMARY KEY(id)
) ENGINE = InnoDb;

CREATE TABLE especialidades(
    id int(255) auto_increment not null,
    nombre varchar(255),
    CONSTRAINT pk_especialidades PRIMARY KEY(id)
) ENGINE = InnoDb;

CREATE TABLE medicamentos(
    id int(255) auto_increment not null,
    nombre varchar(255),
    CONSTRAINT pk_medicamentos PRIMARY KEY(id)
) ENGINE = InnoDb;

CREATE TABLE pacientes(
    id int(255) auto_increment not null,
    nombre varchar(255),
    apellido varchar(255),
    edad int(200),
    EPS varchar(255),
    tipo_iden varchar(255),
    num_iden int(255),
    CONSTRAINT pk_pacientes PRIMARY KEY(id)
) ENGINE = InnoDb;

CREATE TABLE usuarios(
    id int(255) auto_increment not null,
    nombre varchar(255),
    apellido varchar(255),
    correo varchar(255) not null,
    password varchar(255) not null,
    rol_id int(255) not null,
    CONSTRAINT pk_usuarios PRIMARY KEY(id),
    CONSTRAINT fk_rol_usuario FOREIGN KEY(rol_id) REFERENCES roles(id)
) ENGINE = InnoDb;

CREATE TABLE medicos(
    id int(255) auto_increment not null,
    nombre varchar(255),
    apellido varchar(255),
    edad int(255),
    especialidad_id int(255),
    CONSTRAINT pk_medicos PRIMARY KEY(id),
    CONSTRAINT fk_especialidad_medico FOREIGN KEY(especialidad_id) REFERENCES especialidades(id)
) ENGINE = InnoDb;

CREATE TABLE tratamientos(
    id int(255) auto_increment not null,
    paciente_id int(255),
    fecha_inic date,
    tipo varchar(255),
    duracion varchar(255),
    CONSTRAINT pk_tratamientos PRIMARY KEY(id),
    CONSTRAINT fk_pacientes_tratamientos FOREIGN KEY(paciente_id) REFERENCES pacientes(id)
) ENGINE = InnoDb;

CREATE TABLE citas(
    id int(255) auto_increment not null,
    paciente_id int(255) not null,
    medico_id int(255) not null,
    tratamiento_id int(255) not null,
    CONSTRAINT pk_citas PRIMARY KEY(id),
    CONSTRAINT fk_pacientes_citas FOREIGN KEY(paciente_id) REFERENCES pacientes(id),
    CONSTRAINT fk_medicos_citas FOREIGN KEY(medico_id) REFERENCES medicos(id),
    CONSTRAINT fk_tratamiento_citas FOREIGN KEY(tratamiento_id) REFERENCES tratamientos(id)
) ENGINE = InnoDb;

CREATE TABLE visitas(
    id int(255) auto_increment not null,
    paciente_id int(255),
    razon varchar(255),
    CONSTRAINT pk_visitas PRIMARY KEY(id),
    CONSTRAINT fk_pacientes_visitas FOREIGN KEY(paciente_id) REFERENCES pacientes(id)
) ENGINE = InnoDb;

CREATE TABLE recetas_medicas(
    id int(255) auto_increment not null,
    paciente_id int(255),
    tratamiento_id int(255),
    medicamento_id int(255),
    CONSTRAINT pk_recetas_medicas PRIMARY KEY(id),
    CONSTRAINT fk_pacientes_recetasM FOREIGN KEY(paciente_id) REFERENCES pacientes(id),
    CONSTRAINT fk_tratamiento_recetasM FOREIGN KEY(tratamiento_id) REFERENCES tratamientos(id),
    CONSTRAINT fk_medicamento_recetasM FOREIGN KEY(medicamento_id) REFERENCES medicamentos(id)
) ENGINE = InnoDb;