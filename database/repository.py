import uuid

from database.database_pool import PostgreSql

def insert(id: str, name: str, live_id: str, local_video_path: str, duration: int,
           stage: int, segment: bool):
    sql = """INSERT INTO videos (id, name, live_id, local_video_path, duration, stage, segment) 
                     VALUES
                     (%(id)s, %(name)s, %(live_id)s, %(local_video_path)s, %(duration)s, %(stage)s, %(segment)s)"""
    params = {'id': id, 'name': name, 'live_id': live_id, 'local_video_path': local_video_path, 'duration': duration,
              'stage': stage, 'segment': segment}
    db = PostgreSql()
    db.execute(sql, params)


def storage(name: str, live_id: str, local_video_path: str, duration: int, stage: int) -> str:
    """
    storage videos
    :return:
    """
    id = uuid.uuid1().hex
    insert(id, name, live_id, local_video_path, duration, stage, False)
    return id


def select_by_id(video_id: str):
    """
    SELECT * FROM videos where id =
    :return: record size
    """
    sql = """SELECT * FROM videos where id = %s;"""
    db = PostgreSql()
    params = (video_id,)
    result = db.select_one(sql, params)
    return result


if __name__ == '__main__':
    print(storage('20201218221537251781.flv', 'http://tx2play1.douyucdn.cn/live/5964044rH8XLVcJz.flv?uuid=', 'E:/TV/20201218221537251781.flv', 60, 0))
