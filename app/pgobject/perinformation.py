from app.pgobject.pagebase import Pagebase
from appium.webdriver.common.mobileby import MobileBy

from app.pgobject.perinformade import Perinformade


class Perinformation(Pagebase):
    path = '../data/perinformation.yaml'
    def clickmore(self):
        self.steps(self.path, 'clickmore')
        # self.find_click((MobileBy.ID, 'com.tencent.wework:id/h9p'))
        return Perinformade(self.driver)