# coding:utf-8
__author__ = 'GRUNMI'

from AppAuto.PageObject.CommonElement import CommonEle
from selenium.webdriver.common.by import By
from AppAuto.common.ReadXLSX import ReadXLSX


# 创建自动干线任务
class CreateAutomainlineTaskPage(CommonEle):
    caseData = ReadXLSX("CreateAutomainlineTask_sta")
    elements = ReadXLSX("page_ele")
    startPoint = (By.ID, elements.read_xlsxData("D24"))

    def into_automainline(self):
        self.business_area()
        self.into_automainline_task()

    def car_into_place(self, intoPlace):
        self.select_car_into_place(intoPlace)

    def Independent_goods(self):
        self.auto_goods()

    def input_waybill(self, waybillNumber):
        self.scan_waybill(waybillNumber)

    def select_destination(self, destination):
        self.destination_select(destination)

    def confirm(self):
        self.confirm_batch()

    def confirm_path(self):
        self.path_confirm()

    def create_automainline_task(self, intoPlace=caseData.read_xlsxData("A2"),
                                 waybillNumber=caseData.read_xlsxData("B2"),
                                 destination=caseData.read_xlsxData("C2")):
        self.into_automainline()
        self.car_into_place(intoPlace)
        self.auto_goods()
        self.input_waybill(waybillNumber)
        self.select_destination(destination)
        self.confirm()
        self.confirm_path()

    def create_success(self):
        self.ele_presence(self.startPoint)