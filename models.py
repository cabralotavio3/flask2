from database import db

class Usuario(db.Model):
    __tablename__= "usuario"
    id = db.Column(db.Integer, primary_key=True)
    nome= db.Column(db.String(100))
    email = db.Column(db.String(100))
    senha= db.Column(db.String(100))

    def __init__(self, nome, email,senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def __repr__(self):
        return"<Usuario{}>".format(self.nome)
    

class Cha(db.Model):
    __tablename__= "cha"
    id = db.Column(db.Integer, primary_key=True)
    sabor= db.Column(db.String(100))
    ingredientes = db.Column(db.String(100))
    preco= db.Column(db.Float)

    def __init__(self, sabor, ingredientes,preco):
        self.sabor = sabor
        self.ingredientes = ingredientes
        self.preco = preco

    def __repr__(self):
        return"<Cha{}>".format(self.cha)
    
class Pedido(db.Model):
    __tablename__= "pedido"
    id = db.Column(db.Integer, primary_key=True)
    usuario_id= db.Column(db.Integer, db.ForeignKey('usuario.id'))
    cha_id = db.Column(db.Integer, db.ForeignKey('cha.id'))
    data = db.Column(db.Date)
    usuario = db.relationship('Usuario', foreign_keys=usuario_id)
    cha = db.relationship('Cha', foreign_keys=cha_id)

    def __init__(self, usuario_id, cha_id, data):
        self.usuario_id = usuario_id
        self.cha_id = cha_id
        self.data = data

    def __repr__(self):
        return"<Pedido {} - {} - {}>".format(self.usuario.nome, self.cha.sabor, self.data)
    

    