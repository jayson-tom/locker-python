import read_conf
import os

rc = read_conf.ReadConf()


class InitDevice(object):
	"""operation of Device"""

	def __init__(self):
		global view_phone, view_android, start_server, close_server, check_phone, install_apk, uninstall_apk, package_path 
		view_phone = rc.get_conf('cmd', 'view_phone')
		view_android = rc.get_conf('cmd', 'view_android')
		start_server = rc.get_conf('cmd', 'start_server')
		close_server = rc.get_conf('cmd', 'close_server')
		check_phone = rc.get_conf('cmd', 'check_phone')
		install_apk = rc.get_conf('cmd', 'install_apk')
		uninstall_apk = rc.get_conf('cmd', 'uninstall_apk')
		package_path = rc.get_conf('config', 'package_path')

	def connect_phone(self):
		status = os.popen(check_phone)

		for s_data in status.readline():
			if s_data.find('devices'):
				return True
			else:
				return False

	def get_devicename(self):
		name = os.popen(view_phone)
		for line in name.readlines():
			if line.find('device') and (not line.startswith('List')):
				line = (line.replace('device','')).strip()
				return line


	def get_android_version(self):
		version = os.popen(view_android)
		for line in version.readlines():
			if line.startswith('ro.build.version'):
				line = line.split('=')
				return line[-1].strip('\r\n')

	def start_adb_server(self):
		os.system(start_server)

	def close_adb_server(self):
		os.system(close_server)

	def restart_adb_server(self):
		self.close_adb_server()
		self.start_adb_server()

	def install(self):
		return True
		file_path = package_path + '/' + self.get_apk()
		cmd = install_apk + ' ' + file_path
		status = os.popen(cmd)
		for line in status.readlines():
			if line.find('Success'):
				return True
		else:
			return False


	def uninstall(self):
		status = os.popen(uninstall_apk)
		for line in status.readlines():
			if line.find('Success'):
				return True
		else:
			return False

	def get_apk(self):
		file_names = os.listdir(package_path)
		for f in file_names:
			if f.split('.')[-1] == 'apk':
				basename = os.path.basename(f)
				return basename

# if __name__ == '__main__':
# 	init_device = InitDevice()
# 	print view_android, start_server, close_server, check_phone, install_apk, uninstall_apk, package_path
# 	print init_device.connect_phone()
# 	print init_device.get_devicename()
# 	init_device.get_android_version()
# 	init_device.install()

