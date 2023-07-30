import json
import responses
from flask import request
from faker import Faker
from datetime import datetime ,timedelta

fake = Faker()

def test_creacion_orden_sin_parametros(app, client):
    res = client.post('/orden')
    assert res.status_code == 400

def test_creacion_orden_parametro_vacio(app, client):
    res = client.post('/orden', headers={"Authorization": "Bearer {}".format("ghyjuilk")},json={"u_id": "1", "title": "", "quantity":"1","price":"100"})
    assert res.status_code == 400

def test_creacion_orden_correcta(app, client):
    res = client.post('/orden', headers={"Authorization": "Bearer {}".format("ghyjuilk")},json={"u_id": "1", "title": "TEST", "quantity":"1","price":"100"})
    assert res.status_code == 201

def test_consulta_orden(app, client):
    res = client.get('/orden/1')
    assert res.status_code == 200

def test_ping(app,client):
    res = client.get('/orden/ping')
    assert res.status_code == 200
    expected = "pong"
    response =  expected in res.get_data(as_text=True)
    assert  response == True
    