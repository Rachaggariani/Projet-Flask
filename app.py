from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bootstrap import Bootstrap
from models.forms import UserForm
import pymysql

# Installer pymysql en tant que MySQLdb
pymysql.install_as_MySQLdb()

# Génère une clé secrète aléatoire
secret_key = os.urandom(24)

# Initialiser l'application Flask
app = Flask(__name__)
Bootstrap(app)

# Configuration de la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/testapplicationone'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = secret_key

# Initialiser SQLAlchemy
db = SQLAlchemy(app)

# Modèle User
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(200))

@app.route('/', methods=['GET', 'POST'])
def home():
    form = UserForm()
    try:
        if form.validate_on_submit():
            username = form.username.data
            
            # Vérifiez l'existence de l'utilisateur dans la base de données
            user = User.query.filter_by(username=username).first()
            if user:
                flash('Utilisateur existe déjà.', 'warning')
            else:
                # Ajoutez l'utilisateur à la base de données
                new_user = User(
                    username=form.username.data,
                    email=form.email.data,
                    password=form.password.data  # Pensez à hacher le mot de passe avant l'insertion
                )
                db.session.add(new_user)
                db.session.commit()
                flash('Utilisateur inséré correctement.', 'success')
    except Exception as e:
        flash(f'Échec de l\'opération: {str(e)}', 'danger')

    return render_template('index_bd01.html', form=form)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crée toutes les tables définies dans le modèle
    app.run(debug=True, port=5002)
