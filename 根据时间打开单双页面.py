# -*- coding: utf-8 -*-
import os
import time
from pywinauto import application
import datetime

class Browser(object):
    """
       pywin framwork main class
       tool_name : 程序名称，支持带路径
       windows_name : 窗口名字
       """
    SLEEP_TIME = 1

    def __init__(self):
        """
        初始化方法，初始化一个app
        """
        self.app = application.Application()

    def run(self, tool_name):
        """
        启动应用程序
        """
        self.app.start(tool_name)
        time.sleep(1)
    def run(self,appCmd,appX,appY,appW,appH,dir):
        position = " --window-position="+str(appX)+","+str(appY)
        size = " --window-size=" + str(appW) + "," + str(appH)
        tmpDir = "C:/temp/Chrome/"+str(dir)
        userDir = " --user-data-dir="+tmpDir
        self.app.start(appCmd+position+size+userDir)
    def close(self):
        os.system(f"taskkill /t /f /im chrome.exe")
        time.sleep(1)

    
    def single(self):
        pass

    
    def double(self):
        pass



    
if __name__ ==  "__main__":

    #打开浏览器的页面
    browser = Browser()
    browser.run(r"C:\Program Files\Google\Chrome\Application\chrome.exe --kiosk www.baidu.com",0,0,1920,1080,3)
    
    time.sleep(4)
    browser.close()


    from datetime import datetime
    dt = datetime.today()
    print(str(dt.year) +"-" + str(dt.month) +"-"+ str(dt.day) + " " + str(dt.hour) +":"+ str(dt.minute)+":" +str(dt.second) +":"+ str(dt.microsecond))


    while True:

        time.sleep(1)

        if (dt.month == 9 and dt.day == 9 and dt.hour == 17 and dt.minute ==0):
            print("单页面")
            pass
            #打开单领导页面
        else:
            print("双页面")
            #打开多领导页面
            pass
        

