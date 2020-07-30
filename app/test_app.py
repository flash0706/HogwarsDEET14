from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDW:

    def setup(self):
       self.desire_cap = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": "com.xueqiu.android.common.MainActivity",
            "noReset": "true",
            # "dontStopAppOnReset": "true",
            "skipDeviceInitialization": "true",
            "unicodeKeyBoard": "true",
            "resetKeyBoard": "true"}
       self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.desire_cap)
       self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_case(self):
        self.el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(self.el1.get_attribute("text"))
        self.el1.click()
        self.el2 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        self.el2.send_keys("阿里巴巴")
        print('11')

    def test_touchaction(self):
        action = TouchAction(self.driver)
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width/2)
        y_start = int(height *4/5)
        y_end = int(height*1/5)
        action.press(x=x1,y=y_start).wait(200).move_to(x=x1,y=y_end).release().perform()

    def test_case1(self):
        self.el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(self.el1.get_attribute("text"))
        self.el1.click()
        self.el2 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        self.el2.send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name'and @text='阿里巴巴']").click()
        #self.el = self.driver.find_element_by_xpath("//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        self.el = (MobileBy.XPATH, "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        ele = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.el))
        print(ele.text)
        #price = self.el.get_attribute('text')

        #print(f'当前股票价格{price}')

    def test_toast(self):
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Make a Popup').click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, 'Clicked popup')]").text
