num1 = int(input("enter number please: "))
num2 = int(input("enter number please: "))
num3 = int(input("enter number please: "))

if num1 >= num2 and num1 >= num3:
    big = num1
if num2 >= num1 and num2 >= num3:
    big = num2
if num3 >= num1 and num3 >= num2:
    big = num3
    
    
print(big)


if num1 <= num2 and num1 <= num3:
    small = num1
if num2 <= num1 and num2 <= num3:
    small = num2
if num3 <= num1 and num3 <= num2:
    small = num3
    
print(small)
    
    
    
