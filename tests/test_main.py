def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_hello_endpoint(client):
    response = client.get("/hello?name=ChatGPT")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, ChatGPT!"}
