# coding:utf-8
__author__ = 'GRUNMI'

import os


def install_apk(ApkPath):
    os.popen("adb install -r {}".format(ApkPath))
    print("安装成功")
    return True

if __name__ == '__main__':
    install_apk(r'C:\Users\Administrator\Desktop\install-pack\gx\6.18.0928.5.apk')