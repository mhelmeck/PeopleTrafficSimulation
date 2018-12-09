import time

from influxdb import InfluxDBClient

from src.influx.InfluxCredentials import *

CLIENT = InfluxDBClient(host, port, user, password, dbname)


def influx_timestamp(ts=time.time()):
    return str("%.9f" % ts).replace(".", "")


class InfluxService:
    def __init__(self):
        self.pedestrians_db_name = dbname
        self._create_ped_db()

    def _create_ped_db(self):
        db_list = CLIENT.get_list_database()
        if {'name': self.pedestrians_db_name} not in db_list:
            print("Creating ", db_list, " database")
            CLIENT.create_database(self.pedestrians_db_name)

    def get_ped_coordinate(self, user_id, ts="now()"):
        query = "select * from \"{}\" where time > {} - 20000ms AND time <= {} + 2000ms ORDER BY time DESC LIMIT 1".format(
            user_id, ts, ts)
        result_generator = CLIENT.query(query).get_points()
        result = next(result_generator)
        x = result['x']
        y = result['y']
        point = [x, y]
        return point

    def get_ped_coordinate2(self, user_id):
        query = "select last(*) from \"{}\"".format(user_id)
        result_generator = CLIENT.query(query).get_points()
        result = next(result_generator)
        x = result['last_x']
        y = result['last_y']
        point = [x, y]
        return point


    def get_all_ped_coords(self):
        ped_ids = CLIENT.get_list_measurements()
        curr_localisations = []
        for ped_id in ped_ids:
            curr_localisations.append(self.get_ped_coordinate2(ped_id['name']))
        return curr_localisations
