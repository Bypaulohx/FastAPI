from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType

# cria a conexão com o banco de dados SQLite
db = create_engine("sqlite:///banco.db")

# cria a base de dados
Base = declarative_base()

# cria as classes/tabelas do banco de dados
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String, nullable=False)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean, default=False)

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

# Pedido
class Pedido(Base):
    __tablename__ = "pedidos"

    # STATUS_PEDIDOS = (
    #     ("pendente", "Pendente"),
    #     ("cancelado", "Cancelado"),
    #     ("finalizado", "Finalizado")
    # )

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String)
    usuario = Column("usuario", ForeignKey("usuarios.id"))
    preco = Column("preco", Float)

    def __init__(self, usuario, status="pendente", preco=0):
        self.status = status
        self.preco = preco
        self.usuario = usuario

# Item do pedido
class ItemPedido(Base):
    __tablename__ = "itens_pedido"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    tamanho = Column("tamanho", String)
    sabor = Column("sabor", String)
    quantidade = Column("quantidade", Integer)
    preco_unitario = Column("preco_unitario", Float)
    pedido = Column("pedido", ForeignKey("pedidos.id"))

    def __init__(self, pedido, tamanho, sabor, quantidade, preco_unitario):
        self.pedido = pedido
        self.tamanho = tamanho
        self.sabor = sabor
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        self.pedido = pedido
# executa a criação dos metadados no banco de dados