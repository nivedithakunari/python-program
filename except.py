try:
	l=[1,2,3,4]
	a=int(input("enter a number"))
	if a>5:
		raise NameError
	else:
		print(l)
		raise TypeError
except NameError:
	print("name error")
except TypeError:
	print("type error")
finally:
	print("execution completed")



