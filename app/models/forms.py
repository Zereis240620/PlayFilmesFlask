from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired


class LoginForm(FlaskForm):
	login    = StringField("login", validators=[DataRequired()])
	password = PasswordField("password", validators=[DataRequired()])

class FilmeForm(FlaskForm):
    id 			= IntegerField("id")
    nome 		= StringField("nome", validators=[DataRequired()])
    duracao		= StringField("duracao", validators=[DataRequired()])
    ano			= IntegerField("ano", validators=[DataRequired()])
    url			= StringField("url", validators=[DataRequired()])
    resumo      = StringField('resumo',validators=[DataRequired()])
    id_user_cad = IntegerField("id_user_cad", validators=[DataRequired()])
    id_category = SelectField("id_category",choices=[(1, 'Desenho'), (2, 'Comédia')] , validators=[DataRequired()])

    capa = FileField('capa', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])