"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the navbar"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/page1">Github</a>' in response.data
    assert b'<a class="nav-link" href="/page2">Docker</a>' in response.data
    assert b'<a class="nav-link" href="/page3">Python/Flask</a>' in response.data
    assert b'<a class="nav-link" href="/page4">CI/CD</a>' in response.data

def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Index Page" in response.data

def test_request_page1(client):
    """This makes page1"""
    response = client.get("/page1")
    assert response.status_code == 200
    assert b"Git" in response.data

def test_request_page2(client):
    """This makes page2"""
    response = client.get("/page2")
    assert response.status_code == 200
    assert b"Docker and Dockerhub" in response.data

def test_request_page3(client):
    """This makes page3"""
    response = client.get("/page3")
    assert response.status_code == 200
    assert b"Python/Flask" in response.data

def test_request_page4(client):
    """This makes page5"""
    response = client.get("/page4")
    assert response.status_code == 200
    assert b"Continuous Development/Continuous Deployment" in response.data

def test_request_page_not_found(client):
    """This makes page not found"""
    response = client.get("/page5")
    assert response.status_code == 404