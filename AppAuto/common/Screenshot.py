# coding:utf-8
__author__ = 'GRUNMI'


import time
import os


def screenshot(driver, imgname):
    PATH = lambda P: os.path.abspath(os.path.join(os.path.dirname(__file__), P))
    imgFolder = PATH("../screenshots")

    if not os.path.exists(imgFolder):
        os.mkdir(PATH("../screenshots"))
    imgname = imgname+'_'+time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
    screen_save_path = PATH("../screenshots") + "\\" + imgname + '.png'
    driver.get_screenshot_as_file(screen_save_path)

if __name__ == '__main__':
    from AppAuto.common.MyDriver import my_driver
    screenshot(my_driver(), "test")
