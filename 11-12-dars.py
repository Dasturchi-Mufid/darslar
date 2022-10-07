# pass haqida
for i in 'salom':
    pass

def oddiy_funksiya():
    pass



# def simple_func():
#     print('Funksiya ishlayapti.')

# simple_func()

# salomlash('Bahriddin')

# def salomlash(ism):
#     '''Bu funksiya berilgan ism bilan salomlashadi'''
#     print(f'Assalomu alaykum {ism}. Hayrli tong.')

# salomlash('Sevinch')

# # function doc string

# print(salomlash.__doc__)

# # function None

# print(salomlash('Sobir'))

# print(print('salom'))

# Sonning modulini qaytaruvchi dastur

# def modul(num):
#     if num >= 0:
#         return num
#     else:
#         return -num

# m = modul(-27)

# print(modul(27))
# print(modul(-13))
# print(f'-27 ning moduli {m}')

# 2 son yig`indisi

# def summa(num1,num2):
#     return num1 + num2

# sum = summa(5,6)
# summa(13,27)

# print(sum)
# a = 13
# b = 27
# sum = summa(a,b)
# print(sum)

# funksiyada lokal va global o`zgaruvchilar

def func():
    global x
    x = 13
    print(f'x ning qiymati {x}')

func()
x = 20
print(f'x ning qiymati {x}')

