from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/health")
def health(request: Request):
    return {"status": "ok", "host": request.client.host}
