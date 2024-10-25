from flask import Flask, render_template, request, flash, redirect
from database import dp
from models import Usuario

bp_usuario = Blueprint('usuarios', __name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add')
def usuario_add():
    u = Usuario.query.all()
    return render_template('usuario_add.html')

@app.route('/usuario/save', methods=['POST'])
def usuario_save():
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    if nome and email and senha:
        objeto = Usuario(nome, email, senha)
        db.session.add(objeto)
        db.session.commit()
        flash('usuario cadastrado com sucesso fera!!')
        return redirect('/')
    else:
        flash('preencha todos os campos zeca')
        return redirect('/add')

