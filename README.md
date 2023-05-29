# Word forms API

## Local

```bash

pipenv shell

pipenv install

uvicorn app:app 
    --host 0.0.0.0 
    --port 8900 
    --ssl-keyfile="certs/cert.key" 
    --ssl-certfile="certs/cert.crt"
```

#### Example: <https://0.0.0.0:8900/random_word_family/love>

## Production

```bash
    docker build -t larturi/wordsform-fastapi:latest .
    docker push larturi/wordsform-fastapi:latest
    docker run -p 8900:8900 --name wordsform-fastapi larturi/wordsform-fastapi
```
