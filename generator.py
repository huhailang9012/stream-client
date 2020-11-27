# coding=gbk
from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import threading
import time
from datetime import datetime
dest = 'E:/TV/'
url = 'http://tx2play1.douyucdn.cn/live/9184179rc5x8Hm04.flv?uuid='
def download(url: str) :
    print('current thread', threading.current_thread().name)
    ffmpeg_cmd = 'ffmpeg -loglevel quiet -i {} -t 5 -s 1920x1080 -c:a copy {}'
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    cmd = ffmpeg_cmd.format(url, dest + now + '.flv')
    os.system(cmd)
    return dest + now + '.flv'


executor = ThreadPoolExecutor(max_workers=5)
while True:
    executor.submit(download, (url))
    time.sleep(2)

# for i in range(5):
#     task = executor.submit(download, (url))
#
#     tasks.append(task)
#     time.sleep(1)y

# for future in as_completed(tasks):
#     data = future.result()
#     print("in main: storage {} success".format(data))

# 执行结果
# get page 2s finished
# in main: get page 2s success
# get page 3s finished
# in main: get page 3s success
# get page 4s finished
# in main: get page 4s success