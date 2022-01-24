FROM python:3.8-slim-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /inno-doctor
COPY requirements.txt .
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY ./inno-Doctor .
EXPOSE 8000
CMD ./entrypoint.sh .
