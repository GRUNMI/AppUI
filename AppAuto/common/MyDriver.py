# coding:utf-8
__author__ = 'GRUNMI'


from appium import webdriver
from AppAuto.Adb.GetDeviceInfo import GetDeviceInfo

deviceInfo = GetDeviceInfo().device_info()


def my_driver():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = deviceInfo['platformVersion']
    desired_caps['deviceName'] = deviceInfo['deviceName']
    desired_caps['version'] = deviceInfo['platformVersion']
    desired_caps['udid'] = deviceInfo['UDID']
    desired_caps['appPackage'] = deviceInfo['appPackage']
    desired_caps['appActivity'] = deviceInfo['appActivity']
    desired_caps['app'] = deviceInfo['apkPath']
    # 不需要再次安装
    desired_caps['noRest'] = True
    # 调用uiautomator2, 获取toast
    # desired_caps['automationName'] = 'Uiautomator2'
    # 使用 Unicode 输入法
    # desired_caps['unicodeKeyboard'] = True
    # 重置输入法到原有状态
    # desired_caps['resetKeyboard'] = True
    # 不对安装的apk重签名
    desired_caps['noSign'] = True
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver


if __name__ == '__main__':
    driver = my_driver()

