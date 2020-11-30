import os
from datetime import datetime
from ffmpy import FFmpeg
dest = 'E:/TV/'

def download(url: str) :
    name = datetime.now().strftime('%Y%m%d%H%M%S%f')
    ff = FFmpeg(
         inputs={url: None},
         outputs={
              'E:/TV/' + name + '.flv': '-loglevel quiet -t 10 -vcodec h264 -acodec aac -c:a copy'}
    )
    print(ff.cmd)
    ff.run()


if __name__ == '__main__':
    download('http://tx2play1.douyucdn.cn/live/7216674rMgLzYv2j.flv?uuid=')