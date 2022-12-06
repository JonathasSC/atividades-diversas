def gradingStudents(grades):
	nova_grade = []
	for grade in grades:
		if grade >= 38 and grade % 5 >=3:
			print(grade % 5)
			nova_grade.append(grade+(5-grade%5))
		else:
			nova_grade.append(grade)
	return nova_grade

print(gradingStudents([78,67,38,33]))