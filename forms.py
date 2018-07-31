from flask_wtf import Form 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
  prenom = StringField('Prenom', validators=[DataRequired("Entrez votre prenom s'il vous plait.")])
  nom = StringField('Nom', validators=[DataRequired("Entrez votre nom s'il vous plait.")])
  email = StringField('Adress Courriel', validators=[DataRequired("Entrez votre adresse courriel s'il vous plait."), Email("Entrez votre adresse courriel s'il vous plait.")])
  mot_de_passe = PasswordField('Mot de Passe', validators=[DataRequired("Entrez votre un mot de passe s'il vous plait."), Length(min=6, message="Les mots de passe doivent comporter 6 caracteres ou plus.")])
  submit = SubmitField('Creer un compte')

class LoginForm(Form):
  email = StringField('Email', validators=[DataRequired("Entrez votre adresse courriel s'il vous plait."), Email("Entrez votre adresse courriel s'il vous plait.")])
  mot_de_passe = PasswordField('Mot de Passe', validators=[DataRequired("Entrez votre un mot de passe s'il vous plait.")])
  submit = SubmitField("Se connecter")

class AddressForm(Form):
  address = StringField('Address', validators=[DataRequired("Entrez une adress s'il vous plait.")])
  submit = SubmitField("Chercher")