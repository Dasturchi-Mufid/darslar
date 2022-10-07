# def double(m):
#     return m * 2

# doubles = lambda x,y: x + y

# print(double(5))
# print(doubles(10,5))

# x = 5

# def good():
#     global x
#     x = 10
#     print("local x:", x)


# good()
# print("global x:", x)

x = 'global'

def outter():
    x = 'local'
    # global x
    print(x)
    def inner():
        # nonlocal x
        x = 'nonlocal'
        print(x)
    inner()

print(x)
outter()

