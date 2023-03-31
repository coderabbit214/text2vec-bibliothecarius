import uvicorn
from fastapi import FastAPI, Request
import json
from text2vec import SentenceModel

app = FastAPI()


@app.post("/vector")
async def vector(request: Request):
    global model
    json_post_raw = await request.json()
    json_post = json.dumps(json_post_raw)
    json_post_list = json.loads(json_post)
    embeddings = model.encode(json_post_list.get('input'))
    return embeddings.tolist()


if __name__ == '__main__':
    model = SentenceModel('text2vec-base-chinese')
    uvicorn.run(app, host='0.0.0.0', port=8001, workers=1)
