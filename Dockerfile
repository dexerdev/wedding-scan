FROM python:3.9-slim-buster
WORKDIR /app
COPY . .
RUN apt-get update && apt-get install -y build-essential python3-dev default-libmysqlclient-dev gcc -y
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m pip install gunicorn

ARG ENV
ADD ${ENV} ./
EXPOSE 5000
ENTRYPOINT ["gunicorn","--log-level", "info", "--access-logfile", "-", "wsgi:app", "-w", "4", "--timeout", "600"]
