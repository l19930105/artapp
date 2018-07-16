#coding:utf-8

import sys
sys.path.append('E:/PycharmProjects/SeleniumTest/PythonWork/ArtApp/ArtAppPortProject')

from PortCommons import opera_excel
from data import data_config
from PortCommons import read_init

class GetData:
	def __init__(self):
		# 存放的用例
		# test_path = r'E:\PycharmProjects\SeleniumTest\PythonWork\ArtApp\ArtAppPortProject\testcase\testcase_APP.xlsx'
		# 优化为获取testcase文件夹下的用例 - 相对路径
		test_path = "../testcase/testcase_APP.xlsx"
		# 表格用例名
		sheet_name =  'V4.9.5'
		self.opera_excel = opera_excel.OperateExcel(test_path, sheet_name)

	# 去获取excel行数,就是我们的case个数
	def get_case_lines(self):
		return self.opera_excel.get_max_row()

	# 获取caseID
	def get_id(self,row):
		col = int(data_config.get_id())
		caseID = self.opera_excel.get_value(row,col)
		return caseID

	# 获取接口名称
	def get_request_name(self,row):
		col = int(data_config.get_request_name())
		request_name = self.opera_excel.get_value(row,col)
		return request_name

	# 获取地址前缀
	def get_prefix_url(self,row):
		col = int(data_config.get_prefix_url())

		# 给地址前缀赋值为测试环境的地址 --->具体环境配置请看config.ini文件
		# oAddress-->生产环境    tAddress-->测试环境
		read_ini = read_init.ReadIni()
		address = read_ini.get_value("tAddress", "testAress")
		self.opera_excel.set_value(row,col,address)

		prefix_url = self.opera_excel.get_value(row,col)
		return prefix_url

	# 获取请求地址
	def get_request_url(self,row):
		col = int(data_config.get_request_url())
		request_url = self.opera_excel.get_value(row,col)
		return request_url

	# 获取请求方法
	def get_request_method(self,row):
		col = int(data_config.get_request_way())
		request_method = self.opera_excel.get_value(row,col)
		return request_method

	# 获取请求格式
	def get_request_format(self,row):
		col = int(data_config.get_request_format())
		request_format = self.opera_excel.get_value(row,col)
		return request_format

	# 获取请求数据
	def get_request_data(self,row):
		col = int(data_config.get_request_data())
		data = self.opera_excel.get_value(row,col)
		if data == '':
			return None
		return data

	# 获取是否有检查点
	def get_check_point(self,row):
		col = int(data_config.get_check_point())
		check_point = self.opera_excel.get_value(row,col)
		if check_point != '':
			return check_point
		else:
			return None

	# 获取是否关联参数
	def get_data_depend(self,row):
		col = int(data_config.get_data_depend())
		data_depend = self.opera_excel.get_value(row,col)
		if data_depend != '':
			return data_depend
		else:
			return None

	# 获取是否执行
	def get_is_run(self,row):
		flag = None
		col = int(data_config.get_is_run())
		run_model = self.opera_excel.get_value(row,col)
		if run_model == 'Yes':
			flag = True
		else:
			flag = False
		return flag

	# 写入测试结果
	def write_result(self,row,value):
		col = int(data_config.get_result())
		self.opera_excel.set_value(row,col,value)
		Result = self.opera_excel.get_value(row, col)
		return Result

	# 写入响应数据
	def write_response_data(self,row,value):
		col = int(data_config.get_response_data())
		self.opera_excel.set_value(row,col,value)
		response_data = self.opera_excel.get_value(row, col)
		return response_data

	# 写入响应时间
	def write_response_time(self,row,value):
		col = int(data_config.get_response_time())
		self.opera_excel.set_value(row,col,value)
		response_time = self.opera_excel.get_value(row, col)
		return response_time


	# 是否携带header
	def is_header(self,row):
		col = int(data_config.get_header())
		header = self.opera_excel.get_cell(row,col)
		if header != '':
			return header
		else:
			return None


	# #通过获取关键字拿到data数据
	# def get_data_for_json(self,row):
	# 	opera_json = OperetionJson()
	# 	request_data = opera_json.get_data(self.get_request_data(row))
	# 	return request_data



if __name__ == '__main__':
	get_data = GetData()
	# 确认是第2行数据
	row = 2

	caseNum = get_data.get_case_lines()-1
	print("用例数为： " + str(caseNum))

	caseID = get_data.get_id(row)
	print("caseID为： " + str(caseID))

	request_name = get_data.get_request_name(row)
	print("接口名称为： " + str(request_name))

	prefix_url = get_data.get_prefix_url(row)
	print("接口前缀为： " + str(prefix_url))

	request_url = get_data.get_request_url(row)
	print("请求地址为： " + str(request_url))

	request_method = get_data.get_request_method(row)
	print("请求方法为： " + str(request_method))

	request_format = get_data.get_request_format(row)
	print("请求格式为： " + str(request_format))

	request_data = get_data.get_request_data(row)
	print("请求数据为： " + str(request_data))

	check_point = get_data.get_check_point(row)
	print("检查点为： " + str(check_point))

	data_depend = get_data.get_data_depend(row)
	print("关联参数为： " + str(data_depend))

	flagResult = get_data.get_is_run(row)
	print("是否运行： " + str(flagResult))

	result = "成功"
	getresult = get_data.write_result(row, result)
	print("测试结果为： " + str(getresult))

	response_data = "响应数据测试"
	get_response_data = get_data.write_response_data(row, response_data)
	print("响应数据为： " + str(get_response_data))

	response_time = "0.2s"
	get_response_time = get_data.write_response_time(row, response_time)
	print("响应数据为： " + str(get_response_time))