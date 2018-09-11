from sqlalchemy import Column, String, Integer, Numeric, DateTime
from marshmallow import Schema, fields
from .entity import Entity, Base, Entity2


class Exam(Entity, Base):
    __tablename__ = 'exams'

    title = Column(String)
    description = Column(String)

    def __init__(self, title, description, created_by):
        Entity.__init__(self, created_by)
        self.title = title
        self.description = description

class ExamSchema(Schema):
    id = fields.Number()
    title = fields.Str()
    description = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()

class Customer(Entity2, Base):
    __tablename__ = 'customers'
    
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)

    def __init__(self, firstname, lastname, age):
        Entity2.__init__(self)
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

class CustomerSchema(Schema):
    id = fields.Number()
    firstname = fields.Str()
    lastname = fields.Str()
    age = fields.Str()
    createdAt = fields.DateTime()
    updateAt = fields.DateTime()

class Test(Base):
    __tablename__="ordtest"
    nume = Column(String)
    tara = Column(String)
    id = Column(Integer, primary_key=True)
    def __init__(self, nume, tara, id):
        self.nume = nume
        self.tara = tara
        self.id = id

class TestSchema(Schema):
    nume = fields.Str()
    tara = fields.Str()
    id = fields.Integer()

class Orders(Base):
    __tablename__='ord7'

    id = Column(Integer, primary_key=True)
    status = Column(Integer)
    order_no = Column(Numeric)
    simbol = Column(String)
    simbol_type = Column(String)
    market = Column(String)
    ef_time = Column(DateTime)
    side = Column(Integer)
    price = Column(Numeric)
    volum = Column(Numeric)
    order_term = Column(Integer)
    ticket = Column(Numeric)
    update_type = Column(Integer)
    update_time = Column(DateTime)
    trader = Column(String)
    internal_account = Column(Numeric)
    cant_exec = Column(Numeric)
    order_status = Column(Integer)
    def __init__(self, status, order_no, simbol, simbol_type, market, ef_time, side, price, volum, order_term, ticket, update_type, update_time,trader, internal_account, cant_exec, order_status):
        self.status = status
        self.order_no = order_no
        self.simbol = simbol
        self.simbol_type = simbol_type
        self.market = market
        self.ef_time = ef_time
        self.side = side
        self.price = price
        self.volum = volum
        self.order_term = order_term
        self.ticket = ticket
        self.update_type = update_type
        self.update_time = update_time
        self.trader = trader
        self.internal_account = internal_account
        self.cant_exec = cant_exec
        self.order_status = order_status

class OrdersSchema(Schema):
    id = fields.Number()
    status = fields.Number()
    order_no = fields.Number()
    simbol = fields.Str()
    simbol_type = fields.Str()
    market =fields.Str()
    ef_time = fields.DateTime()
    side = fields.Number()
    price = fields.Number()
    volum = fields.Number()
    order_term = fields.Number()
    ticket = fields.Number()
    update_type = fields.Number()
    update_time = fields.DateTime()
    trader = fields.Str()
    internal_account = fields.Number()
    cant_exec = fields.Number()
    order_status = fields.Number()


# class Orders(Base):
#     # aici e tabela din postgres
#     __tablename__='orders7'

#     id = Column(Integer, primary_key=True)
#     data = Column(DateTime)
#     simbol = Column(String)
#     side = Column(Integer)
#     simbol_type = Column(String)
#     piata = Column(String)
#     internal_account = Column(Integer)
#     volum = Column(Integer)
#     pret = Column(Numeric)
#     order_no = Column(Integer)
#     tip_ordin = Column(String)
#     trader = Column(String)
#     def __init__(self, id, data, simbol, side, simbol_type, piata, internal_account, volum, pret, order_no, tip_ordin, trader):
#         self.id = id
#         self.data = data
#         self.simbol = simbol
#         self.side = side
#         self.simbol_type = simbol_type
#         self.piata = piata
#         self.internal_account = internal_account
#         self.volum = volum
#         self.pret = pret
#         self.order_no = order_no
#         self.tip_ordin = tip_ordin
#         self.trader = trader

# class OrdersSchema(Schema):
#     id = fields.Number()
#     data = fields.DateTime()
#     simbol = fields.Str()
#     side = fields.Number()
#     simbol = fields.Str()
#     simbol_type = fields.Str()
#     piata = fields.Str()
#     internal_account = fields.Number()
#     volum = fields.Number()
#     pret = fields.Decimal()
#     order_no = fields.Number()
#     tip_ordin = fields.Number()
#     trader = fields.Str()
