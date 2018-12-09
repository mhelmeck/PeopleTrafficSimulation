from influxdb import SeriesHelper

from src.influx import InfluxService


class PedestriansCoordSeries(SeriesHelper):
    class Meta:
        client = InfluxService.CLIENT
        series_name = '{ped_id}'
        fields = ['x', 'y']
        tags = ['ped_id']
        bulk_size = 5
        autocommit = True
