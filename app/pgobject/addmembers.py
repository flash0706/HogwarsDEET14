from app.pgobject.addmanualmem import Addmanualmem
from app.pgobject.pagebase import Pagebase
from appium.webdriver.common.mobileby import MobileBy

'''
        添加成员页page
'''

class Addmembers(Pagebase):
    '''
            点击通讯手动添加成员，返回手动添加页面page
    '''
    path = '../data/addmembers.yaml'
    def add_manually(self):
        self.steps(self.path, 'add_manually')
        # eleadd_manually =(MobileBy.ID, "com.tencent.wework:id/cq6")
        # self.webdriver_wait(eleadd_manually)
        # self.find_click(eleadd_manually)
        return Addmanualmem(self.driver)



