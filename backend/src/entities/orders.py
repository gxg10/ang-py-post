from sqlalchemy import Column, String, Integer, Numeric, DateTime
from marshmallow import Schema, fields
from .entity import Base

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