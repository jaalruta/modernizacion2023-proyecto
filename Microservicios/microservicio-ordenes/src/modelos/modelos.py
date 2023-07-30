from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy.sql import func

db = SQLAlchemy()

class Orden(db.Model):
    o_id = db.Column(db.Integer, primary_key=True)
    u_id  =db.Column(db.Integer)
    title  = db.Column(db.String(1000))
    quantity  = db.Column(db.Integer)
    price  = db.Column(db.String(1000))
    status  = db.Column(db.String(1000))
    date  = db.Column(db.DateTime,server_default=func.now())



class OrdeneslistSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Orden
        include_relationships = True
        load_instance = True
