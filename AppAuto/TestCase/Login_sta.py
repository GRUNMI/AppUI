# coding:utf-8
__author__ = 'GRUNMI'


from AppAuto.common.MyUnittest import MyTest
from AppAuto.PageObject.SettingPage import SettingPage
from AppAuto.PageObject.LoginPage import LoginPage
from AppAuto.common.ReadXLSX import ReadXLSX
from AppAuto.common.Screenshot import screenshot
import unittest


class LoginTest(MyTest):
    caseData = ReadXLSX("Login_sta")

    '''登录界面'''
    def login_verity(self, username, password):
        SettingPage(self.driver).setting_site()
        self.P = LoginPage(self.driver)
        self.P.login(username=username, pwd=password)

    def test_correct_user_password(self):
        '''正确的账号和密码'''
        self.login_verity(self.caseData.read_xlsxData('a2'), self.caseData.read_xlsxData('b2'))
        # LoginPage(self.driver).correct_user_password_verity()
        self.assertEqual(self.P.correct_user_password_verity(), "主菜单", msg="text判断有误")
        screenshot(self.driver, "用户名密码正确")

    def test_password_empty(self):
        '''密码为空'''
        self.login_verity(self.caseData.read_xlsxData('a3'), self.caseData.read_xlsxData('b3'))
        self.assertEqual(self.P.password_empty_verity(), "请输入密码！", msg="text判断有误")
        screenshot(self.driver, "密码为空")

    def test_username_empty(self):
        '''用户名为空'''
        self.login_verity(self.caseData.read_xlsxData('a4'), self.caseData.read_xlsxData('b4'))
        self.P.username_empty_verity()
        self.assertEqual(self.P.username_empty_verity(), "请输入员工编号！", msg="text判断有误")
        screenshot(self.driver, "密码为空")

if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(LoginTest('test_correct_user_password'))
    suit.addTest(LoginTest('test_password_empty'))
    suit.addTest(LoginTest('test_username_empty'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suit)
