import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Басты бетті тексеру тесті"""
    response = client.get('/')
    assert response.status_code == 200

def test_get_grades(client):
    """Студенттер тізімін алу тесті"""
    response = client.get('/api/grades')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'success'
    assert len(data['students']) >= 2

def test_add_grade(client):
    """Жаңа студент бағасын қосу тесті"""
    payload = {"name": "Нұрлан", "subject": "DevOps", "grade": 92}
    response = client.post('/api/grades', json=payload)
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'Нұрлан'
    assert data['grade'] == 92
