import time
from database.repository import storage
from downloader import download


def download(live_id: str, live_source: str):
    stage = 0
    duration = 60
    while stage < 10:
        name, local_video_path = download(live_source, str(duration))
        storage(name, live_id, live_source, local_video_path, duration, stage)
        stage += 1
        time.sleep(5)