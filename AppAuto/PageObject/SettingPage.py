# coding:utf-8
__author__ = 'GRUNMI'

from AppAuto.common.Base import Base
from selenium.webdriver.common.by import By
from AppAuto.common.ReadXLSX import ReadXLSX


# 设置界面元素
class SettingPage(Base):
    elements = ReadXLSX("page_ele")

    settingBtn = (By.ID, elements.read_xlsxData("D2"))  # 设置按钮
    airport = (By.ID, elements.read_xlsxData("D3"))
    network = (By.ID, elements.read_xlsxData("D4"))
    site = (By.ID, elements.read_xlsxData("D5"))
    saveBtn = (By.ID, elements.read_xlsxData("D6"))

    # 验证设置保存之后的按钮是否存在
    loginBtn = (By.ID, elements.read_xlsxData("D7"))

    def click_setting(self):
        self.ele_visibility(self.settingBtn).click()

    def select_airport(self):
        self.ele_visibility(self.airport).click()

    def select_network(self):
        self.ele_visibility(self.network).click()

    def select_site(self):
        self.ele_visibility(self.site).click()

    def click_save_btn(self):
        self.ele_visibility(self.saveBtn).click()

    def setting_site(self):
        self.click_setting()
        self.select_airport()
        self.select_network()
        self.select_site()
        self.click_save_btn()

    def setting_success(self):
        self.find_toast("保存成功")

    def success_setting(self):
        return self.ele_presence(self.loginBtn).text
