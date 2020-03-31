FROM python:3.7-alpine
WORKDIR /etc/
COPY . .
RUN pip install -r requires.txt

ENTRYPOINT python ./web-app/app.py
