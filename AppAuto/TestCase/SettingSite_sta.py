# coding:utf-8
__author__ = 'GRUNMI'


from AppAuto.common.MyUnittest import MyTest
from AppAuto.PageObject.SettingPage import SettingPage
from AppAuto.common.Screenshot import screenshot
import unittest
from BeautifulReport import BeautifulReport
import os


class SettingTest(MyTest):
    '''站点界面'''
    def setting_verify(self):
        SettingPage(self.driver).setting_site()

    def test_setting(self):
        '''站点设置'''
        self.setting_verify()
        # 定制手机无法调用uiautomator2，不能获取到toast
        # self.assertEqual(SettingPage(self.driver).setting_success(), "保存设置")
        self.assertEqual(SettingPage(self.driver).success_setting(), "登录")
        screenshot(self.driver, "保存站点设置")

if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(SettingTest('test_setting'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suit)
