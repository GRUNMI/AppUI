# coding:utf-8
__author__ = 'GRUNMI'

import os
import csv
from AppAuto.common.LogOutput import Log

PATH = lambda P:os.path.abspath(os.path.join(os.path.dirname(__file__), P))

mylogger = Log().get_logger()


def read_case_data(data):
    with open(PATH("../ConfigData/CaseData.csv")) as f:
        reader = csv.reader(f)
        for value in reader:
            # print(value)
            if value.count(data):
                mylogger.info("获取到{}是{}".format(data, value[1]))
                return value[1]
        mylogger.info("CaseDace中不存在{}值".format(data))

if __name__ == '__main__':
    read_case_data('password')