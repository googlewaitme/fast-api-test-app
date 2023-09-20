from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root(name: str | None = None, message: str | None = None):
    if name is None:
        name = "empty"
    if message is None:
        message = "message"
    return f"<h2>Hello, {name}! {message}!</h2>"

