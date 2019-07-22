#!/usr/bin/env python

import math


class Calculator:
    """
    Simple calculator takes in a list
    of values and runs basic descriptive
    stats on them
    """
    def __init__(self, data):
        self.data = data
        # update does most of the work
        self.update_stats()
#   def __check

    def __calc_mean(self):
        return round(sum(self.data) / len(self.data), 2)

    def __calc_med(self):
        mid = len(self.data) / 2
        if len(self.data) % 2 == 0:
            return (self.data[int(mid + .5)] + self.data[int(mid - .5)]) / 2
        else:
            return self.data[int(mid - .5)]

    def __calc_var(self):
        sum = 0
        for i in self.data:
            sum += (i - self.mean)**2
        return round(sum / (len(self.data) - 1), 2)

    def __calc_standev(self):
        return round(math.sqrt(self.variance), 2)

    # allow a user to add list data
    def add_data(self, data):
        # add new data and sort it
        self.data.extend(data)
        self.data.sort()
        # re-run all stats calcs on new data
        self.update_stats()

    # allow a user to remove a specific datum
    def remove_data(self, item):
        self.data.remove(item)
        self.update_stats()

    # do the work to get our stats
    def update_stats(self):
        # assumes data has been set or re-set
        self.length = len(self.data)
        self.mean = self.__calc_mean()
        self.median = self.__calc_med()
        self.variance = self.__calc_var()
        self.standev = self.__calc_standev()
