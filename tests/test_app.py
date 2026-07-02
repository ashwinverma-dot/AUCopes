from app.main import app


def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"College Information Portal" in response.data
    assert b"CI/CD Pipeline" in response.data


def test_academics_page():
    client = app.test_client()
    response = client.get("/academics")
    assert response.status_code == 200
    assert b"Departments and Courses" in response.data
    assert b"Computer Science and Engineering" in response.data
    assert b"B.Tech" in response.data


def test_faculty_contact_page():
    client = app.test_client()
    response = client.get("/faculty-contact")
    assert response.status_code == 200
    assert b"Faculty Details and Contact" in response.data
    assert b"Faculty Members" in response.data


def test_faculty_contact_form_post():
    client = app.test_client()
    response = client.post("/faculty-contact", data={
        "name": "Test User",
        "email": "test@example.com",
        "message": "Please share admission details."
    })
    assert response.status_code == 200
    assert b"enquiry has been submitted successfully" in response.data


def test_health_route():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["health"] == "ok"


def test_college_api():
    client = app.test_client()
    response = client.get("/api/college")
    assert response.status_code == 200
    data = response.get_json()
    assert data["project_title"] == "Cloud-Based College Information Portal with CI/CD Pipeline"
    assert "Python Flask" in data["technology_stack"]
