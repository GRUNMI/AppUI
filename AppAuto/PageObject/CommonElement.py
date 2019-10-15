# coding:utf-8
__author__ = 'GRUNMI'


from AppAuto.common.Base import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from AppAuto.common.LogOutput import Log
import time
from AppAuto.common.ConnectSql import SqlServer,MySql
from AppAuto.common.ReadXLSX import ReadXLSX


mylogger = Log().get_logger()
mylogger.info('当前运行文件：{}'.format(__file__))


class CommonEle(Base):
    elements = ReadXLSX("common_ele")
    businessBtn = (By.XPATH, elements.read_xlsxData("D2"))
    automainlineBtn = (By.XPATH, elements.read_xlsxData("D3"))
    autoGoods = (By.ID, elements.read_xlsxData("D4"))  # 自主带货
    carPosition = (By.ID, elements.read_xlsxData("D5"))
    carIntoPlace = (By.XPATH, elements.read_xlsxData("D6"))
    intoPlacePosition = (By.ID, elements.read_xlsxData("D7"))  # 场地编码
    carIntoPlaceConfirm = (By.XPATH, elements.read_xlsxData("D8"))
    carLeavePlace = (By.ID, elements.read_xlsxData("D9"))
    leavePlaceConfirm = (By.XPATH, elements.read_xlsxData("D10"))
    scanWaybillBox = (By.ID, elements.read_xlsxData("D11"))  # 扫描单号
    confirmBatch = (By.ID, elements.read_xlsxData("D12"))  # 确认批次
    destination = (By.ID, elements.read_xlsxData("D13"))  # 返回一组 选择目的地（list）
    scanDestination = (By.ID, elements.read_xlsxData("D14"))  # 自选目的地
    selsctDestinationConfirm = (By.ID, elements.read_xlsxData("D15"))  # 确定按钮
    checkBtn = (By.ID, elements.read_xlsxData("D16"))  # 安检确定按钮
    pathConfirm = (By.ID, elements.read_xlsxData("D17"))  # 路线确认
    pathSelectConfirm = (By.ID, elements.read_xlsxData("D18"))  # 路线选择确定
    passingBtn = (By.ID, elements.read_xlsxData("D19"))  # 顺带
    startPoint = (By.ID, elements.read_xlsxData("D20"))  # 起点，用于展开干线任务列表

    "com.seuic.kysy:id/iv_add_passing_scan"  # 顺带
    "com.seuic.kysy:id/tv_transit_name"  # 经停 验证生成任务

    # 业务区
    def business_area(self):
        self.ele_visibility(self.businessBtn).click()

    # 干线任务
    def into_automainline_task(self):
        self.ele_visibility(self.automainlineBtn).click()

    # 自主带货
    def auto_goods(self):
        self.ele_visibility(self.autoGoods).click()

    # 车入场
    def select_car_into_place(self, locName):
        time.sleep(1)
        car_position_text = self.ele_visibility(self.carPosition).text
        if "离" in car_position_text:
            self.find_element(*self.carIntoPlace).click()
            palce = self.ele_visibility(self.intoPlacePosition)
            palce.click()
            # 连接数据库查询场地编码
            sql = "SELECT Col_002 from TB_DomainSJDCodeNEW WHERE Col_001=N'{}'".format(locName)
            palceNum = SqlServer("sqlserver").execute_query(sql)

            palce.send_keys(palceNum)
            self.driver.press_keycode(66)
            time.sleep(2)
            if "500米" in self.driver.page_source:
                self.ele_visibility(self.carIntoPlaceConfirm).click()

        elif locName in car_position_text and "已到达" in car_position_text:
            pass

        else:
            self.find_element(*self.carLeavePlace).click()
            self.ele_visibility(self.leavePlaceConfirm).click()
            # 重新入场
            self.ele_visibility(self.carIntoPlace).click()
            palce = self.ele_visibility(self.intoPlacePosition)
            palce.click()
            # 连接数据库查询场地编码
            sql = "SELECT Col_002 from TB_DomainSJDCodeNEW WHERE Col_001=N'{}'".format(locName)
            palceNum = SqlServer("sqlserver").execute_query(sql)

            palce.send_keys(palceNum)
            self.driver.press_keycode(66)
            time.sleep(2)
            if "500米" in self.driver.page_source:
                self.ele_visibility(self.carIntoPlaceConfirm).click()

    # 车离场
    def car_leave(self):
        time.sleep(1)
        car_position_text = self.ele_visibility(self.carPosition).text
        if "已到达" in car_position_text:
            self.find_element(*self.carLeavePlace).click()
            self.ele_visibility(self.carLeavePlace).click()
        else:
            mylogger.info("车已离场，不需要再次离场")

    # 扫描运单
    def scan_waybill(self, waybillNumber):
        scan_waybill_box = self.ele_visibility(self.scanWaybillBox)
        scan_waybill_box.clear()
        scan_waybill_box.click()
        scan_waybill_box.send_keys(waybillNumber)
        mylogger.info("已输入运单号：{}".format(waybillNumber))
        if scan_waybill_box.text == waybillNumber:
            mylogger.info("输入的运单号正确")
        else:
            mylogger.info("输入的运单号不正确，将使用press_keycode输入运单号")
            number = {
                '0': 7,
                '1': 8,
                '2': 9,
                '3': 10,
                '4': 11,
                '5': 12,
                '6': 13,
                '7': 14,
                '8': 15,
                '9': 16,
            }
            for num in str(waybillNumber).strip():
                for i in num:
                    self.driver.press_keycode(number[i])
                mylogger.info("已输入运单号：{}".format(waybillNumber))
        # 点击键盘回车键
        self.driver.press_keycode(66)
        # 隐藏键盘
        # self.hide_keyboard()

    # 选择目的地
    def destination_select(self, locName):
        time.sleep(2)
        loc = self.find_elements(*self.destination)
        for i in loc:
            if locName == i.text:
                i.click()
                self.find_element(*self.selsctDestinationConfirm).click()
                if WebDriverWait(self.driver, 5, 0.5).until(EC.visibility_of_element_located(self.checkBtn)):
                    self.find_element(*self.checkBtn).click()
                return True
        # 自选目的地
        sql = "SELECT Col_002 from TB_DomainSJDCodeNEW WHERE Col_001=N'{}'".format(locName)
        palceNum = SqlServer("sqlserver").execute_query(sql)
        palce = self.find_element(*self.scanDestination).click()
        palce.send_keys(palceNum)
        # 点击键盘回车键
        self.driver.press_keycode(66)
        self.find_element(*self.selsctDestinationConfirm).click()
        time.sleep(1)
        if WebDriverWait(self.driver, 5, 0.5).until(EC.visibility_of_element_located(self.checkBtn)):
            self.find_element(*self.checkBtn).click()
        return True

    # 确认批次
    def confirm_batch(self):
        self.ele_visibility(self.confirmBatch).click()

    # 路线确认
    def path_confirm(self):
        self.ele_visibility(self.pathConfirm).click()
        self.find_element(*self.pathSelectConfirm).click()

    # 点击顺带按钮
    def click_passing_btn(self):
        self.ele_visibility(self.passingBtn).click()

    # 展开干线任务列表
    def unfold_antomainline_task_list(self):
        self.ele_visibility(self.startPoint).click()
