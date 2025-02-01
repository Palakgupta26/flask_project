from app import app

def test_home():
    reponse=app.test_client().get("/")

    assert response.status_code==200
    assert reponse.data ==b"Hello jolly"