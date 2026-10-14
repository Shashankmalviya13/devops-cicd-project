# Python DevOps CI Project

A Python web application demonstrating DevOps fundamentals.

## Technologies
- Python 3.12
- Git and GitHub
- GitHub Actions
- Docker
- Python unittest

## Features
- Python web application
- Health-check endpoint at `/health`
- Automated unit tests
- Docker containerization
- CI pipeline using GitHub Actions

## Run Locally

```bash
python app.py
```

Open: http://localhost:8000

## Run Tests

```bash
python -m unittest -v test_app.py
```

## Build Docker Image

```bash
docker build -t devops-python-app .
```

## CI Pipeline

GitHub Actions runs automated tests and builds the Docker image on pushes and pull requests.

Workflow: `.github/workflows/ci.yml`

## Author
Shashank Malviya

GitHub: https://github.com/Shashankmalviya13
