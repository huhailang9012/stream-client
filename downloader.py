import time
from datetime import timedelta, datetime
import random

from ffmpy import FFmpeg
import threading
dest = 'E:/TV/'


def cult_video(video_path: str, video_name: str, long: int):
    tm_sum = 0
    mytime = datetime(2020, 1, 1, 0, 0, 0)
    stime = str(mytime.time())
    i = 1
    while tm_sum < long:
        cut = FFmpeg(
            executable='D:/ffmpeg/bin/ffmpeg.exe',
            inputs={video_path: None},
            outputs={
                'E:/TV/' + video_name + '_' + str(i) + '.flv': '-loglevel quiet -ss ' + stime + ' -t 00:00:30  -c:a copy'}
        )
        print(cut.cmd)
        cut.run()
        tm_sum += 30
        mytime += timedelta(seconds=30)
        stime = str(mytime.time())
        i += 1
    pass


def download(url: str):
    ra = random.randint(1, 100000)
    name = datetime.now().strftime('%Y%m%d%H%M%S%f') + str(ra)
    video_path = dest + name + '.flv'
    long = '60'
    ff = FFmpeg(
        executable='D:/ffmpeg/bin/ffmpeg.exe',
        inputs={url: None},
        outputs={
            'E:/TV/' + name + '.flv': '-loglevel quiet -t ' + long + ' -vcodec h264 -acodec aac -c:a copy'}
    )
    print(ff.cmd)
    ff.run()
    cult_video(video_path, name, int(long))


if __name__ == '__main__':
    # download('https://txdirect.hls.huya.com/huyalive/1199561494589-1199561494589-5435792235671060480-2399123112634'
    #          '-10057-A-0-1_2000.m3u8?wsSecret=117af05487266aded1dc0fffaf1a6788&wsTime=5fddcb3a&u=0&seqid'
    #          '=16082846033138140&ctype=tars_mobile&txyp=o%3Ad3%3B&fs=bgct&t=103')
    # cult_video("E:/TV/20201202112750661184.flv", 600)
    t1 = threading.Thread(target=download, args=("https://migu-bd.hls.huya.com/huyalive/1199560103015-1199560103015"
                                                 "-5429815470851096576-2399120329486-10057-A-0-1_2000.m3u8?wsSecret"
                                                 "=8371841ebab1aac87bca5aac8dd1d855&wsTime=5fddd3b7&u=0&seqid"
                                                 "=16082867763021678&ctype=tars_mobile&txyp=o%3Aq6%3B&fs=bgct&t=103",))
    t2 = threading.Thread(target=download, args=("https://txdirect.hls.huya.com/src/2178953218-2178953218"
                                                 "-9358532810823958528-4358029892-10057-A-0-1_2000.m3u8?wsSecret"
                                                 "=09aafa01337da509f4682fe9e80f588d&wsTime=5fddd5cc&u=0&seqid"
                                                 "=16082873169751186&ctype=tars_mobile&txyp=o%3Awx6%3B&fs=bgct"
                                                 "&&sphdcdn=al_7-tx_3-js_3-ws_7-bd_2-hw_2&sphdDC=huya&sphd=264_*-265_*&t=103",))
    while 1:
        t1.start()
        t2.start()
        time.sleep(60)

    pass


