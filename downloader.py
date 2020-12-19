from datetime import datetime
import time
from ffmpy import FFmpeg
from database.repository import storage, select_by_id

# dest_dir = "/data/files/live_videos/"
dest_dir = "E:/TV/"
long = '20'


def cut_video(video_id: str):
    """
    cut video
    :param: video
    :return:
    """
    tm_sum = 0
    video = select_by_id(video_id)
    segment = video['segment']
    duration = video['duration']
    video_path = video['local_video_path']
    if not segment:
        while tm_sum < duration:
            stime = str(tm_sum)
            video_name = datetime.now().strftime('%Y%m%d%H%M%S%f')
            cut = FFmpeg(
                inputs={video_path: None},
                outputs={
                    'E:/TV/' + video_name + '.flv': '-loglevel quiet -ss ' + stime + ' -t ' + long + '  -c:a copy'}
            )
            print(cut.cmd)
            cut.run()
            tm_sum += 20
    pass


def download(url: str, duration: str):
    """
    download video
    :param: url
    :param: duration
    :return:
    """
    name = datetime.now().strftime('%Y%m%d%H%M%S%f')[:-3]
    ff = FFmpeg(
        inputs={url: None},
        outputs={
            'E:/TV/' + name + '.flv': '-loglevel quiet -t ' + duration + ' -vcodec h264 -acodec aac -c:a copy'}
    )
    print(ff.cmd)
    ff.run()
    return name + '.flv', dest_dir + name + '.flv'


if __name__ == '__main__':
    stage = 0
    duration = 120
    real_url = 'http://tx2play1.douyucdn.cn/live/8239885rsu5f6SO3.flv?uuid='
    while stage < 5:
        name, local_video_path = download(real_url, str(duration))
        id = storage(name, '1', local_video_path, duration, stage)
        cut_video(id)
        stage += 1
        time.sleep(5)