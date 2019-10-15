# coding:utf-8
__author__ = 'GRUNMI'


import os
import configparser
from common.LogOutput import Log

PATH = lambda P: os.path.abspath(os.path.join(os.path.dirname(__file__), P))


mylogger = Log().get_logger()
mylogger.info('当前运行文件：{}'.format(__file__))


# 重新configparser方法，去掉lower()转成小写
class MyConfigParser(configparser.ConfigParser):
    def __init__(self, defaults=None):
        configparser.ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr


class ReadConfig:
    def __init__(self):
        self.cfPath = PATH("../ConfigData")
        self.cfFile = PATH("../ConfigData/SqlInfo.ini")
        self.cf = MyConfigParser()
        self.cf.read(self.cfFile, encoding='utf-8')

    def get_all_value(self, sectionName):
        sections = self.cf.sections()
        if not sections.count(sectionName):
            mylogger.info("获取配置文件section_name：{}，不存在".format(sectionName))
        else:
            data = dict(self.cf.items(sectionName))
            mylogger.info("获取配置文件sections：{} 下的options：{}".format(sectionName, data))
            return data

if __name__ == '__main__':
    data = ReadConfig().get_all_value("sqlserver")
    print(data)