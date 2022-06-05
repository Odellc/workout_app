import harperdb

url = "https://workout-codell.harperdbcloud.com"
username = "odellc"
password = "Everly2020"


SCHEMA = "workout_repo"
TABLE = "workout"
TABLE_TODAY = "workout_today"


def insert_workout(workout_data):
    return db.insert(SCHEMA, TABLE, [workout_data])

def delete_workout(workout_id):
    return db.delete(SCHEMA, TABLE, [workout_id])

def get_all_workouts():
    return db.sql(f"select video_id, channel, title, duration from {SCHEMA}.{TABLE}")

def get_workout_today():
    return db.sql(f"SELECT * FROM {SCHEMA}.{TABLE_TODAY} where id=0")


def update_workout_today(workout_data, insert=False):
    workout_data['id'] = 0
    if insert:
        return db.insert(SCHEMA, TABLE_TODAY, [workout_data])
    return db.update(SCHEMA, TABLE_TODAY, [workout_data])


db = harperdb.HarperDB(
    url=url,
    username=username,
    password=password
)
