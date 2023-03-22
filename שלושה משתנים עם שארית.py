#קליטת 3 מספרים
num1 = int(input("enter number please: "))
num2 = int(input("enter number please: "))
num3 = int(input("enter number please: "))
#########
#הגדרת משתנים שיבדקו לנו אם התנאי התקיים
term1=False
term2=False
########מציאת המספר הגדול מבין ה3
if num1 >= num2 and num1 >= num3:
    big = num1
if num2 >= num1 and num2 >= num3:
    big = num2
if num3 >= num1 and num3 >= num2:
    big = num3
    
###########
#######מציאת המספר הכי קטן
if num1 <= num2 and num1 <= num3:
    small = num1
if num2 <= num1 and num2 <= num3:
    small = num2
if num3 <= num1 and num3 <= num2:
    small = num3 
    



##חישוב הסכום והממוצע
sum = num1+num2+num3
avg = float (sum/3)
###########תנאי ראשון
if sum % 2 == 0 and 100<sum:
    print(avg)
    term1 = True
##########תנאי שני
#print(int(avg))
if int (avg) % 2 == 0 or int (avg) % 3 == 0:
        print (big - small)
        term2=True
        
#if term1 and term2:
if term1 is True and term2 is True:
  print("conditions succeeded")    
        
        
    
    