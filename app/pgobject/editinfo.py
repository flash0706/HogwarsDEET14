from app.pgobject.pagebase import Pagebase
from appium.webdriver.common.mobileby import MobileBy



class Editinfo(Pagebase):
    # deletele=(MobileBy.ID, 'com.tencent.wework:id/e3f')
    # surele=(MobileBy.ID, 'com.tencent.wework:id/bci')
    path ='../data/editinfo.yaml'
    def detele(self):
        # self.webdriver_wait(self.deletele)
        # self.find_click(self.deletele)
        # self.webdriver_wait(self.surele)
        # self.find_click(self.surele)
        self.steps(self.path, 'detele')
        from app.pgobject.screch import Screch
        return Screch(self.driver)
