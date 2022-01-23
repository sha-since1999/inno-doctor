FROM python:3.8-slim-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /inno-doctor
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./inno-Doctor .
EXPOSE 8000
CMD ./entrypoint.sh .
