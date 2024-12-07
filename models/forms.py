
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,EmailField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    username = StringField('Nom d\'utilisateur', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    submit = SubmitField('Enregistrer')
