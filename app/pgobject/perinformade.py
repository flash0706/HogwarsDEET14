from app.pgobject.editinfo import Editinfo
from app.pgobject.pagebase import Pagebase
from appium.webdriver.common.mobileby import MobileBy

class Perinformade(Pagebase):
    path = '../data/perinformade.yaml'
    def clickedit(self):
        self.steps(self.path, 'clickedit')
        return Editinfo(self.driver)

