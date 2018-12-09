#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2018 Artur Siepietowski
# Copyright 2018 Maciej Hełmecki
#
# This file is part of PeopleTrafficSimulation
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

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
