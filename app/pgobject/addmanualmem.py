from app.pgobject.pagebase import Pagebase
from appium.webdriver.common.mobileby import MobileBy


'''
        手动添加页面page
'''
class Addmanualmem(Pagebase):

    # 添加姓名
    def add_name(self, name):
        self.find_sendkey((MobileBy.XPATH,
                    "//*[contains(@text, '姓名')]/../*[@class='android.widget.EditText']"), name)
        return self



    # 添加电话
    def add_mobynum(self, num):
        self.find_sendkey((MobileBy.ID,
                           "com.tencent.wework:id/f1e"), num)
        return self


    # 添加性别
    def add_gender(self, gender):
        self.find_click((MobileBy.XPATH,
                    "//*[contains(@text, '性别')]/../*[@class='android.widget.RelativeLayout']"))
        if str(gender) == '男':
            self.find_click((MobileBy.XPATH, "//*[@text='男']"))
        else:
            self.find_click((MobileBy.XPATH, "//*[@text='女']"))
        return self


        '''
            点击保存，返回添加成员页page
        '''
    def save(self):
        from app.pgobject.addmembers import Addmembers
        self.find_click((MobileBy.ID, "com.tencent.wework:id/h9w"))
        return Addmembers(self.driver)


