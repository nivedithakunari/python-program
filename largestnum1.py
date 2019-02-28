#python program to find the largest number among three input numbers

#change the values of num1,num2,num3
#for different result
num1=10
num2=14
num3=12

#uncomment following lines to take three numbers from user
num1=float(input("enter the first number: "))
num2=float(input("enter the second number: "))
num3=float(input("enter the third number: "))

if (num1>=num2) and (num1>=num3):
	largest = num1
elif (num2>=num1) and (num2>=num3):
	largest = num2
else:
	largest = num3

print("the largest number between",num1,",",num2,"and",num3,"is",largest)
