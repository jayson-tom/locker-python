#coding=utf-8
import os
import xml.etree.ElementTree as ET
from selenium.common.exceptions import NoSuchElementException
import read_conf
from DRIVER import MyDriver


myapp_conf = read_conf.ReadConf()
element_path = myapp_conf.get_conf('other', 'element_path')
activity = {}

def set_xml():
	element_xml_path = os.path.join(element_path, 'element.xml')
	try:
		tree = ET.parse(element_xml_path)
		root = tree.getroot()
	except Exception, e:
		raise e
	all_element = root.findall('activity')

	for father_element in all_element:
		activity_name = father_element.get('name')
		element = {}

		for son_element in father_element.getchildren():
			element_name = son_element.get('name')
			element_child = {}

			for grandson in son_element.getchildren():
				element_child[grandson.tag] = grandson.text

			element[element_name] = element_child

		activity[activity_name] = element

def get_el_dict(activity_name, element_name):
	set_xml()
	element_dict = activity.get(activity_name).get(element_name)
	return element_dict


class Element(object):
	def __init__(self, activity_name, element_name):
		global driver
		driver = MyDriver.get_driver()
		self.activity_name = activity_name
		self.element_name = element_name
		element_dict = get_el_dict(self.activity_name, self.element_name)
		self.pathtype = element_dict['pathtype']
		self.pathvalue = element_dict['pathvalue']

	def is_exists(self):
		try:
			if self.pathtype == 'ID':
				driver.find_element_by_id(self.pathvalue)
				return True
			if self.pathtype == 'NAME':
				driver.find_element_by_name(self.pathvalue)
				return True
			if self.pathtype == 'CLASSNAME':
				driver.find_element_by_class_name(self.pathvalue)
				return True
			if self.pathtype == 'XPATH':
				driver.find_element_by_xpath(self.pathvalue)
				return True
		except NoSuchElementException:
			return False

	def get(self):
		try:
			if self.pathtype == 'ID':
				element = driver.find_element_by_id(self.pathvalue)
				return element
			if self.pathtype == 'NAME':
				element = driver.find_element_by_name(self.pathvalue)
				return element
			if self.pathtype == 'CLASSNAME':
				element = driver.find_element_by_class_name(self.pathvalue)
				return element
			if self.pathtype == 'XPATH':
				element = driver.find_element_by_xpath(self.pathvalue)
				return element
		except NoSuchElementException:
			return None


	def click(self):
		element = self.get()
		element.click()

		
if __name__ == '__main__':
	el = Element('SettingsActivity', 'Guide')
	el.is_exists()