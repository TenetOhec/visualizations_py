# 01

# def selectionSort(arr):
#     for i in range(0, len(arr) - 1):
#         max = arr[i]
#         index = i
#         for j in range(i + 1, len(arr)):
#             if arr[j] > max:
#                 index = j
#                 max = arr[j]
#         if (index != i):
#             temp = arr[i]
#             arr[i] = max
#             arr[index] = temp
#         print(f"After round {i}: {arr}")
#
#
# Arr = []
# while True:
#     str = input("Enter an integer (or enter quit): ")
#     if (str == "quit"):
#         break
#     else:
#         num = int(str)
#         Arr.append(num)
# print(f"Selection Sort Algorithm for {Arr}")
# selectionSort(Arr)


# 02

# input_num1 = int(input("Enter a student id: "))
# input_num2 = int(input("Enter a starting number: "))
# input_num3 = int(input("Enter number of equations: "))
#
# print("Equation display:")
# for i in range(input_num3):
#     print(f"{input_num1} + {input_num2 + i} = {input_num1 + input_num2 + i}")


# 03

# input_num1 = int(input("Min integer: "))
# input_num2 = int(input("Max integer: "))
#
# max = input_num1 if (input_num1 > input_num2) else input_num2
# min = input_num1 if (input_num1 < input_num2) else input_num2
#
# print("Display equation:")
# for i in range(max - min + 1):
#     print(f"{max - i} + {max - i} + {max - i} = {(max - i) * 2} + {max - i} = {(max - i) * 3}")


# 04

# first_even = -1
# first_odd = -1
# Arr = []
#
# while True:
#     str = input("Enter an integer (or EXIT): ")
#     if (str == "EXIT"):
#         break
#     else:
#         num = int(str)
#         Arr.append(num)
# for i in range(len(Arr)):
#     if (Arr[i] % 2 == 0):
#         if(first_even == -1):
#             first_even = Arr[i]
#     if (Arr[i] % 2 == 1):
#         if(first_odd == -1):
#             first_odd = Arr[i]
# if (first_even != -1):
#     print(f"First even number is {first_even}")
# else:
#     print("Even number not found")
# if (first_odd != -1):
#     print(f"First odd number is {first_odd}")
# else:
#     print("Odd number not found")


# 05

# input_num1 = int(input("Enter number of lines: "))
# input_num2 = int(input("Enter number of numbers on each line: "))
# for i in range(input_num1 * input_num2):
#     if ((i+1) % input_num2 != 0):
#         print(f"{i}", end=',')
#     else:
#         print(f"{i}.")


# 06

# input_str = input("Enter a string: ")
# input_num = int(input("Enter a positive integer: "))
#
# print("Display pattern:")
# for i in range(len(input_str)):
#     print(input_str[i] * input_num)


# 07

# input_str1 = input("Enter option A or B: ")
#
# if input_str1 != 'A' and input_str1 != 'B':
#     print("We only support A or B")
#     print("Good bye!")
#
# if input_str1 == 'A':
#     input_str2 = input("Enter a word: ")
#     for i in range(len(input_str2)):
#         print(f"Index {i} -> letter {input_str2[i]}")
#
# if input_str1 == 'B':
#     input_num = int(input("Enter a positive integer: "))
#     for i in range(input_num):
#         print(f"{input_num} - {i + 1} = {input_num - (i + 1)}")
#     print("Result is zero, stop now!")


# 08

# input_str1 = input("Enter a word for base: ")
# input_str2 = input("Enter a word for side: ")
#
# print("Here is the pattern:")
# print(f"*{input_str1}*")
# num1 = len(input_str1)
# num2 = len(input_str2)
#
# for i in range(num2):
#     print(input_str2[i] + ' ' * num1 + input_str2[i])
#
# print(f"*{input_str1}*")

# 09

while True:
    input_str = input("Enter an integer (or exit): ")
    if input_str == "exit":
        break
    num = int(input_str)

    if (num == 0):
        print("Zero, display just zero: 0")
    if(num < 0):
        print(f"Negative integer, display multiplication: ({num}) x ({num}) = {num * num}")
    if(num > 0):
        print(f"Positive integer, display addition: {num} + {num} = {num * 2}")

