#!/usr/bin/env python
# -*- coding:utf-8 -*-

#导入webdriver API对象，可以调用浏览器和操作页面
from selenium import webdriver
#导入Keys,可以使用操作键盘、标签、鼠标
from selenium.webdriver.common.keys import Keys

#创建PhantomJS浏览器对象
driver = webdriver.PhantomJS()

driver.get("https://www.douban.com/")

driver.save_screenshot("douban.png")

driver.find_element_by_name("form_email").send_keys("mr.mao.tony@gmail.com")
driver.find_element_by_name("form_password").send_keys("Mzj60055969alarm")
driver.find_element_by_id("captcha_field").send_keys("produce")
driver.save_screenshot("douban.png")
driver.find_element_by_class_name("bn-submit").click()
driver.save_screenshot("douban.png")

driver.get("https://www.douyu.com/directory/all")
driver.page_source
driver.page_source.find("shark-pager-disable-next")




