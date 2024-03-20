# Enter product code: ABC123
# Enter product name: Green eggs and ham
# Enter product size: 300mg
# Enter product price: 2.5
# ABC123: Green eggs and ham, 300mg
# Green eggs and ham, 300mg, $2.50
# ABC123: "Green eggs and ham"

# code = input("Enter product code: ")
# name = input("Enter product name: ")
# size = input("Enter product size: ")
# price = float(input("Enter product price: "))
#
#
# print(f"{code}: {name}, {size}")
# print("{0}, {1}, ${2:.2f}".format(name, size, price))
# print(f"{code}: \"{name}\"")

# print("{0} x {1} = {2}".format(1, 1, 1*1))
# print("{0} x {1} = {2}".format(2, 2, 2*2))
# print("{0} x {1} = {2}".format(3, 3, 3*3))
# print("{0} x {1} = {2}".format(4, 4, 4*4))
# print("{0} x {1} = {2}".format(5, 5, 5*5))
# print("{0} x {1} = {2}".format(6, 6, 6*6))
# print("{0} x {1} = {2}".format(7, 7, 7*7))
# print("{0} x {1} = {2}".format(8, 8, 8*8))
# print("{0} x {1} = {2}".format(9, 9, 9*9))
# print("{0} x {1} = {2}".format(10, 10, 10*10))


# print("{0:>10}{1:^30}{2:<10}".format("Faces", "Name", "Vertices"))
# print("{0:>10}{1:^30}{2:<10}".format(4, "Tetrahedron", 4))
# print("{0:>10}{1:^30}{2:<10}".format(6, "Cube", 8))
# print("{0:>10}{1:^30}{2:<10}".format(8, "Octahedron", 6))
# print("{0:>10}{1:^30}{2:<10}".format(12, "Dodecahedron", 20))
# print("{0:>10}{1:^30}{2:<10}".format(20, "Icosahedron", 12))


# def format_dob(dob):
#     day, month, year = dob.split('-')
#
#     month_names = {
#         '01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr',
#         '05': 'May', '06': 'Jun', '07': 'Jul', '08': 'Aug',
#         '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'
#     }
#
#     formatted_dob = f"{day}/{month_names[month]}/{year}"
#
#     return formatted_dob
#
#
# box_length = int(input("Enter length of the box: "))
#
# dob = input("Enter your dob (DD-MM-YYYY): ")
#
# border = '*' * box_length
#
# formatted_dob = format_dob(dob)
#
# center_padding = max(0, box_length - len(formatted_dob) - 7)
#
# result = f"{border}\n|DOB:{' ' * center_padding} {formatted_dob}|\n{border}"
#
# print(result)

# Input
# user_input = input("Enter an integer: ")
#
# number = int(user_input)
#
# print(f'\nThis is the number {number}.')
#
# print(f'It is between {number-1} and {number+1}.')


# zrog_legs_num = 2
# zmu_legs_num = 5
# zhark_legs_num = 10
# zrog = int(input("Enter number of zrog: "))
# zmu = int(input("Enter number of zmu: "))
# zhark = int(input("Enter number of zhark: "))
#
# print("\nLeg calculation")
# print(f"Zrog legs = {zrog} x {zrog_legs_num} = {zrog*zrog_legs_num}")
# print(f"Zmu legs = {zmu} x {zmu_legs_num} = {zmu*zmu_legs_num}")
# print(f"Zhark legs = {zhark} x {zhark_legs_num} = {zhark*zhark_legs_num}")
# print(f"Total legs = {zrog*zrog_legs_num} + {zmu*zmu_legs_num} + {zhark*zhark_legs_num} = {zrog*zrog_legs_num+zmu*zmu_legs_num+zhark*zhark_legs_num}")

# a = int(input("Enter 1st positive integer: "))
# b = int(input("Enter 2nd positive integer: "))
# print("\nMath operations:")
# print(f"Add: {a} + {b} = {a + b}")
# print(f"Minus: {a} - {b} = {a - b}")
# print(f"Times: {a} * {b} = {a * b}")
# print(f"Modulo: {a} % {b} = {a % b}")
# print(f"Division: {a} / {b} = {a / b}")
# print(f"Floor division: {a} // {b} = {a // b}")

# print("Packaging lollies into boxes")
# brand = input("Enter the lollies brand: ")
# number_lollies = int(input("Enter number of lollies: "))
# lollies_1 = int(input("How many lollies in 1 box? "))
#
# print(f"\n{brand} lollies packaging calculation")
# print(f"Number of lollies: {number_lollies}")
# print(f"Number of lollies per box: {lollies_1}")
# print(f"Number of boxes needed: {int(number_lollies / lollies_1)}")
# print(f"Number of lollies left over: {number_lollies % lollies_1}")


