###Taking Input Changing for Git
exp= raw_input("Please enter the expression ")
try :
	res= eval(exp+'.0')
	print "The result is "+str(res)
except SyntaxError:
	print "Error: Invalid Expression"


