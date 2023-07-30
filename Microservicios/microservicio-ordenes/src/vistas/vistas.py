from flask import request,abort,make_response
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity,get_jwt
from flask_restful import Resource
from sqlalchemy import desc,asc
from modelos import db, OrdeneslistSchema , Orden
import json
import time


blacklist_schema = OrdeneslistSchema()

class VistaOrdenes(Resource):
    def post(self):
        if request.json == None or not "u_id" in request.json or not "title" in request.json or not "quantity" in request.json  or not "price" in request.json :
            abort(400)
        else:
            u_id = request.json["u_id"]
            title = request.json["title"]
            quantity = request.json["quantity"]
            price = request.json["price"]
            if (not u_id or u_id.isspace()) or (not title or title.isspace()) or (not quantity or quantity.isspace()) or (not price or price.isspace() )  :
                abort(400)

            nueva_orden = Orden(u_id=u_id, title=title,  quantity=quantity, price=price)
            db.session.add(nueva_orden)
            db.session.commit()
            
        return {"estado": "OK","mensaje":"Orden creada correctamente" } , 201


class VistaObtenerOrdenes(Resource):
    def get(self,u_id):
        ordenes = Orden.query.filter(Orden.u_id == u_id).all()
        lista = []
        for orden in ordenes:
            a = {"o_id": orden.o_id, "u_id": orden.u_id, "title": orden.title, "quantity": orden.quantity, 
                "price": orden.price,"status":orden.status, "date": orden.date.strftime("%Y-%m-%d")} 
            lista.append(a)
        return lista, 200        

    
class VistaPing(Resource):
    def get(self):
        response = make_response("pong", 200)
        response.mimetype = "text/plain"
        return response