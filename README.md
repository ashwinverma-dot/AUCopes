# Cloud-Based College Information Portal with CI/CD Pipeline

This project is a simple cloud-based college website developed using Flask. It displays basic college information, departments, courses, faculty details, and a contact enquiry form. The project also includes testing, Docker support, and a GitHub Actions CI/CD pipeline.

## Project Title

Cloud-Based College Information Portal with CI/CD Pipeline

## Project Objective

The objective of this project is to design and deploy a simple college information website using a cloud-ready architecture. The project demonstrates web application development, automated testing, containerization, and CI/CD-based deployment.

## Main Pages

| Page | URL | Description |
|---|---|---|
| Home | `/` | College introduction, vision, mission, and CI/CD pipeline overview |
| Departments and Courses | `/academics` | List of departments and courses offered |
| Faculty and Contact | `/faculty-contact` | Faculty details and enquiry form |

## Additional Endpoints

| Endpoint | Description |
|---|---|
| `/health` | Health check endpoint for testing and deployment monitoring |
| `/api/college` | Returns project details in JSON format |

## Technology Stack

| Component | Technology |
|---|---|
| Backend | Python Flask |
| Frontend | HTML, CSS |
| Testing | Pytest |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Cloud Deployment | Render or any Docker-supported cloud platform |

## Project Structure

```text
college-info-portal-cicd/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── academics.html
│   │   └── faculty_contact.html
│   └── static/
│       └── css/
│           └── style.css
├── tests/
│   └── test_app.py
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── Dockerfile
├── .dockerignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## Run on Windows

Open Command Prompt or PowerShell inside the project folder.

### 1. Create virtual environment

```bash
python -m venv venv
```

### 2. Activate virtual environment

```bash
.\venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the project

```bash
python app\main.py
```

Open the browser:

```text
http://localhost:5000
```

## Run Tests

```bash
python -m pytest
```

Expected output:

```text
6 passed
```

## Run with Docker

```bash
docker build -t college-info-portal-cicd .
docker run -p 5000:5000 college-info-portal-cicd
```

Open:

```text
http://localhost:5000
```

## CI/CD Pipeline

The GitHub Actions pipeline performs the following tasks:

```text
Developer pushes code to GitHub
        ↓
GitHub Actions starts
        ↓
Python dependencies are installed
        ↓
Unit tests are executed
        ↓
Docker image is built
        ↓
Cloud deployment is triggered
```

## GitHub Actions Workflow

The workflow file is available at:

```text
.github/workflows/ci-cd.yml
```

It runs automatically when code is pushed to the `main` branch.

## Deployment on Render

1. Create a new Web Service on Render.
2. Connect your GitHub repository.
3. Select Docker as the runtime environment.
4. Use the `main` branch.
5. Copy the Render Deploy Hook URL.
6. Add it to GitHub repository secrets using this name:

```text
RENDER_DEPLOY_HOOK_URL
```

7. Push code to GitHub.
8. GitHub Actions will test, build, and trigger cloud deployment.

## Presentation Explanation

This project is a cloud-based college information portal developed using Python Flask. It provides three main pages: Home, Departments and Courses, and Faculty and Contact. The application displays department information, course details, sample faculty profiles, and a basic enquiry form. The project is tested using Pytest and containerized using Docker. A CI/CD pipeline is configured using GitHub Actions, which automatically runs tests, builds the Docker image, and triggers deployment to the cloud when code is pushed to the main branch.

## Note

The college address, contact details, and faculty information used in this project are sample values. They can be replaced with actual official college information before final submission or deployment.
