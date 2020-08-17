from time import sleep

from app.pgobject.pagebase import Pagebase
from appium.webdriver.common.mobileby import MobileBy
from app.pgobject.perinformation import Perinformation


class Screch(Pagebase):
    path ='../data/screch.yaml'
    def editText(self, name):
        self._params['name'] = name
        self.steps(self.path, 'editText')
        return Perinformation(self.driver)

    def isexistence(self, name):
        self._params['name'] = name
        return self.steps(self.path, 'isexistence')