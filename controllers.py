from flask import Flask, request, jsonify
from models import db, Usuario, Curso, Grupo, KitRobotica

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///escuela_robotica.db'
db.init_app(app)

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([{"id": u.id, "nombre": u.nombre, "rol": u.rol} for u in usuarios])

@app.route('/usuarios', methods=['POST'])
def add_usuario():
    data = request.json
    nuevo_usuario = Usuario(
        nombre=data['nombre'], 
        apellido=data['apellido'], 
        email=data['email'], 
        password=data['password'], 
        rol=data['rol'], 
        grupo_id=data['grupo_id']
    )
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({"message": "Usuario agregado correctamente"}), 201

if __name__ == '__main__':
    app.run(debug=True)