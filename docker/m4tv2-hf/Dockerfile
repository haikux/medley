FROM python:3.9-slim

WORKDIR /app

COPY app.py .
COPY voice.py .
COPY requirements.txt .

RUN apt-get -y update && apt-get -y install git && apt-get -y install vim
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]