# name = input("Enter your name: ")
# street_address = input("Enter street address: ")
# city = input("Enter city: ")
# state = input("Enter state: ")
# postcode = input("Enter postcode: ")
# country = input("Enter country: ")
#
# print(f"\nHi {name}")
# print("This is your address:")
# print(f"{street_address}, {city}, {state} {postcode}, {country}.")

# print("Laptop rental calculation")
# brand = input("Enter the laptop brand: ")
# application_cost = int(input("Enter the application cost: "))
# monthly_cost = int(input("Enter the monthly cost: "))
# months = int(input("Enter the number of months: "))
#
# print(f"\nRental cost for {brand} laptop")
# print(f"Application cost: ${application_cost}")
# print(f"Rental cost: ${monthly_cost} x {months} month = ${monthly_cost * months}")
# print(f"Total cost: ${application_cost} + ${monthly_cost * months} = ${monthly_cost * months + application_cost}")


# code = input("Enter subject code: ")
# title = input("Enter subject title: ")
# points = int(input("Number of credit points: "))
# cost_point = int(input("Cost per credit point: "))
# core = input("Is this a core subject (Y/N)? ")
#
# print("\nHere is the JSON output")
# print("{")
# print(f"  \"code\": \"{code}\",")
# print(f"  \"title\": \"{title}\",")
# print(f"  \"core\": \"{core}\",")
# print(f"  \"cp\": {points},")
# print(f"  \"fee\": {points * cost_point},")
# print("}")


# code = input("Enter subject code: ")
# title = input("Enter subject title: ")
# points = int(input("Number of credit points: "))
# cost_point = int(input("Cost per credit point: "))
# core = input("Is this a core subject (Y/N)? ")
#
# print("\nHere is the XML output")
# print("<?xml version=\"1.0\"?>")
# print(f"<subject code=\"{code}\" core=\"{core}\">")
# print(f"  <title>{title}</title>")
# print(f"  <cp>{points}</cp>")
# print(f"  <fee>{points * cost_point}</fee>")
# print(f"</subject>")

# lab 3

# 1

# cost_item_1_50 = 3
# cost_item_50 = 2
#
# postage_1_50 = 10
# postage_50 = 0
#
# items = int(input("Enter the number of items: "))
#
# print("\nReceipt:")
# if(1 < items and items< 50):
#     print(f"{items} items x ${cost_item_1_50} = ${items * cost_item_1_50}")
#     print(f"Postage: ${postage_1_50}")
#     print(f"Total: ${items * cost_item_1_50 + postage_1_50}")
# elif(items >50):
#     print(f"{items} items x ${cost_item_50} = ${items * cost_item_50}")
#     print(f"Postage: ${postage_50}")
#     print(f"Total: ${items * cost_item_50 + postage_50}")

# 2

# cost_item_1_50 = 3
# cost_item_50 = 2
#
# postage_1_50_s = 10
# postage_1_50_r = 15
# postage_1_50_e = 20
#
# postage_50_s = 0
# postage_50_r = 10
# postage_50_e = 17
#
#
# items = int(input("Enter the number of items: "))
# postage = input("Enter shipping method (s/r/e): ")
#
# print("\nReceipt:")
# if(1 < items and items<= 50):
#     print(f"{items} items x ${cost_item_1_50} = ${items * cost_item_1_50}")
#     if(postage == 's'):
#         print(f"Standard post: ${postage_1_50_s}")
#         print(f"Total: ${items * cost_item_1_50 + postage_1_50_s}")
#     elif(postage == 'r'):
#         print(f"Registered post: ${postage_1_50_r}")
#         print(f"Total: ${items * cost_item_1_50 + postage_1_50_r}")
#     elif (postage == 'e'):
#         print(f"Express post: ${postage_1_50_e}")
#         print(f"Total: ${items * cost_item_1_50 + postage_1_50_e}")
#
# elif(items >50):
#     print(f"{items} items x ${cost_item_50} = ${items * cost_item_50}")
#     if (postage == 's'):
#         print(f"Standard post: ${postage_50_s}")
#         print(f"Total: ${items * cost_item_50 + postage_50_s}")
#     elif (postage == 'r'):
#         print(f"Registered post: ${postage_50_r}")
#         print(f"Total: ${items * cost_item_50 + postage_50_r}")
#     elif (postage == 'e'):
#         print(f"Express post: ${postage_50_e}")
#         print(f"Total: ${items * cost_item_50 + postage_50_e}")

# 3

# nums = []
#
# nums.append(int(input("Enter the first integer: ")))
# nums.append(int(input("Enter the second integer: ")))
# nums.append(int(input("Enter the third integer: ")))
# nums.append(int(input("Enter the fourth integer: ")))
#
# min = nums[0]
# max = nums[0]
# for num in nums:
#     if(num > max):
#         max = num
#     if(num < min):
#         min = num
#
# print(f"\nThe minimum number is {min} and the maximum number is {max}.")

