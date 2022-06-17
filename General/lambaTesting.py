lowerLimit=int(input("Enter a range of numbers\nEnter lower limit: "))
upperLimit=int(input("Enter the upper limit: "))
g = lambda a: print(str(a)+": "+str(a*a)) if a%2==0 else print(a)
for i in range(upperLimit-lowerLimit):
	g(lowerLimit+i)
