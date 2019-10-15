# coding:utf-8
__author__ = 'GRUNMI'


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction


class Base(object):
    def __init__(self, driver):
        self.driver = driver

    # *得到是一个元组，**得到是一个字典
    def find_element(self, *ele):
        return self.driver.find_element(*ele)

    def find_elements(self, *ele):
        return self.driver.find_elements(*ele)

    def ele_visibility(self, ele):
        #  判断某个元素是否可见. 可见代表元素非隐藏，并且元素的宽和高都不等于0
        return WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located(ele))

    def ele_not_visibility(self, ele):
        #  判断某个元素是否可见. 直到某个元素不可见 bool
        return WebDriverWait(self.driver, 10, 0.5).until_not(EC.visibility_of_element_located(ele))

    def ele_invisibility(self, ele):
        #  判断某个元素中是否不存在于dom树或不可见
        return WebDriverWait(self.driver, 10, 0.5, ignored_exceptions=None).until(EC.invisibility_of_element_located(ele))

    def ele_presence(self, ele):
        # 判断某个元素是否被加到了dom树里，并不代表该元素一定可见
        return WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(ele))

    def ele_dom(self, ele):
        # 判断是否至少有1个元素存在于dom树中
        return WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_all_elements_located(ele))

    def ele_contain_text(self, ele, text):
        # 判断某个元素中的text是否包含预期字符串
        return WebDriverWait(self.driver, 10, 0, 0.5).until(EC.text_to_be_present_in_element(ele, text))

    def ele_contain_value(self, ele, value):
        # 判断某个元素中的value属性是否包含预期字符串
        return WebDriverWait(self.driver, 10, 0, 0.5).until(EC.text_to_be_present_in_element_value(ele, value))

    def ele_selected(self, ele):
        # 判断某个元素是否被选中了,一般用在下拉列表
        return WebDriverWait(self.driver, 10, 0.5).until(EC.element_to_be_selected(ele))

    def ele_frame(self, ele):
        # 判断该frame是否可以switch进去，如果可以的话，返回True并且switch进去，否则返回False
        return WebDriverWait(self.driver, 10, 0.5).until(EC.frame_to_be_available_and_switch_to_it(ele))

    def find_toast(self, msg):
        try:
            toast = WebDriverWait(self.driver, 5, 0.1).until(EC.presence_of_element_located(
                (By.XPATH, "//*[contains(@text,'"+msg+"')]")))
            # print(toast.text)
            return toast.text
        except Exception as e:
            return e

    def get_ele_size(self, *ele):
        '''
        获取元素的大小
        size 返回是字典{'y': 38, 'x': 192}
        '''
        eleSize = self.find_element(*ele).size
        width = eleSize["width"]
        height = eleSize["height"]
        eleSize = [width, height]
        return eleSize

    def get_ele_location(self, *ele):
        '''
        获取元素的左上角坐标位置
        location 返回是字典{'y': 38, 'x': 192}
        '''
        eleX = self.find_element(*ele).location.get('x')
        eleY = self.find_element(*ele).location.get('y')
        eleCoords = [eleX, eleY]
        return eleCoords

    def scroll_ele(self, originEle, destinationEle):
        '''
        滚动元素
        '''
        startEle = self.get_ele_location(*originEle)
        endEle = self.get_ele_location(*destinationEle)
        self.driver.swipe(startEle[0], startEle[1], endEle[0], endEle[1])

    def scroll(self, originEle, destinationEle):
        '''
        从元素origin_ele滚动至元素destination_ele
        '''
        self.driver.scroll(originEle, destinationEle)

    def window_size(self):
        '''
        获取当前屏幕的尺寸大小
        get_window_size()返回是字典{'y': 38, 'x': 192}
        '''
        windowSize = self.driver.get_window_size()
        return windowSize

    def swipe_to_left(self, t):
        '''
        向左滑动
        '''
        windowsSize = self.window_size()
        width = windowsSize.get("width")
        height = windowsSize.get("height")
        self.driver.swipe(width*3/4, height/2, width*1/4, height/2, t)

    def swipe_to_right(self, t):
        '''
        向右滑动
        '''
        windowsSize = self.window_size()
        width = windowsSize.get("width")
        height = windowsSize.get("height")
        self.driver.swipe(width * 1/4, height / 2, width * 3/4, height / 2, t)

    def swipe_to_top(self, t):
        '''
        向上滑动
        '''
        windowsSize = self.window_size()
        width = windowsSize.get("width")
        height = windowsSize.get("height")
        self.driver.swipe(width/2, height*3/4, width/2, height*1/4, t)

    def swipe_to_down(self, t):
        '''
        向下滑动
        '''
        windowsSize = self.window_size()
        width = windowsSize.get("width")
        height = windowsSize.get("height")
        self.driver.swipe(width / 2, height * 1 / 4, width / 2, height * 3 / 4, t)

    def switch_to_app(self):
        # 切换到原生app
        self.driver.switch_to.context("NATIVE_APP")

    def switch_to_h5(self):
        # 切换到h5
        for i in self.driver.contexts:
            if i.lower().startswith("web"):
                self.driver.switch_to.context(i)

    def current_context(self):
        '''
        获取当前会话
        '''
        return self.driver.current_context

    def press(self, ele=None, x=None, y=None):
        '''
        按压
        eg:滑动解锁，连接move_to使用
        '''
        TouchAction(self.driver).press(ele, x, y)

    def long_press(self, milliseconds, ele=None, x=None, y=None):
        '''
        长按
        '''
        TouchAction(self.driver).long_press(ele, x, y, duration=milliseconds).release().perform()

    def tap(self, ele=None, x=None, y=None):
        '''
        点击
        '''
        TouchAction(self.driver).tap(ele, x, y)

    def ele_move_to_ele(self, startEle=None, startX=None, startY=None, endEle=None, endX=None, endY=None):
        '''
        点到点 移动元素
        '''
        self.press(startEle, startX, startY).wait(1000).perform().move_to(endEle, endX, endY).release().perform()


    def pinch(self, ele, percent=200, steps=50):
        '''
        缩放
        '''
        self.driver.pinch(ele, percent, steps)

    def zoom(self, ele, percent, steps):
        '''
        放大
        '''
        self.driver.zoom(ele, percent, steps)

    def keyevent(self, keyCode):
        self.driver.keyevent(keyCode)

    def press_keycode(self, *ele, keyCode):
        # 需要先点击input输入框，再执行press_keycode方法
        self.find_element(*ele).click()
        # 查看对应的按键码
        self.driver.press_keycode(keyCode)

    def long_press_keycode(self, keyCode):
        # 长按某键
        self.driver.long_press_keycode(keyCode)

    def get_attr_value(self, *ele, attr):
        '''
        获取元素的属性值
        '''
        return self.find_element(*ele).get_attribute(attr)

    def ele_is_selected(self, *ele):
        '''
        返回bool值
        '''
        return self.find_element(*ele).is_selected()

    def ele_is_displayed(self):
        '''
        是否可见
        '''
        return self.driver.is_displayed()

    def shake(self):
        '''
        摇动
        '''
        self.driver.shake()

    def hide_keyboard(self):
        '''
        隐藏键盘
        '''
        self.driver.hide_keyboard()

    def background_app(self, seconds):
        '''
        置后台seconds再运行
        '''
        self.driver.background_app(seconds)

    def launch_app(self):
        '''
        启动app
        '''
        self.driver.launch_app()

    def open_notifications(self):
        '''
        打开通知栏
        '''
        self.driver.open_notifications()

    def deactivate_ime_engine(self):
        '''
        关闭安卓设备当前的输入法
        '''
        self.driver.deactivate_ime_engine()

    def is_ime_active(self):
        '''
        检查设备是否有输入法服务活动 bool值
        '''
        return self.driver.is_ime_active()

    def current_activity(self):
        '''
        获取当前activity
        '''
        return self.driver.current_activity()

    def reset(self):
        '''
        删除应用数据
        '''
        return  self.driver.reset()