# lab04
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()  # Move to the next line after each row

# lab05
# 1
# num = 2
#
#
# # Set the maximum value (10 in this case)
# max_value = 10
#
# # While loop to generate the output
# while num <= max_value:
#     result = num + num
#     print(f"{num:>2} + {num:>2} = {result:>2}")
#     # print(f" {num1} +  {num2} =  {result}")
#
#     # Increment the variables by 2 for the next iteration
#     num += 2

# 2

# num = 1
# while num < 10:
#     if num == 9:
#         print(num, end=".")
#     else:
#         print(num, end="; ")
#     num += 2

# 3
# total_integers = 0
# sum_number = 0
# even_numbers = 0
# odd_numbers = 0
# positive_numbers = 0
# negative_numbers = 0
#
# while True:
#     user_input = input("Enter an integer or q to quit: ")
#
#     if user_input == 'q':
#         break
#
#     number = int(user_input)
#     total_integers += 1
#     sum_number = sum_number + number
#     if number % 2 == 1:
#         odd_numbers += 1
#     else:
#         even_numbers +=1
#     if number > 0:
#         positive_numbers += 1
#     elif number < 0:
#         negative_numbers += 1
#
#
#
# print("\nSummary information:")
# print(f"You have entered {total_integers} integers.")
# print(f"The sum of these numbers is {sum_number}.")
# print(f"There are {even_numbers} even numbers.")
# print(f"There are {odd_numbers} odd numbers.")
# print(f"There are {positive_numbers} positive numbers.")
# print(f"There are {negative_numbers} negative numbers.")

# 04
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and key > arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#
#
# numbers = []
#
# while True:
#     user_input = input("Enter an integer or q to quit: ")
#
#     if user_input == 'q':
#         break
#
#     else:
#         number = int(user_input)
#         numbers.append(number)
#
#
# print("Before insertion sort:", numbers)
# insertion_sort(numbers)
# print("After insertion sort:", numbers)


# assignments

# 1

# user_input1 = input("Which degree do you choose? Undergraduate (U) or Postgraduate (P): ")
# if user_input1 == 'U':
#     print("\nCourse summary: ")
#     print("Location: Wollongong, Liverpool")
#     print("Duration: 3 years full-time or part-time equivalent")
# elif user_input1 == 'P':
#     user_input2 = input("Which course do you choose? Master by Coursework (C) or Master by Research (R): ")
#     if user_input2 == 'C':
#         print("\nCourse summary: ")
#         print("Location: Wollongong, Liverpool")
#         print("Duration: 1.5-2 years full-time or part-time equivalent")
#     elif user_input2 == 'R':
#         print("\nCourse summary: ")
#         print("Location: Wollongong")
#         print("Duration: 2 years full-time or part-time equivalent")


# 2

# num1 = int(input("Enter an integer: "))
# num2 = int(input("Enter another integer: "))
# if num2 < num1:
#     t = num1
#     num1 = num2
#     num2 = t
# for i in range(num1, num2+1):
#     print(f"{i:>5} +{i:>6} ={i*2:>6}")


# 3

# num = int(input("Enter a positive integer: "))
# for i in range(1, num + 1):
#     num2 = i
#     print(" " * (2*num-i*2), end="")
#     for j in range(1, num2+1):
#         print(j, end=" ")
#     for k in range(num2-1, 0, -1):
#         print(k, end=" ")
#     print()


# 4

# user_input = int(input("How many subjects would you choose for this session: "))
# tag = 1
# for i in range(1, user_input + 1):
#     con = input("Would you like to continue subject enrolment? (Y/N): ")
#     if con == 'Y':
#         sub = input("Which subject would you like: ")
#         print(f"You have successfully enrolled in {sub}.")
#     if con == 'N':
#         tag = 0
#         if (user_input - i + 1) > 1:
#             print(
#                 f"You have not completely finished the enrollment. There are {user_input - i + 1} "
#                 f"subjects to be enrolled.")
#         else:
#             print("You have not completely finished the enrollment. There is 1 subject to be enrolled.")
#         break
# if tag == 1:
#     print(f"You have finished the enrollment of all {user_input} subjects.")

