students = [['Jerry', 88], ['Justin', 84], ['Tom', 90], ['Akriti', 92], ['Harsh', 90]]
def second_highest(students):	
	grade = [s[1] for s in students] # 先把分數抓出來
	grade = sorted(grade, reverse=True) # 把分數這行列表由大到小排列
	second = grade[1] # 分數第二高的就在grade的第二格	
	second_student = [s[0] for s in students if s[1] == second]# 抓出兩高分數相同的'人名'
	for student in second_student:
		print(student)           


second_highest(students)