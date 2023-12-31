# # Python exceptions

# dividing = 27 / 0
# print(dividing)

# def hi(fname,lname):
#     return f'Ismingiz: {fname} familiyangiz: {lname}'

# print(hi('Ahmadaliyev','Shahboz'))


# try:
#     numerator = 10
#     denominator = 10

#     result = numerator/denominator

#     print(result)
# except:
#     print("Error: Bo`luvchi 0 bo`lishi mumkin emas.")

# raise ZeroDivisionError

# try:    
#     even_numbers = [2,4,6,8]
#     print(even_numbers[5])

# except ZeroDivisionError:
#     raise ZeroDivisionError
#     # print("Bo`linuvchi 0 bo`lishi mukin emas.")
    
# except IndexError:
#     raise IndexError
#     print("Indeksni kiritishda xatolik.")


# x = 55
# assert x == 5, "x = 5 bo`lishi kerak."

# try:
#     # num = int(input("Enter a number: "))
#     num = 4
#     assert num % 2 == 0
# except:
#     print("Juft raqam emas!")
# else:
#     result = num ** 2
#     print(result)

# try:
#     # num = int(input("Enter a number: "))
#     num = 5
#     assert num % 2 == 0
# except:
#     print("Juft raqam emas!")
# else:
#     result = num ** 2
#     print(result)
# finally:
#     print('Dastur o`z ish faoliyatini tugatdi.')
#     print(num ** 2)