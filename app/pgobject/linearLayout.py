from app.pgobject.addmembers import Addmembers
from app.pgobject.pagebase import Pagebase
from appium.webdriver.common.mobileby import MobileBy

from app.pgobject.screch import Screch

'''
        通讯录page
'''

class LinearLayout(Pagebase):
    path = '../data/linearLayout.yaml'

    #点击搜索，返回搜索页page
    def click_screch(self):
        # screchele =(MobileBy.ID, "com.tencent.wework:id/h9z")
        # self.steps(self.path, 'wait')
        # self.webdriver_wait(screchele)
        #self.find_click(screchele)
        self.steps(self.path, 'click_screch')
        return Screch(self.driver)


    # 点击添加，返回添加page
    def add_num(self):
        # ele = self.find_by_scroll('添加成员')
        # ele.click()
        self.steps(self.path, 'add_num')
        #self.find_click((MobileBy.XPATH, '//*[@text="添加成员"]'))
        return Addmembers(self.driver)

