# coding=utf-8
import configparser
import os
'''
获取配置文件中的测试地址
从而判断是测试环境还是生产环境
可以优化接口测试用例的地址前缀，实现测试地址的任意切换
'''
class ReadIni:
	def __init__(self,file_path=None):
		if file_path == None:
			# 获取当前文件夹的父目录绝对路径
			BaseDir = os.path.dirname(os.path.dirname(__file__))
			# 配置文件地址
			self.file_path = os.path.join(BaseDir, 'config', 'config.ini')
		else:
			self.file_path = file_path
		self.data = self.read_ini()

	def read_ini(self):
		read_ini = configparser.ConfigParser()
		read_ini.read(self.file_path)
		return read_ini

	#通过key获取对应的value
	def get_value(self,key,address=None):
		if address == None:
			address = 'testAress'
		try:
			value = self.data.get(address,key)
		except:
			value = None  # 捕获异常没有传值就返回None
		return value

if __name__ == '__main__':
	read_ini = ReadIni()
	address = read_ini.get_value("tAddress","testAress")
	print(address)
	if "ceshi" in address:
		print("这是测试环境地址： %s " %address)
	else:
		print("这是生产环境地址： %s " %address)