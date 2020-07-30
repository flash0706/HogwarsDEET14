from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.webdriver import WebDriver


class Pagebase:
    _bolck_list = []
    _error_max_num =3
    _error_count =0
    toast = (MobileBy.XPATH, "//*[@class='android.widget.Toast']")

    def __init__(self, driver: WebDriver=None):
        """

        :type driver: object
        """
        self.driver = driver

    def find(self, by, locator=None):
        try:
            if locator is None:
                rulest = self.driver.find_element(*by)
            else:
                rulest = self.driver.find_element(by, locator)
            return rulest
        except NoSuchElementException as e:
            if self._error_count>self._error_max_num:
                self._error_count =0
                raise e
            self._error_count +=1
            for ele in self._bolck_list:
                eles= self.finds(ele)
                if len(eles) > 0:
                    eles[0].click()
                    return self.find(by,locator)
            raise e

    def finds(self, by, locator=None):
        if locator is None:
            rulest = self.driver.find_elements(by, locator)
        else:
            rulest = self.driver.find_elements(*locator)
        return rulest


    def find_click(self, locator):
        self.find(locator).click()

    def find_sendkey(self, locator, text):
        self.find(locator).send_keys(text)

    def find_by_scroll(self, text):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiScrollable(new UiSelector()'
                                        '.scrollable(true).instance(0))'
                                        '.scrollIntoView(new UiSelector()'
                                        f'.text("{text}").instance(0));')

    def webdriver_wait(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            lambda x: x.find_element(*locator))
        return element

    def webdriver_wait_click(self, locator, timeout=10):
        element = self.webdriver_wait(locator)
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(element))

    def get_toast(self, locator=toast):
        ele = self.webdriver_wait(locator)
        return ele

    def isPresent(self, locator):
        try:
            self.find(locator)
        #except NoSuchElementException:
        except Exception:
            return False
        return True
