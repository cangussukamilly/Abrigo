from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class CadastraUsuarioForm(FlaskForm):
    username = StringField(
        'Nome:',
        validators=[DataRequired(), Length(min=2, max=80)]
    )
    datadenascimento = StringField(
        'Data de nascimento:',
        validators=[DataRequired(), Length(min=2, max=80)]
    )
    email = StringField(
        'E-mail:',
        validators=[DataRequired(), Email()]
    )
    repitaemail = StringField (
        'Repita E-mail:',
        validators=[DataRequired(), EqualTo(email)]
    )
    senha = PasswordField (
        'Senha:',
        validators=[DataRequired()]
    )
    repitasenha = PasswordField (
        'Repita a Senha:',
        validators=[DataRequired(), EqualTo(senha)]
    )
    botao = SubmitField('Cadastrar')
        
class LoginUsuarioForm(FlaskForm):
    email = StringField (
        'E-mail:',
        validators=[DataRequired(), Email()]
    )
    senha = PasswordField (
        'Senha:',
        validators=[DataRequired()]
    )
    botao = SubmitField('Fazer Login')

class AdocaoForm(FlaskForm):
    username = StringField(
        'Nome:',
        validators=[DataRequired(), Length(min=2, max=80)]
    )
    email = StringField(
        'E-mail:',
        validators=[DataRequired(), Email()]
        )
    datadenascimento = StringField(
        'Data de nascimento:',
        validators=[DataRequired(), Length(min=2, max=80)]
    )
    escrevaRelato = StringField(
        'Data de nascimento:',
        validators=[Length(min=2, max=1000)]
    )
