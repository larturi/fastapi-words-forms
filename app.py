import ssl
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from word_forms.word_forms import get_word_forms

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:32000",
    "http://apirest.com.ar:8900",
    "https://next-words-form.vercel.app"
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/random_word_family/{word}")
async def random_word_family(word: str):
    word_forms = get_word_forms(word)
    return {"word": word, "word_forms": word_forms}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
