def kangaroo(x1, v1, x2, v2):
	try:
		r = (x2-x1) % (v1-v2)
		d = (x2-x1) / (v1-v2)
		print(r)
		print(d)
	except(ZeroDivisionError):
		return "NO"

	if r == 0 and d > 0:
		return "YES"
	else:
		return "NO"
kangaroo(0,2,5,3)