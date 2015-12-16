import init_device
import threading
from time import sleep
from appium import webdriver
from urllib2 import URLError
from selenium.common.exceptions import WebDriverException
import read_conf
conf = read_conf.ReadConf()


class MyDriver(object):

	driver = None
	mutex = threading.Lock()

	my_init = init_device.InitDevice()
	platform_name = conf.get_conf('config', 'platform_name')
	platform_version = my_init.get_android_version()
	package_name = conf.get_conf('config', 'package_name')
	main_activity = conf.get_conf('config', 'main_activity')
	device_name = my_init.get_devicename()
	base_url = conf.get_conf('config', 'base_url')

	desired_caps = {"platformName":platform_name, "platformVersion":platform_version, "appPackage":package_name, "appActivity":main_activity, "deviceName":device_name}

	def __init__(self):
		pass

	@staticmethod
	def get_driver():
		try:
			if MyDriver.driver is None:
				MyDriver.mutex.acquire()
				if MyDriver.driver is None:
					try:
						MyDriver.driver = webdriver.Remote(MyDriver.base_url, MyDriver.desired_caps)
					except URLError, e:
						MyDriver.driver = None

				MyDriver.mutex.release()

			return MyDriver.driver
		except WebDriverException:
			raise
		
		
# my_init = init_device.InitDevice()
# platform_name = init_device.platform_name
# print platform_name
# aa = MyDriver()
# aa.get_driver()
# print conf.get_conf('config', 'platform_name')
