
from datetime import timedelta, datetime
from datetime import datetime,time
from ffmpy import FFmpeg





# start_time = datetime(2020, 1, 1, 0, 0, 0) + timedelta(seconds=3600)
# print(start_time.time())

def cult_video(video_path: str, long: int):
    tm_sum = 0
    mytime = datetime(2020, 1, 1, 0, 0, 0)
    stime = str(mytime.time())
    i = 1
    while tm_sum < long:
        cut = FFmpeg(
            inputs={video_path: None},
            outputs={
                'E:/TV/' + str(i) + '.flv': '-loglevel quiet -ss ' + stime + ' -t 00:00:30  -c:a copy'}
        )
        print(cut.cmd)
        cut.run()
        tm_sum += 30
        mytime += timedelta(seconds=30)
        stime = str(mytime.time())
        i += 1
    pass

if __name__ == '__main__':
    # download('http://tx2play1.douyucdn.cn/live/258718rhHNF097ui.flv?uuid=')
    cult_video("E:/TV/20201202112750661184.flv", 600)

    pass

