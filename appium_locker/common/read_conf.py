import os
import sys
import ConfigParser

# path = sys.path[0]
# path_appium = path + '/common/myapp.conf'
path_appium = '/Users/tom/python/Appium/appium_locker/common/myapp.conf'


class ReadConf(object):
	"""read the configuration file"""

	def __init__(self):
		self.cp = ConfigParser.SafeConfigParser()
		self.cp.read(path_appium)

	def get_conf(self, section, name):
		value = self.cp.get(section, name)
		return value