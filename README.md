# Word forms API

## Local

```bash

pyenv shell 3.7.10

pipenv shell

pipenv install

uvicorn app:app --host 0.0.0.0 --port 8900

```

#### Example: <https://0.0.0.0:8900/random_word_family/love>

## Production

```bash
    docker build -t larturi/wordsform-fastapi:latest .
    docker push larturi/wordsform-fastapi:latest
    docker run -p 8900:8900 --name wordsform-fastapi larturi/wordsform-fastapi
```
