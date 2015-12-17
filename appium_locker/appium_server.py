import os
import sys
import threading
import urllib2
from urllib2 import URLError
import time
import common.read_conf as read_conf

rc = read_conf.ReadConf()

class AppiumServer(object):
	"""operation for AppiumServer"""

	def __init__(self):
		self.appium_path = rc.get_conf('config', 'appium_path')
		self.base_url = rc.get_conf('config', 'base_url')
		self.cmd = 'node ' + self.appium_path + ' &'

	def run_appium_server(self):
		os.system(self.cmd)

	def start_server(self):
		t = threading.Thread(target=self.run_appium_server)
		t.start()
		t.join()
		time.sleep(5)

	def stop_server(self):
		os.system('pkill node')

	def restart_server(self):
		self.stop_server()
		self.start_server()

	def is_running(self):
		url = self.base_url + '/status'
		response = None
		try:
			request = urllib2.Request(url)
			response = urllib2.urlopen(request, timeout=5)
			if response.getcode() == 200:
				return True
		except URLError:
			return False
		finally:
			if response:
				response.close()
		

# if __name__ == '__main__':
# appium_server = AppiumServer()
# appium_server.start_server()