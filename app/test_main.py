from pprint import pprint

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

input_text = """This is a sample @@text. It is 99used for   testing text processing.
Testing is a good idea and always important part of software development.
Testing ensures that the software is working correctly.

Software testing is the act of examining the artifacts and the
behavior of the software under test by validation and verification.
Software testing can also provide an objective, independent view of the
software to allow the business to appreciate and understand the
risks of software implementation."""


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_create_document():
    request_json = {"text": "example_text"}
    response = client.post("/documents/", json=request_json)
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


def test_read_document():
    request_json = {"text": "example_text"}
    post_resp = client.post("/documents/", json=request_json)
    resp_json = post_resp.json()
    document_id = resp_json["id"]
    get_resp = client.get(f"/documents/{document_id}")
    assert get_resp.status_code == 200
    assert resp_json == {"id": document_id, "text": "example_text"}


def test_get_document_summary():
    request_json = {"text": input_text}
    post_resp = client.post("/documents/", json=request_json)
    resp_json = post_resp.json()
    document_id = resp_json["id"]
    get_resp = client.get(f"/documents/{document_id}/summary/")
    resp_dict = get_resp.json()
    print(resp_dict["summary"])
    assert get_resp.status_code == 200
    summary = (
        "Software testing can also provide an objective, independent view of the\n"
        "software to allow the business to appreciate and understand the\n"
        "risks of software implementation. Software testing is the act of "
        "examining the artifacts and the\n"
        "behavior of the software under test by validation and verification. "
        "Testing is a good idea and always important part of software development."
    )
    # Assert summary of 3 sentences are returned
    assert resp_dict["summary"] == summary
    assert len(resp_dict["summary"].strip(".").split(".")) == 3
