x = 10    # Gobal variable 
y = 20    #global variable

def sum_f(x, y):
    print(x)
    print(y)
    
    z = 50 #local variable
    print(z)
sum_f(x, y)
print("-------")
print(x)
print(y)

