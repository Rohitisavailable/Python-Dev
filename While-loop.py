"""x = 0 

while x < 6:
    print("Cureent value of x", x)
    x = x + 1 
else:
    print("Loop complete")

x = 0

while x < 999:
    print("current value of x", x)
    x = x + 1 """


num = 1 

sum = 0

print("Enter number for sum, Press '0' to exit")

while num !=0 :
    num = int(input("Enter No.: "))

    sum = sum + num
    print("Current Sum:", sum)

else:
    print("COmpleted")