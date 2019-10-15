# coding:utf-8
__author__ = 'GRUNMI'

import os


def get_all_ime():
    '''
    获取系统上所有输入法
    '''
    return os.system('adb shell ime list -s')

def set_appium_ime():
    '''
    切换到appium输入法
    '''
    os.system('adb shell ime set io.appium.android.ime/.UnicodeIME')

def set_default_ime():
    '''
    切换到系统默认输入法
    '''
    os.system('adb shell settings get secure default_input_method')

def set_android_ime():
    '''
    切换到系统默认输入法
    '''
    os.system('adb shell ime set com.android.inputmethod.latin/.LatinIME')

def set_Fly_ime():
    '''
    切换到讯飞输入法
    '''
    os.system('adb shell ime set com.iflytek.inputmethod/.FlyIME')

def set_other_ime(ime):
    '''
    切换达到第三方输入法
    '''
    os.system('adb shell ime set {}'.format(ime))

if __name__ == '__main__':
    print(get_all_ime())