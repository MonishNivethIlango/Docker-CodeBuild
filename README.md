# FastAPI Sample Application

This is a sample FastAPI application with 4 endpoints, unit tests, Docker support, and CI/CD integration for AWS and Docker Hub.

## Features
- 4 sample FastAPI endpoints
- Unit tests with pytest (including passing and failing cases)
- Test coverage enforced at 90%+
- Dockerfile for containerization
- AWS CodeBuild/CodePipeline ready (buildspec.yml)
- Test and coverage artifacts uploaded to S3

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the app:
   ```bash
   uvicorn app.main:app --reload
   ```
3. Run tests with coverage:
   ```bash
   pytest --cov=app --cov-report=term-missing
   ```

## Docker
Build and run the Docker image:
```bash
# Build
 docker build -t fastapi-sample .
# Run
 docker run -p 8000:8000 fastapi-sample
```

## CI/CD
- Uses AWS CodeBuild and CodePipeline
- Only builds and deploys if tests pass and coverage is >= 90%
- Artifacts (test/coverage logs) are uploaded to S3

## GitHub & AWS Integration
- Push code to your GitHub repo
- Connect repo to AWS CodeBuild/CodePipeline for automated builds and deployments

---

Replace placeholders and secrets before production use.
