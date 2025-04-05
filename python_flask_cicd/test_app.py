from app import app

def test_home():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert response.data == b"Hello World!"
    
def test_app():
    response = app.test_client().get("/app")
    assert response.status_code == 200
    assert response.data == b"This is app page!"
