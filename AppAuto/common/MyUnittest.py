# coding:utf-8
__author__ = 'GRUNMI'


import unittest
from .MyDriver import my_driver


class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = my_driver()
        # 隐性等待，最长时间20秒
        self.driver.implicitly_wait(20)

    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()