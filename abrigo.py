from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from forms import CadastraUsuarioForm, LoginUsuarioForm, DeixeSeuRelatorioForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///abrigo.db'
app.config['SECRET_KEY'] = 'd77a98b1c04bc37e50787352e80323e3'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    passaword = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    datadenascimento = db.Column(db.Date(), nullable =False)

class Visitante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    datadenascimento = db.Column(db.Date(), nullable =False)
    escrevaRelato = db.Column(db.String(1000))

def __repr__(self):
        return '<User %r>' % self.username
@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html')
@app.route('/login')
def login():
    form=LoginUsuarioForm()
    return render_template('pages/login.html', formulario=form)
@app.route('/Cadastre-se', methods=['GET', 'Post'])
def cadastro():

    form= CadastraUsuarioForm()

    return render_template('pages/Cadastre-se.html', formulario=form)
@app.route('/sobre')
def lute():
    return render_template('pages/sobre.html')
@app.route('/Trabalhoabrigodecaes')
def acompanhamento():
    form= DeixeSeuRelatorioForm()

    return render_template('pages/Trabalhoabrigodecaes.html', formulario=form)

if __name__ == '__main__':
    app.run(debug=True, port = 5555)




