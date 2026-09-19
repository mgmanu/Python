# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# c = float(input("Enter third number: "))

# if a >= b and a >= c:
#     print("Maximum number is:", a)
# elif b >= a and b >= c:
#     print("Maximum number is:", b)
# else:
#     print("Maximum number is:", c)


# n = int(input("Enter the value of n: "))
# a = 0
# b = 1
# if n <= 0:
#     print("Please enter a positive integer")
# elif n == 1:
#     print(a)
# else:
#     print(a, b, end=" ")
#     for i in range(3, n + 1):
#         c = a + b
#         print(c, end=" ")
#         a = b
#         b = c


# n = int(input("Enter n: "))
# a = 0
# b = 1
# if n <= 0:
#     print("Invalid input")
# elif n == 1:
#     print(a)
# else:
#     print(a, b, end=" ")
#     for i in range(2, n):
#         c = a + b
#         print(c, end=" ")
#         a = b
#         b = c
















# phrase = input("Enter a phrase: ")
# words = phrase.split()
# acronym = ""
# for word in words:
#     acronym += word[0].upper()
# print("Acronym:", acronym)



# phrase = input("Enter a phrase: ")
# words = phrase.split()
# acronym = ""
# for i in range(len(words)):
#     acronym += words[i][0].upper()
# print("Acronym:", acronym)





# p = float(input("Enter principal: "))
# r = float(input("Enter rate: "))
# t = float(input("Enter time: "))

# si = (p * r * t) / 100
# print("Simple Interest =", si)









# n = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(n, "x", i, "=", n * i)


# n = int(input("Enter a number: "))
# i = 1
# while i <= 10:
#     print(n, "x", i, "=", n * i)
#     i += 1









# n = int(input("Enter a number: "))
# temp = n
# rev = 0
# while temp > 0:
#     digit = temp % 10
#     rev = rev * 10 + digit
#     temp //= 10
# if n == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")






# marks = int(input("Enter marks: "))
# if marks >= 90:
#     print("Grade: A")
# elif marks >= 75:
#     print("Grade: B")
# elif marks >= 60:
#     print("Grade: C")
# elif marks >= 40:
#     print("Grade: D")
# else:
#     print("Grade: F")










# def student_details(name, usn, marks):
#     print("Name:", name)
#     print("USN:", usn)
#     print("Marks:", marks)
# name = input("Enter name: ")
# usn = input("Enter USN: ")
# marks = int(input("Enter marks: "))
# student_details(name, usn, marks)










# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# temp = a
# a = b
# b = temp
# print("After swapping:")
# print("a =", a)
# print("b =", b)


# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# a, b = b, a
# print("After swapping:")
# print("a =", a)
# print("b =", b)












# for num in range(2, 101):
#     is_prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num, end=" ")



# for num in range(2, 101):
#     for i in range(2, num):
#         if num % i == 0:
#             break
#     else:
#         print(num, end=" ")












# try:
#     n = float(input("Enter a number: "))
#     print("Reciprocal =", 1 / n)
# except ValueError:
#     print("Invalid input! Please enter a number.")
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# finally:
#     print("Program execution completed.")




















# squares = []
# for i in range(1, 6):
#     squares.append(i * i)
# print(squares)


# squares = [i*i for i in range(1, 6)]
# print(squares)


















# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print(f"Hello {name}! You are {age} years old.")


# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print("Hello {}! You are {} years old.".format(name, age))


# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print("Hello %s! You are %d years old." % (name, age))

























