from fastapi import FastAPI
from service import download

app = FastAPI()


@app.post("/live/video/download")
def live_video_download(live_id: str, live_source: str):
    download(live_id, live_source)
    return {"success": True, "code": 0, "msg": "ok"}