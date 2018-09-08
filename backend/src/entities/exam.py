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

class Orders(Base):
    __tablename__='orders'

    id = Column(Integer, primary_key=True)
    data = Column(DateTime)
    simbol = Column(String)
    side = Column(Integer)
    simbol_type = Column(String)
    piata = Column(String)
    internal_account = Column(Integer)
    volum = Column(Integer)
    pret = Column(Numeric)
    order_no = Column(Integer)
    tip_ordin = Column(String)
    trader = Column(String)
    def __init__(self, id, data, simbol, side, simbol_type, piata, internal_account, volum, pret, order_no, tip_ordin, trader):
        self.id = id
        self.data = data
        self.simbol = simbol
        self.side = side
        self.simbol_type = simbol_type
        self.piata = piata
        self.internal_account = internal_account
        self.volum = volum
        self.pret = pret
        self.order_no = order_no
        self.tip_ordin = tip_ordin
        self.trader = trader

class OrdersSchema(Schema):
    id = fields.Number()
    data = fields.DateTime()
    simbol = fields.Str()
    side = fields.Number()
    simbol = fields.Str()
    simbol_type = fields.Str()
    piata = fields.Str()
    internal_account = fields.Number()
    volum = fields.Number()
    pret = fields.Decimal()
    order_no = fields.Number()
    tip_ordin = fields.Number()
    trader = fields.Str()
    