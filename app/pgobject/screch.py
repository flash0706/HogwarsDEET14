from time import sleep

from app.pgobject.pagebase import Pagebase
from appium.webdriver.common.mobileby import MobileBy
from app.pgobject.perinformation import Perinformation


class Screch(Pagebase):
    path ='../data/screch.yaml'
    def editText(self, name):
        self._params['name'] = name
        self.steps(self.path, 'editText')
        # elename = f"//*[(@text='{name}')and (@class='android.widget.TextView')]"
        # print(elename)
        # self.find_sendkey((MobileBy.ID, 'com.tencent.wework:id/fxc'), name)
        # # self.webdriver_wait((MobileBy.XPATH, elename))
        # self.find_click((MobileBy.XPATH, elename))
        return Perinformation(self.driver)

    def isexistence(self, name):
        # sleep(3)
        # elename = f"//*[(@text='{name}')and (@class='android.widget.TextView')]"
        # return self.isPresent((MobileBy.XPATH, elename))
        self._params['name'] = name
        return self.steps(self.path, 'isexistence')