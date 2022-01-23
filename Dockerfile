FROM python:3.8-slim-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /inno-doctor
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./inno-Doctor .
EXPOSE 8000
#COPY entrypoint.sh .
ADD entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod 777 /usr/local/bin/entrypoint.sh
CMD /usr/local/bin/entrypoint.sh