from app.pgobject.pagebase import Pagebase
from appium.webdriver.common.mobileby import MobileBy



class Editinfo(Pagebase):
    path ='../data/editinfo.yaml'
    def detele(self):
        self.steps(self.path, 'detele')
        from app.pgobject.screch import Screch
        return Screch(self.driver)
