#!/usr/bin/python
from helper.measurements import group_frequency_measurements, delete_old_measurements
import sys


if __name__ == '__main__':
    if len(sys.argv) > 1:
        days = int(sys.argv[1])
        delete_old_measurements(days)
    else:
        delete_old_measurements()
    group_frequency_measurements()
