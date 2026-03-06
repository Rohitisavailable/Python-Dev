# a[start:end]    # items start through end-1
# a[start:]       # items start through the rest of the array
# a[:end]         # items from the beginning through end-1
# a[:]            # a copy of the whole array
# a[start:end:step] # start through not past end, by step

x = [100, 200, 300, 400, 500, 600, 700]
#     0    1    2    3    4    5    6
#    -7   -6   -5   -4   -3   -2   -1
y = (10, 20, 30, 40, 50, 60, 70)
#    0    1   2   3   4   5   6
#    -7  -6  -5  -4  -3  -2  -1  
z ="Python"

print(x[0:3:])
print(x[0:])
print(x[3:])
print(x[:6])
print(x[::2])
print(x[::-1]) #reversed
print(x[-3::])
print(x[:-3:])
print(x[:-3:2])
print(x[-3::2])
print(z[0::2])