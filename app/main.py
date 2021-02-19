from fastapi import FastAPI
from pydantic import BaseModel
import clean

app = FastAPI()


class Input(BaseModel):
    doc1: str
    doc2: str


@app.get("/")
def read_root():
    return ("Lets compare some texts!")


@app.post("/jaccard")
async def jaccard(doc1, doc2):
    clean_doc1 = clean.clean(doc1)
    clean_doc2 = clean.clean(doc2)
    score = 0.0
    def shingles(s): return set(s[i:i+3] for i in range(len(s)-2))

    def jaccard_distance(seta, setb): return len(
        seta & setb)/float(len(seta | setb))
    try:
        score = jaccard_distance(shingles(clean_doc1), shingles(clean_doc2))
    except ZeroDivisionError:
        print('ZeroDivisionError')

    return score
