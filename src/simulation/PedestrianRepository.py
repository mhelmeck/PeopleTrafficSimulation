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


class PedestrianRepository:
    class __PedestrianRepository:
        def __init__(self, arg):
            self.val = arg
            self.pedestrians = arg[0]
            self.repo_name = arg[1]

        def __str__(self):
            return repr(self) + self.val

    instance = None

    def __init__(self, arg):
        if not PedestrianRepository.instance:
            PedestrianRepository.instance = PedestrianRepository.__PedestrianRepository(arg)
        else:
            PedestrianRepository.instance.val = arg

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __repr__(self):
        return str(self.repo_name) + str(self.pedestrians)

    def move_all(self):
        # should be runned on multiple threads depending on system capacity
        for pedestrian in self.pedestrians:
            pedestrian.move()
