def sum_f(arg1, arg2):
    c = arg1 + arg2
    print(c)

    
a = int(input("Enter a: "))
b = int(input("Enter b: "))

sum_f(a, b)


def sum_a(a, b):
    return a + b

num = sum_a(5, 10)

print(num)

def sum_a(a, b):
    if type(a) == type(b):
        return a + b
    else:
        return "Not same"
    
x = sum_a("ADA", 12)
print(x)

def shop(item, price=30):
    print("Item:", item)
    print("Price:", price)

shop(price=50, item="Rice")

def std(name, cls, *marks):
    print("Name:", name)
    print("Class:", cls)
    print("Marks:", marks)

std("XYZ", 10, 30, 20, 51)

def std(name, cls, *marks):
    print("Name:", name)
    print("Class:", cls)
    #print("Marks:", marks)

    for x in marks:
        print("Marks", x)

std("XYZ", 10, 30, 20, 51)

def std(name, cls, **marks):
    print("Name:", name)
    print("Class:", cls)
    print("Marks:", marks)

    #for x in marks:
     #   print("Marks", x)

std("XYZ", cls=10, English=30, maths=20, science=51)

def std(name, cls, **marks):
    print("Name:", name)
    print("Class:", cls)
    #print("Marks:", marks)

    for x, y in marks.items():
       print(x + " marks: ", y)

std("XYZ", cls=10, English=30, maths=20, science=51)