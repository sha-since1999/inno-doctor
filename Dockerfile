FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED=1
#RUN mkdir inno-doctor
WORKDIR /inno-doctor
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./inno-Doctor .
#EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000