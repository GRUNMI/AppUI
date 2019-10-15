# coding:utf-8
__author__ = 'GRUNMI'


from AppAuto.common.MyUnittest import MyTest
from AppAuto.PageObject.SettingPage import SettingPage
from AppAuto.PageObject.LoginPage import LoginPage
from AppAuto.PageObject.CreateAutomainlineTaskPage import CreateAutomainlineTaskPage
from AppAuto.common.ReadXLSX import ReadXLSX
from AppAuto.common.Screenshot import screenshot
import unittest


class CreateAutomainlineTaskTest(MyTest):
    '''创建自主带货任务'''
    def createAutomainlineTaskTest_verity(self, intoPlace, waybillNumber, destination):
        SettingPage(self.driver).setting_site()
        LoginPage(self.driver).login()
        CreateAutomainlineTaskPage(self.driver).create_automainline_task(intoPlace, waybillNumber, destination)
        self.caseData = ReadXLSX("CreateAutomainlineTask_sta")

    def test_createAutomainlineTaskTest(self):
        '''创建自主任务'''
        self.createAutomainlineTaskTest_verity(intoPlace=self.caseData.read_xlsxData("A2"),
                                               waybillNumber=self.caseData.read_xlsxData("B2"),
                                               destination=self.caseData.read_xlsxData("C2"))
        CreateAutomainlineTaskPage(self.driver).create_success()
        screenshot(self.driver, "生成自主任务成功")

if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(CreateAutomainlineTaskTest('test_createAutomainlineTaskTest'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suit)