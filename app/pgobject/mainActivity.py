from time import sleep

from app.pgobject.linearLayout import LinearLayout
from app.pgobject.pagebase import Pagebase
from appium.webdriver.common.mobileby import MobileBy


'''
    主页page
'''

class MainActivity(Pagebase):
    contactlist = (MobileBy.XPATH,
                   "//android.widget.TextView[@text='通讯录']")
    '''
        点击通讯录，返回通讯录page
    '''
    def click_cont(self):
        sleep(3)
        # self.webdriver_wait_click(self.contactlist)
        self.find_click(self.contactlist)
        # self.driver.find_element(MobileBy.XPATH,
        #            "//android.widget.TextView[@text='通讯录']").click()

        return LinearLayout(self.driver)
