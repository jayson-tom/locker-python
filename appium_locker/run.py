import os
import HTMLTestRunner
from appium import webdriver
import unittest
import appium_server
from time import sleep
from common.DRIVER import MyDriver
from common.init_device import InitDevice
from common.read_conf import ReadConf

r_conf = ReadConf()


class AllTest(object):
	"""run the test case"""

	def __init__(self):
		self.case_list = []
		self.casesuit_list = []
		self.case_path = r_conf.get_conf('other', 'caselist_path')
		self.caselist_path = os.path.join(r_conf.get_conf('other', 'caselist_path'), 'case_list.txt')
		self.test_result_path = os.path.join(r_conf.get_conf('other', 'test_result_path'), 'result.log')
		self.my_server = appium_server.AppiumServer()

		self.driver = self.driver_on()

	def driver_on(self):
		MyDriver.get_driver()

	def driver_off(self):
		MyDriver.get_driver().quit()

	def get_caselist(self):
		fp = open(self.caselist_path)

		for line in fp.readlines():
			s_data = str(line)
			if s_data != '' and not s_data.startswith('#'):
				self.case_list.append(s_data.strip('\r\n'))

		fp.close()

	def create_suite(self):
		self.get_caselist()
		test_suite = unittest.TestSuite()

		for case in self.case_list:
			discover = unittest.defaultTestLoader.discover(self.case_path, pattern=case+'.py', top_level_dir=None)
			self.casesuit_list.append(discover)

		if len(self.casesuit_list) > 0:

			for case_suit in self.casesuit_list:
				for test_case in case_suit:
					test_suite.addTest(test_case)

		else:
			test_suite = None

		return test_suite

	def run(self):
		try:
			self.my_server.start_server()
			while not self.my_server.is_running():
				sleep(1)

			suit = self.create_suite()
			print suit

			fp = open(self.test_result_path, 'wb')
			print self.test_result_path
			runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='testReport', description='Report_description')
			runner.run(suit)
			# unittest.TextTestRunner(verbosity=2).run(suit)

		except Exception, e:
			print e
		finally:
			self.driver_off()
			self.my_server.stop_server()


if __name__ == '__main__':
	obj = AllTest()
	obj.run()