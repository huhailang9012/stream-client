import os
from datetime import datetime

dest = 'E:/TV/'

def download(url: str) :
    """:param video
       ffmpeg -i 3.mp4 -vn -y -acodec copy 3.aac
       ffmpeg -i 2018.mp4 -codec copy -bsf: h264_mp4toannexb -f h264 tmp.264
       ffmpeg -i killer.mp4 -an -vcodec copy out.h264
    """
    # ffmpeg_cmd = 'ffmpeg -i {} -vn -y -acodec copy {}'
    ffmpeg_cmd = 'ffmpeg -i {} -t 15 -c copy {}'
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    cmd = ffmpeg_cmd.format(url, dest + now + '.flv')
    os.system(cmd)


if __name__ == '__main__':
    download('http://tx2play1.douyucdn.cn/live/7216674rMgLzYv2j.flv?uuid=')