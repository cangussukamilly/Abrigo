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
    bairro = StringField(
        'Bairro:',
        validators=[DataRequired(), Length(min=2, max=80)]
    )

    cidade = StringField(
        'Cidade:',
        validators=[DataRequired(), Length(min=2, max=80)]
    )
    estado = StringField(
        'Estado:',
        validators=[DataRequired(), Length(min=2, max=80)]
    )

    email = StringField(
        'E-mail:',
        validators=[DataRequired(), Email()]
        )

    confirmeseuemail= StringField(
        'Confirme seu E-mail:',
        validators=[DataRequired(), Length(min=2, max=80)]
    )

    ddd = StringField(
        'DDD:',
        validators=[DataRequired(), Length(min=2, max=80)]
    )
    telefone = StringField(
        'Telefone:',
        validators=[DataRequired(), Length(min=2, max=80)]
    )
    porquevocequeradotarumcao = StringField(
        'Porque você quer adotar um cachorro?',
        validators=[Length(min=2, max=1000)]
    )

    botao = SubmitField('Enviar')