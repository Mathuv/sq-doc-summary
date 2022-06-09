from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_create_document():
    request_json = {"text": "example_text"}
    response = client.post(
        "/documents/", json=request_json
    )
    assert response.status_code == 200
    resp_dict = response.json()
    resp_dict.pop("id")
    assert resp_dict == request_json


def test_read_documents():
    request_json = {"text": "example_text"}
    post_resp = client.post("/documents/", json=request_json)
    get_resp = client.get("/documents/")
    assert get_resp.status_code == 200
    resp_dict = get_resp.json()
    assert post_resp.json() in resp_dict
