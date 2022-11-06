
# task 1(1)
# num = int(input("Enter the number "))
# if num % 2 == 0:
#     print("It is an even number (1)")
# else:
#     print("It is a not even number (0)")

# task 1(2)
# num = int(input("Enter the number "))
# print(1) if num % 2 == 0 else print(0)

# task 2

# voice = str(input())
# if voice.capitalize() == "Meow":
#     print("Its a cat")
# if voice.capitalize() == "Bark":
#     print("Its a dog")
# elif voice.capitalize() != "Meow" and voice.capitalize() != "Bark":
#     print("Unknown monster")

# task 3

# num = str(input("Enter the number "))
#
# if not num.lstrip("-").isdigit():
#     print("it's not number! Try one more time")
# elif int(num) < 0:
#     print("You entered a number with the number of digits: " + str(len(num.lstrip("-"))))
#     print("This number is negative ")
# elif int(num) > 0:
#     print("You entered a number with the number of digits: " + str(len(num)))
#     print("This number is positive ")
# elif int(num) == 0:
#     print("You entered '0' ")

# task 4

# num = int(input("Enter the number "))
# if (num ** 0.5) % 1 == 0:
#     print(num ** 2)
# else:
#     print(-1)

# task 5

# i = int(input())
# arabian_num_list = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# rome_num_list = ("Nulla", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X")
# if 0 <= i <= 10:
#     print(str(arabian_num_list[i]) + " ---> " + str(rome_num_list[i]))
# else:
#     print("I don't know")

# task 6

# x = input("x ордината точки расположения короля. Введите: ")
# y = input("y абсцисса точки расположения короля. Введите: ")
# print(str(x) + ":" + str(y) + " - расположение короля")
# a = input("x ордината точки в которую нужно поставить короля. Введите: ")
# b = input("y абсцисса точки в которую нужно поставить короля. Введите: ")
# print(str(a) + ":" + str(b) + " - перемещение короля в данную точку")
# if 1 <= int(a) <= 8 and 1 <= int(b) <= 8 and 1 <= int(x) <= 8 and 1 <= int(y) <= 8:
#     if int(a) == int(x) + 1 or int(a) == int(x) - 1 or int(b) == int(y) + 1 or int(b) == int(y) - 1:
#         print("He can!")
#     elif int(a) == int(x) and int(b) == int(y):
#         print("He stay safe")
#     else:
#         print("He can't")
# else:
#     print("Not valid number")

# task 7

# x = input("x ордината точки расположения ферзя. Введите: ")
# y = input("y абсцисса точки расположения ферзя. Введите: ")
# print(str(x) + ":" + str(y) + " - расположение ферзя")
# a = input("x ордината точки в которую нужно поставить ферзя. Введите: ")
# b = input("y абсцисса точки в которую нужно поставить ферзя. Введите: ")
# print(str(a) + ":" + str(b) + " - перемещение ферзя в данную точку")
# if 1 <= int(a) <= 8 and 1 <= int(b) <= 8 and 1 <= int(x) <= 8 and 1 <= int(y) <= 8:
#     if int(a) == int(x) and 1 <= int(b) <= 8 and int(b) != int(y) or int(b) == int(y) and 1 <= int(a) <= 8 and \
#             int(a) != int(x):
#         print("He can!")
#     elif int(a) % 2 == 0 and int(b) % 2 != 0 and int(y) % 2 == 0 and int(x) % 2 != 0 or int(b) % 2 == 0 and \
#             int(a) % 2 != 0 and int(x) % 2 == 0 and int(y) % 2 != 0 or int(x) == int(y) and int(a) == int(b):
#         print("He can!!!!!")
#     elif int(a) == int(x) and int(b) == int(y):
#         print("He stay safe")
#     else:
#         print("He can't")
# else:
#     print("Not valid number")

# task 8

# x = input("x ордината точки расположения коня. Введите: ")
# y = input("y абсцисса точки расположения коня. Введите: ")
# print(str(x) + ":" + str(y) + " - расположение коня")
# a = input("x ордината точки в которую нужно поставить коня. Введите: ")
# b = input("y абсцисса точки в которую нужно поставить коня. Введите: ")
# print(str(a) + ":" + str(b) + " - перемещение коня в данную точку")
# if 1 <= int(a) <= 8 and 1 <= int(b) <= 8 and 1 <= int(x) <= 8 and 1 <= int(y) <= 8:
#     if int(a) == int(x) + 2 and int(b) == int(y) + 1 or int(a) == int(x) + 2 and int(b) == int(y) - 1 or \
#             int(a) == int(x) - 2 and int(b) == int(y) + 1 or int(a) == int(x) - 2 and int(b) == int(y) - 1 or \
#             int(b) == int(y) + 2 and int(a) == int(x) + 1 or int(b) == int(y) + 2 and int(a) == int(x) - 1 or \
#             int(b) == int(y) - 2 and int(a) == int(x) + 1 or int(b) == int(y) - 2 and int(a) == int(x) - 1:
#         print("He can!!!!!")
#     else:
#         print("He can't")
# else:
#     print("Not valid number")