# 5
# fruit_and_veg_cost = float(input("Enter the cost of Fruit&Veg: "))
# deli_chilled_meals_cost = float(input("Enter the cost of Deli&Chilled Meals: "))
# pantry_cost = float(input("Enter the cost of Pantry: "))
#
# total_cost = fruit_and_veg_cost + deli_chilled_meals_cost + pantry_cost
# discounted_cost = total_cost
#
# use_mobile_discount = input("Would you like to use your 10% Woolworths Mobile discount? Y or N: ")
# use_rewards_dollars = input("Would you like to use your $10 Everyday Rewards Dollars? Y or N: ")
#
# print("\nReceipt:")
# print("Fruit&Veg".ljust(40) + f"{fruit_and_veg_cost:.2f}".rjust(15))
# print("Deli&Chilled Meals".ljust(40) + f"{deli_chilled_meals_cost:.2f}".rjust(15))
# print("Pantry".ljust(40) + f"{pantry_cost:.2f}".rjust(15))
#
#
# print("Total".ljust(40) + f"${total_cost:.2f}".rjust(15))
#
#
#
# if use_mobile_discount.upper() == 'Y':
#     discount_amount = 0.10 * total_cost
#     discounted_cost -= discount_amount
#     print(f"\n$%.2f saved with your Woolworths Mobile discount" % discount_amount)
#
# if use_mobile_discount.upper() == 'Y':
#     print("Promotional Price".ljust(40) + f"${discounted_cost:.2f}".rjust(15))
#
# if use_rewards_dollars.upper() == 'Y':
#     if discounted_cost >= 10:
#         discounted_cost -= 10
#         print("\n$10 Everyday Rewards Dollars enjoyed")
#
# # print("\nPayment".ljust(40) + f" ${discounted_cost:.2f}".rjust(15))
# print(f"\n{f'Payment'.ljust(40) + f'${discounted_cost:.2f}'.rjust(15)}")

# 6
# user_input = input("Which subject did you enroll in? (a) CSIT110 (b) CSIT881: ")
# if user_input == 'a':
#     print("You are an undergraduate.")
# elif user_input =='b':
#     print("You are a postgraduate.")
# else:
#     print("Invalid input.")

# 7

# input_string = input("Enter some characters: ")
# num = int(input("Enter the number of characters to be displayed: "))
# result = input_string[:num]
# result = '-'.join(result)
# print(result)

# 8

# input_string = input("Enter a string: ")
# change = input("Uppercase or Lowercase? (U/L): ")
#
# if change == 'U' or change == 'u':
#     print(f"The Uppercase of {input_string} is {input_string.upper()}.")
# elif change == 'L' or change == 'l':
#     print(f"The Lowercase of {input_string} is {input_string.lower()}.")
# else:
#     print("Invalid input.")


# s = 'asd'
# sss = []
# for i in s:
#     s1 = i*3
#     sss.append(s1)
# print(sss)
# s2 = ''.join(sss)
# print(s2)

# lab 06

# 1

# def triple(sentence):
#     result_list = []
#     for i in sentence:
#         s = i * 3
#         result_list.append(s)
#     res = ''.join(result_list)
#     return res


# 3

# def next_number(num):
#     if num % 2 == 0:
#         return 3 * num + 1
#     else:
#         return 2 * num + 2
#
#
# num1 = int(input("Enter the initial number: "))
# print("Sequence:")
# i = 0
# while True:
#     if i == 0:
#         print(f"Step {i}: {num1}")
#         i += 1
#     if num1 > 100:
#         break
#     else:
#         num1 = next_number(num1)
#         print(f"Step {i}: {num1}")
#         i += 1

# lab 07

# 1

# @classmethod是一个装饰器，用于将一个方法定义为类方法。类方法与实例方法不同，它不需要实例化一个对象就可以调用，而是通过类本身来调用。类方法通常用于执行与类相关的操作，而不是与特定实例相关的操作。例如，在Student类中，我们可以定义一个类方法，用于返回所有学生的总人数。
#
# 下面是一个示例代码，展示了如何使用@classmethod定义一个类方法：
# ```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def count_students(cls):
        return len(cls.students)

    @classmethod
    def add_student(cls, name, age):
        cls.students.append(Student(name, age))

    @classmethod
    def remove_student(cls, name):
        cls.students = [s for s in cls.students if s.name != name]

    @classmethod
    def get_student(cls, name):
        for student in cls.students:
            if student.name == name:
                return student
        return None

    @classmethod
    def print_students(cls):
        for student in cls.students:
            print(student.name, student.age)

# 创建一个Student类实例
student1 = Student("Alice", 20)
student2 = Student("Bob", 21)
student3 = Student("Charlie", 22)

# 将实例添加到类属性中
Student.add_student(student1.name, student1.age)
Student.add_student(student2.name, student2.age)
Student.add_student(student3.name, student3.age)

# 调用类方法
print(Student.count_students())  # 输出：3
print(Student.get_student("Alice"))  # 输出：<__main__.Student object at 0x7f31283521d0>
Student.remove_student("Bob")
print(Student.count_students())  # 输出：2
Student.print_students()  # 输出：Alice

