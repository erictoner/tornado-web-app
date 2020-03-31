# Tornado Web App
Simple Tornado Web App that responds to a few basic HTTP requests

# Setup
```shell
docker-compose up -d
```

# Usage
```shell
# Return basic mesages
curl -i 127.0.0.1:8000/
curl -i 127.0.0.1:8000/request

# Return a static index.html webpage
curl -i 127.0.0.1:8000/resume
```
