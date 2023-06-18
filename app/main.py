from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, StreamingResponse

from recognition.reco import Rozpoznawanie

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")


cam = Rozpoznawanie()

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", context={"request": request})


@app.get("/video", response_class=HTMLResponse)
async def video():
    return  StreamingResponse(cam.stream(),
                    media_type='multipart/x-mixed-replace; boundary=frame')
