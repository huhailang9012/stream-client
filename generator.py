from ffmpy import FFmpeg
import threading
import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor


def download(url: str) :
    print('current thread', threading.current_thread().name)
    name = datetime.now().strftime('%Y%m%d%H%M%S%f')
    ff = FFmpeg(
         inputs={url: None},
         outputs={
              'E:/TV/' + name + '.flv': '-loglevel quiet -t 10 -vcodec h264 -acodec aac -c:a copy'}
    )
    print(ff.cmd)
    ff.run()
#
#
executor = ThreadPoolExecutor(max_workers=2)
n = 0
while True:
    n = n + 1
    executor.submit(download, ('http://tx2play1.douyucdn.cn/live/6448043r1vyShOLw.flv?uuid='))
    if n == 1:
        time.sleep(10)
    else:
        time.sleep(1)