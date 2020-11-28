# coding=gbk
from concurrent.futures import ThreadPoolExecutor, as_completed
import os
from ffmpy import FFmpeg
import threading
import time
from datetime import datetime
dest = 'E:/TV/'
url = 'http://tx2play1.douyucdn.cn/live/2045445r9wqXizbz.flv?uuid='


def download(url: str) :
    print('current thread', threading.current_thread().name)
    ffmpeg_cmd = 'ffmpeg -loglevel quiet -i  {} -t 5 -s 1280x720 -c:a copy {}'
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    cmd = ffmpeg_cmd.format(url, dest + now + '.flv')
    os.system(cmd)
    return dest + now + '.flv'


def info():
    ffmpeg_cmd = 'ffmpeg -i http://tx2play1.douyucdn.cn/live/2045445r9wqXizbz.flv?uuid='
    print(ffmpeg_cmd)
    os.system(ffmpeg_cmd)

if __name__ == '__main__':
    # executor = ThreadPoolExecutor(max_workers=1)
    # while True:
    #     executor.submit(download, (url))
    #     time.sleep(2)
    info()

