from fastapi.testclient import TestClient
from main import app
client=TestClient(app)
def test_home_page():
    r=client.get('/'); assert r.status_code==200; assert 'EduGenie' in r.text
def test_static():
    assert client.get('/static/style.css').status_code==200
def test_health():
    r=client.get('/health'); assert r.status_code==200; assert r.json()['status']=='ok'
def test_empty_question():
    assert client.post('/qa',json={'text':''}).status_code==422
