# coding:utf-8
__author__ = 'GRUNMI'

import os
import re


class GetDeviceInfo:
    def __init__(self):
        PATH = lambda P: os.path.abspath(os.path.join(os.path.dirname(__file__), P))
        self.apkPath = PATH("../App/6.18.1015.5_input2.apk")
        self.appPackageAdb = list(os.popen("aapt dump badging {}".format(self.apkPath)).readlines())

    def get_apk_package_name(self):
        return re.findall("\'com\w*.*?\'", self.appPackageAdb[0])[0].strip("'")

    def get_apk_launch_activity_name(self):
        # print(self.appPackageAdb)
        for info in self.appPackageAdb:
            if re.findall("launchable-activity: name='.*?'", info):
                # print(re.findall("launchable-activity: name='.*?'", info))
                return re.findall("launchable-activity: name='.*?'", info)[0].replace("launchable-activity: name='","").strip("'")

    def get_device_state(self):
        """
        获取设备状态： offline | bootloader | device
        """
        return os.popen("adb shell get-state").read().strip()

    def get_product_name(self):
        """
        获取设备名称
        """
        return os.popen('adb shell getprop ro.product.name').read().strip()

    def get_platform_version(self):
        """
        获取设备版本
        """
        return os.popen('adb shell getprop ro.build.version.release').read().strip()

    def get_sdk_version(self):
        """
        获取设备SDK版本号
        """
        return list(os.popen("adb shell getprop ro.build.version.sdk").readlines())[0].strip('\n')

    def get_product_brand(self):
        """
        获取设备品牌
        """
        return list(os.popen("adb shell getprop ro.product.brand").readlines())[0].strip('\n')

    def get_product_model(self):
        """
        获取设备型号
        """
        return list(os.popen("adb shell getprop ro.product.model").readlines())[0].strip('\n')

    def get_product_rom(self):
        """
        获取设备ROM名
        """
        return list(os.popen("adb shell getprop ro.build.display.id").readlines())[0].strip('\n')

    def get_device_UDID(self):
        devices = os.popen('adb devices').read().strip()
        pattern = r'\n.*\t'
        device = re.compile(pattern=pattern).findall(devices)
        for deviceName in device:
            deviceName = deviceName.replace(r"\n", "").strip()
            return deviceName

    def device_info(self):
        # deviceState = self.get_device_state()
        deviceName = self.get_product_name()
        platformVersion = self.get_platform_version()
        sdkVersion = self.get_sdk_version()
        productBrand = self.get_product_brand()
        productModel=self.get_product_model()
        productRom=self.get_product_rom()
        UDID = self.get_device_UDID()
        appPackage = self.get_apk_package_name()
        appActivity = self.get_apk_launch_activity_name()
        apkPath = self.apkPath

        return {'deviceName': deviceName, 'platformVersion': platformVersion,
                'sdkVersion': sdkVersion, 'productBrand': productBrand, 'productModel': productModel,
                'productRom': productRom, 'UDID': UDID, 'appPackage': appPackage,
                'appActivity': appActivity, 'apkPath': apkPath}

if __name__ == '__main__':
    b = GetDeviceInfo().device_info()
    print(b)
