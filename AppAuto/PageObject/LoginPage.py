# coding:utf-8
__author__ = 'GRUNMI'

from AppAuto.common.Base import Base
from selenium.webdriver.common.by import By
from AppAuto.common.ReadXLSX import ReadXLSX


# 登录界面
class LoginPage(Base):
    elements = ReadXLSX("page_ele")
    caseData = ReadXLSX("Login_sta")
    username = (By.ID, elements.read_xlsxData("D13"))
    pwd = (By.ID, elements.read_xlsxData("D14"))
    loginBtn = (By.ID, elements.read_xlsxData("D15"))
    title = (By.ID, elements.read_xlsxData("D16"))
    inputPwdHit = (By.ID, elements.read_xlsxData("D17"))
    inputNumberHit = (By.ID, elements.read_xlsxData("D18"))

    def input_username(self, value):
        self.ele_visibility(self.username).send_keys(value)

    def input_pwd(self, value):
        self.ele_visibility(self.pwd).send_keys(value)

    def click_login(self):
        self.ele_visibility(self.loginBtn).click()

    # 默认正确的参数
    def login(self, username=caseData.read_xlsxData("A2"), pwd=caseData.read_xlsxData("B2")):
        self.input_username(username)
        self.input_pwd(pwd)
        self.click_login()

    def correct_user_password_verity(self):
        return self.ele_presence(self.title).text

    def password_empty_verity(self):
        return self.ele_presence(self.inputPwdHit).text

    def username_empty_verity(self):
        return self.ele_presence(self.inputNumberHit).text