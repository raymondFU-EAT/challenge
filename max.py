def max_num(list_num):
	if not list_num: # 了解空單是否為空
		return 0     # 是空的話回傳0
	max = list_num[0] # 先把最大值設定在列表第1格
	for num in list_num: # 把list_num中的num一個個拿出來
		if num > max: # 如果列出的num>列表第一格的最大值
			max = num # 那就把最大值變成此數
	return max # 回傳最大值


max_num = max_num([5, 66, -985])
print(max_num)
