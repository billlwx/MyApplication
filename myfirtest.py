#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# __author__ = 'bill'
# create on 2018/7/27
import ConfigParser
import unittest
from time import sleep

import setup
import swipe

class mytest(unittest.TestCase):
    # 进入欢迎页面
    def test_welcome(self):
        # 向左滑动2次
        swipe.swipLeft(1000)
        sleep(3)
        swipe.swipLeft(1000)
        sleep(3)
        # 点击立即体验
        setup.driver.find_element_by_id('com.qianjinjin.android:id/clickView').click()
        sleep(3)
    # 登录
    def test_login(self):
        # 刷新一下
        swipe.swipeDown(500)
        sleep(3)
        # 打开左侧栏
        swipe.swipRight(500)
        sleep(3)
        # 点击登录组件
        setup.driver.find_element_by_id('com.qianjinjin.android:id/gotologin_tv').click()
        # 读取配置文件
        conf = ConfigParser.SafeConfigParser()
        conf.read("user.ini")
        # 输入账户密码登录
        setup.driver.find_element_by_id('com.qianjinjin.android:id/mobileInput').send_keys(conf.get("user", "phone"))
        sleep(3)
        setup.driver.find_element_by_id('com.qianjinjin.android:id/pwdInput').send_keys(conf.get("user", "password"))
        setup.driver.find_element_by_id('com.qianjinjin.android:id/loginBtn').click()
        sleep(3)
        # 可能如果没有广告，需要 try 一下
        try:
            setup.driver.find_element_by_id('com.qianjinjin.android:id/msg_adv_close').click()
        except:
            print 'failed'
            pass

    def test_logout(self):
        swipe.swipRight(500)
        sleep(3)
        setup.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[6]/android.widget.TextView').click()
        # setup.driver.find_element_by_id('com.qianjinjin.android:id/itemDesc').click()
        sleep(3)
        setup.driver.find_element_by_id('com.qianjinjin.android:id/logoutBtn').click()
        sleep(3)
        # setup.driver.find_element_by_id('com.qianjinjin.android:id/actionBtn').click()
        # sleep(3)

if __name__ == "__main__":
    # 此用法可以同时测试多个类
    suite = unittest.TestSuite()
    suite.addTest(mytest("test_welcome"))
    suite.addTest(mytest("test_login"))
    suite.addTest(mytest("test_logout"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
