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

input_string = input("Enter a string: ")
change = input("Uppercase or Lowercase? (U/L): ")

if change == 'U' or change == 'u':
    print(f"The Uppercase of {input_string} is {input_string.upper()}.")
elif change == 'L' or change == 'l':
    print(f"The Lowercase of {input_string} is {input_string.lower()}.")
else:
    print("Invalid input.")