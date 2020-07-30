from appium import webdriver

from app.pgobject.mainActivity import MainActivity
from app.pgobject.pagebase import Pagebase
'''
app启动类
'''

class App(Pagebase):
    '''
    开启driver
    '''

    def start(self):
        if self.driver == None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = "com.tencent.wework.launch.WwMainActivity"
            caps["noReset"] = "true"
            caps['skipServerInstallation'] = 'true'  # 跳过 uiautomator2 server的安装
            caps['skipDeviceInitialization'] = 'true'  # 跳过设备初始化
            # caps['dontStopAppOnReset'] = 'true'    # 启动之前不停止app
            caps['settings[waitForIdleTimeout]'] = 0

            # 与server 建立连接,初始化一个driver 创建session,返回一个sessionid
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            # launch_app() 这个方法不需要传入任何参数， 会自动启动起来DesireCapa里面定义的activity
            # start_activity(packagename, activityname) 可以启动其它的应用的页面
            self.driver.launch_app()
        self.driver.implicitly_wait(20)
        return self

    def stop(self):
        self.driver.quit()

    '''
    返回主页page
    '''
    def go_MainActivity(self):
        return MainActivity(self.driver)