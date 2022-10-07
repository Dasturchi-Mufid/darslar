# 6! = 1*2*3*4*5*6 = 720

# m = list(range(15))
# print(m)

# n = 6
# sum = 1

# for i in range(1,n+1):
#     sum *= i
# print(sum)

# def factorial(m):
#     '''Bu rekursiv funksiya
#     kiritilgan son faktorialini topib beradi.'''
#     if m == 1:
#         return 1
#     else:
#         return(m * factorial(m-1))

# m = 6100

# print(f'{m}!(faktorial) = {factorial(m)}')

def recursion():
    print(1,end='')
    recursion()

recursion()