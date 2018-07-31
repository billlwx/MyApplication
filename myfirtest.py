#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# __author__ = 'bill'
# create on 1018/7/17
import ConfigParser
import os
import socket
import unittest
from time import sleep
import time

import HTMLTestRunner
import setup
import swipe

class mytest(unittest.TestCase):
    # 进入欢迎页面
    def test_welcome(self):
        # 向左滑动1次
        swipe.swipLeft(1000)
        sleep(1)
        swipe.swipLeft(1000)
        sleep(1)
        # 点击立即体验
        setup.driver.find_element_by_id('com.qianjinjin.android:id/clickView').click()
        sleep(1)
    # 登录
    def test_login(self):
        # 刷新一下
        swipe.swipeDown(500)
        sleep(1)
        # 打开左侧栏
        swipe.swipRight(500)
        sleep(1)
        # 点击登录组件
        setup.driver.find_element_by_id('com.qianjinjin.android:id/gotologin_tv').click()
        # 读取配置文件
        conf = ConfigParser.SafeConfigParser()
        conf.read("user.ini")
        # 输入账户密码登录
        setup.driver.find_element_by_id('com.qianjinjin.android:id/mobileInput').send_keys(conf.get("user", "phone"))
        sleep(1)
        setup.driver.find_element_by_id('com.qianjinjin.android:id/pwdInput').send_keys(conf.get("user", "password"))
        setup.driver.find_element_by_id('com.qianjinjin.android:id/loginBtn').click()
        sleep(1)
        # 可能如果没有广告，需要 try 一下
        try:
            setup.driver.find_element_by_id('com.qianjinjin.android:id/msg_adv_close').click()
        except:
            print '没有广告'
            pass

    # 借款
    def test_load(self):
        setup.driver.find_element_by_id('com.qianjinjin.android:id/agreeIv').click()
        sleep(1)
        setup.driver.find_element_by_id('com.qianjinjin.android:id/actionBtn').click()
        sleep(1)
        # 可能已经有权限，需要 try 一下
        try:
            setup.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
        except:
            print 'failed'
            pass
        sleep(1)
        setup.driver.find_element_by_id('com.qianjinjin.android:id/actionBtn').click()
        sleep(60)
        # 刷新一下
        swipe.swipeDown(500)
        sleep(1)

    def test_repay(self):
        setup.driver.find_element_by_id('com.qianjinjin.android:id/actionBtn').click()
        sleep(1)
        setup.driver.find_element_by_id('com.qianjinjin.android:id/actionBtn').click()
        sleep(1)
        setup.driver.find_element_by_id('com.qianjinjin.android:id/payMethodRl').click()
        sleep(1)
        setup.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout').click()
        sleep(1)
        setup.driver.find_element_by_id('com.qianjinjin.android:id/actionBtn').click()
        sleep(1)
        setup.driver.find_element_by_id('com.qianjinjin.android:id/verifyCodeInput').send_keys('1')
        sleep(1)
        setup.driver.find_element_by_id('com.qianjinjin.android:id/payBtn').click()
        sleep(1)

    # 退出
    def test_logout(self):
        # 打开左侧栏
        swipe.swipRight(500)
        sleep(1)
        # 点击设置,菜单还是用find_element_by_xpath比较好
        setup.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[6]/android.widget.TextView').click()
        # setup.driver.find_element_by_id('com.qianjinjin.android:id/itemDesc').click()
        sleep(1)
        # 点击退出按钮
        setup.driver.find_element_by_id('com.qianjinjin.android:id/logoutBtn').click()
        sleep(1)
        # 点击确认
        setup.driver.find_element_by_id('com.qianjinjin.android:id/confirm_btn').click()
        sleep(1)

if __name__ == "__main__":
    # 此用法可以同时测试多个类
    suite = unittest.TestSuite()
    # suite.addTest(mytest("test_welcome"))
    suite.addTest(mytest("test_login"))
    # suite.addTest(mytest("test_load"))
    # suite.addTest(mytest("test_repay"))
    suite.addTest(mytest("test_logout"))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    # 获取当前时间，这样便于下面的使用。
    Nowtime = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    workpath = os.getcwd()
    filename = Nowtime + socket.gethostname() + ".html"
    reportPath = workpath + "/report/" + Nowtime + ".html"
    # 打开一个文件，将result写入此file中
    fp = file(reportPath, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况：')
    runner.run(suite)
    fp.close()