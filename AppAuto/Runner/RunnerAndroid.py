# coding:utf-8
__author__ = 'GRUNMI'


import unittest
from AppAuto.TestCase.SettingSite_sta import SettingTest
import HTMLTestReportCN
import os
import time


def run_main():
    suit = unittest.TestSuite()
    suit.addTest(SettingTest('test_setting'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suit)


def run_discover():
    discover = unittest.defaultTestLoader.discover('../TestCase', pattern='*_sta.py')
    runner = unittest.TextTestRunner()
    runner.run(discover)


def HTMLTestRunnerCN_report():
    PATH = lambda P: os.path.abspath(os.path.join(os.path.dirname(__file__), P))
    report_name = time.strftime("%Y-%m-%d %H-%M-%S")
    report_path = PATH("../Report")+"\\"+report_name+".html"
    test_suite = unittest.defaultTestLoader.discover('../TestCase', pattern='*_sta.py')
    fp = open(report_path, 'wb')
    # 生成报告的Title,描述
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fp,
        verbosity=2,
        title='巴枪自动化测试报告',
        description='测试用例结果',
        tester='GRUNMI'
    )
    runner.run(test_suite)


if __name__ == '__main__':
    # run_main()
    # run_discover()
    HTMLTestRunnerCN_report()