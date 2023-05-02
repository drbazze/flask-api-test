import pytest

def test_status_endpoint_status_code(test_client):
    response = test_client.get("/status")

    assert response.status_code == 200

def test_status_endpoint_response(test_client):
    response = test_client.get("/status")

    assert b"live" in response.data

def test_status_endpoint_not_accepting_post_method(test_client):
    response = test_client.post("/status")

    assert response.status_code == 405

def test_root_endpoint_status_code(test_client):
    response = test_client.get("/")

    assert response.status_code == 200

def test_root_endpoint_response(test_client):
    response = test_client.get("/")

    assert b"ok" in response.data

def test_root_endpoint_not_accepting_post_method(test_client):
    response = test_client.post("/")

    assert response.status_code == 405