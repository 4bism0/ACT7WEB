from config import app, db
from models import Usuario, Grupo, Curso, KitRobotica

with app.app_context():
    db.create_all()
    print("📂 Base de datos creada con éxito.")