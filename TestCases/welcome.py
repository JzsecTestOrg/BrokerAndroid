# -*- coding: utf-8 -*-
__author__ = 'xuwen1'

from Elements import welcomeElements
from CommonMethods import globalData, generateLog, Data
import time
from appium.webdriver.common.touch_action import TouchAction

def welcome(self, action):

    #校验欢迎页
    # try:
    #     el = welcomeElements.welcomePage(self)
    #     width = self.driver.get_window_size()['width']
    #     height = self.driver.get_window_size()['height']
    #     for i in range(1, 5):
    #         if(i == 1):
    #             globalData.LOG += generateLog.format_log('欢迎第' + str(i) + '页显示正确')
    #         # if(welcomeElements.welcome_title(self).get_attribute("name")  == Data.getValue('welcome', 'welcome', 'welcome_title', i)):
    #         #     globalData.LOG += generateLog.format_log("欢迎第" + str(i) + "页显示正确")
    #         # else:
    #         #     globalData.LOG += generateLog.format_log("欢迎第" + str(i) + "页显示错误: " + welcomeElements.welcome_title(self).get_attribute("name"))
    #         elif(i != 4):
    #             # TouchAction(self.driver).press(x=1000,y=500).move_to(x=50,y=500).release().perform()
    #             self.driver.execute_script("mobile: flick", {"direction": "right", "element": el.id})
    #             globalData.LOG += generateLog.format_log('欢迎第' + str(i + 1) + '页显示正确')
    # except:
    #     globalData.LOG += generateLog.format_log("欢迎页错误\n" + traceback.format_exc())


    #校验下一步操作
    try:
        if(action == 'login'):
            welcomeElements.welcome_login(self).click()
            globalData.LOG += generateLog.format_log("欢迎页面点击登录")
        elif(action == 'register'):
            welcomeElements.welcome_register(self).click()
            globalData.LOG += generateLog.format_log("欢迎页面点击注册")
    except:
        globalData.LOG += generateLog.format_log('欢迎页面下一操作错误')

def check_update(self):
    #校验版本更新
    try:
        time.sleep(2)
        el = welcomeElements.versionUpdate_alert(self)
        globalData.LOG += generateLog.format_log('提示版本更新')
        welcomeElements.versionUpdate_cancel(self).click()
        globalData.LOG += generateLog.format_log("取消版本更新")
    except Exception, e:
        globalData.LOG += generateLog.format_log("未提示版本更新,无需取消更新!")


