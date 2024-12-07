from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

# Installer pymysql en tant que MySQLdb
pymysql.install_as_MySQLdb()

app = Flask(__name__)

# Configuration de la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/testapplicationone'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Désactiver les notifications de modification SQLAlchemy
db = SQLAlchemy(app)

# Créer un contexte de l'application pour SQLAlchemy
app.app_context().push()

# Modèle User
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(200))

# Route principale
@app.route('/')
def home():
    new_user = User(username='xx', email='xx@gmail.com', password='p1')
    try:
        # Vérifier si l'utilisateur ou l'email ou le mot de passe existe déjà
        existing_user = User.query.filter(
            (User.username == new_user.username) |
            (User.email == new_user.email) |
            (User.password == new_user.password)
        ).first()

        if existing_user:
            if existing_user.username == new_user.username:
                return f"L'utilisateur existe déjà: {new_user.username}"
            if existing_user.email == new_user.email:
                return f"L'email existe déjà: {new_user.email}"
            if existing_user.password == new_user.password:
                return f"Le mot de passe existe déjà: {new_user.password}"
        else:
            # Ajouter l'utilisateur s'il n'existe pas
            db.session.add(new_user)
            db.session.commit()
            return "L'utilisateur a été ajouté avec succès"
    except Exception as e:
        return str(e)

    return 'Exécution réussie'

if __name__ == '__main__':
    app.run(debug=True, port=5001)
