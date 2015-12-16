import unittest
import sys
import time
sys.path.append('../')
from common.DRIVER import MyDriver
from common.common import Element


class Test01(unittest.TestCase):

	def setUp(self):
		self.driver = MyDriver.get_driver()

	def test_case01(self):
		# el = self.driver.find_element_by_name('Help')
		# el.click()
		if Element('SettingsActivity', 'App').is_exists():
			Element('SettingsActivity', 'App').click()
		time.sleep(1)

	def test_case02(self):
		if Element('SettingsActivity', 'Home').is_exists():
			Element('SettingsActivity', 'Home').click()
		time.sleep(1)

	def test_case03(self):
		if Element('SettingsActivity', 'Wallpaper').is_exists():
			Element('SettingsActivity', 'Wallpaper').click()
		time.sleep(1)

	def test_case04(self):
		if Element('SettingsActivity', 'Style').is_exists():
			Element('SettingsActivity', 'Style').click()
		time.sleep(1)

	def test_case04(self):
		if Element('SettingsActivity', 'Security').is_exists():
			Element('SettingsActivity', 'Security').click()
		time.sleep(1)

	def tearDown(self):
		pass