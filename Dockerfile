FROM python:3.11-slim-buster

WORKDIR /app

COPY app.py app.py
COPY perceptron.pkl perceptron.pkl
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

ENV FLASK_APP=app

EXPOSE 5000

CMD ["python", "app.py", "flask", "run", "--host", "0.0.0.0", "--port", "5000"]
