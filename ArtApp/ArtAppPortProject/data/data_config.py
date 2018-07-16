#coding:utf-8
class global_var:
	Id = '1'                 # id
	request_name = '2'       # 接口名称
	prefix_url = '3'         # 获取地址前缀
	request_url = '4'        # 获取请求地址
	request_way = '5'        # 获取请求方法
	request_format = '6'
	request_data = '7'
	check_point = '8'
	data_depend = '9'
	is_run = '10'
	result = '11'
	response_data = '12'
	response_time = '13'

# 获取caseid
def get_id():
	return global_var.Id

# 接口名称
def get_request_name():
	return global_var.request_name

# 获取地址前缀
def get_prefix_url():
	return global_var.prefix_url

# 获取请求地址
def get_request_url():
	return global_var.request_url

# 获取请求方法
def get_request_way():
	return global_var.request_way

# 获取请求格式
def get_request_format():
	return global_var.request_format

# 获取请求数据
def get_request_data():
	return global_var.request_data

# 获取检查点
def get_check_point():
	return global_var.check_point

# 获取关联参数
def get_data_depend():
	return global_var.data_depend

# 获取是否运行
def get_is_run():
	return global_var.is_run

# 获取测试结果
def get_result():
	return global_var.result

# 获取响应数据
def get_response_data():
	return global_var.response_data

# 获取响应时间
def get_response_time():
	return global_var.response_time
