name="hello i am neha singh"
grade='A'
salary=356787
print(type(salary))
#typecasting convert datatype into another
salary=str(356787) 
print(type(salary))
print(name+grade+salary)
#print(grade)
#print(salary)
salary=float(356787)
print(type(salary))
a=input("enter your current year")
b=input("enter your born year")
print(type(a-b))
#input default return type is string 
bornyear=int(input("enter born year:"))
currentyear=int(input("enter current year"))
ageinyear=currentyear-bornyear
print("my age is",(currentyear-bornyear))
print("my age is:"(int("enter current year")-int("enter bornyear")))
