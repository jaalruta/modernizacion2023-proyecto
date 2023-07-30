import pytest
import responses
from application import application as flask_app

@pytest.fixture(scope='session')
def app():
    yield flask_app
    
@pytest.fixture(scope='session')
def client(app):
    responses.start()

    app.config['TESTING'] = True
    client = app.test_client() 
    yield client
    responses.stop()