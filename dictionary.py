marks={'hindi':80,'english':90}
print(marks)
print(type(marks))
print(marks['english'])


#print(marks["maths"])
print(marks.get("hindi"))

marks["maths"]=100    #value provide karna
print(marks)
print (marks.get("maths"))

del marks['hindi']
print(marks)