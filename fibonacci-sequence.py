'''
INPUTS A NUMBER AND PROVIDES THE FIBONACCI SEQUENCE UP TO THAT NUMBER
'''

def fib_func(n):
    
    a = 0
    b = 1
    
    for i in range(n):
        a,b = b,b+a
        i = a + b
        yield i

n = int(input("Enter a number: "))

for x in fib_func(n):
    print(x)

input("Press ENTER to exit")