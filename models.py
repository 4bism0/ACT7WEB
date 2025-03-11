from config import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    rol = db.Column(db.Enum('ESTUDIANTE', 'DOCENTE', 'ADMINISTRATIVO'), nullable=False)
    grupo_id = db.Column(db.Integer, db.ForeignKey('grupos.id'))

class Grupo(db.Model):
    __tablename__ = 'grupos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(255))

class Curso(db.Model):
    __tablename__ = 'cursos'
    course_key = db.Column(db.String(10), primary_key=True)
    course_name = db.Column(db.String(100), nullable=False)
    robotics_kit = db.Column(db.String(100), db.ForeignKey('kits_robotica.nombre'))
    caratula = db.Column(db.String(255))
    contenido = db.Column(db.Text)

class KitRobotica(db.Model):
    __tablename__ = 'kits_robotica'
    nombre = db.Column(db.String(100), primary_key=True)
    descripcion = db.Column(db.String(255))
    disponibilidad = db.Column(db.String(100))
