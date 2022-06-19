FROM python:latest

COPY bin/ /app

WORKDIR /app

CMD ["python", "-m", "unittest", "test_main.py", "-v"]
