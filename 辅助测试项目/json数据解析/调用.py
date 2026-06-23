import utils

def 测试程序():
	# 准备测试数据
	数据 = [
		{"key": "a", "name": "苹果", "price": 5, "color": "红"},
		{"key": "b", "name": "香蕉", "price": 3, "color": "黄"},
		{"key": "c", "name": "橘子", "price": 4, "color": "橙"},
		{"key": "d", "name": "葡萄", "price": 6, "color": "紫", "season": "夏"}
	]

	解析器 = utils.对象数组解析器(数据)

	print("对象个数:",   len(解析器))
	print("共通属性:",   解析器.共通属性)   # 应包含 name, price, color
	print("所有属性:",   解析器.所有属性)   # name, price, color, season
	print("非共通属性:", 解析器.非共通属性) # season

	print("\n提取属性值('name'):", 解析器.提取属性值("name"))
	print("提取属性值('price'):",  解析器.提取属性值("price"))

	print("\n通过键访问:", 解析器["a"])

	print("\n所有对象:")
	for key, value in 解析器.items():
		print(f"  {key}: {value}")

	# 测试空数组情况
	空解析器 = utils.对象数组解析器([])
	print("\n空解析器长度:", len(空解析器))
	print("空解析器共通属性:", 空解析器.共通属性)

if __name__ == "__main__":
	测试程序()