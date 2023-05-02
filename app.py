from fastapi import FastAPI
from word_forms.word_forms import get_word_forms

app = FastAPI()

@app.get("/random_word_family/{word}")
async def random_word_family(word: str):
    word_forms = get_word_forms(word)
    return {"word": word, "word_forms": word_forms}
