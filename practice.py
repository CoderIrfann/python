# # # factorial number
# # a = int(input("Enter your number : "))
# #
# # factorial = 1
# #
# # for x in range(11):
# #     factorial =a* x
# #
# #     print("The factorial is : " , factorial)
# #
# #
# # check number is positive or not
#
# num1 = int(input("Enter your number :"))
#
# if(num1 % 2 == 0):
#     print(num1," ,Is positive")
# else:
#     print(num1 ," ,Is Negative")

# Simple calculator
num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))

# Calculator logic operation
sum = num1+num2
sub = num1-num2
multiply = num1*num2
divide = num1%num2
power = num1**num2

# printing the operation
print("Addition of",num1 , "+" , num2 , "is :" , sum)
print("Subtraction of",num1 , "-" , num2 , "is :" , sub)
print("Multiplication of",num1 , "*" , num2 , "is :" , multiply)
print("Division of",num1 , "%" , num2 , "is :" , divide)
print("Power of",num1 , "**" , num2 , "is :" , power)
