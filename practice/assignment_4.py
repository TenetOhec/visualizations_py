# 1

# def ask_transport_num():
#     bike_num = int(input("Enter the number of bikes: "))
#     car_num = int(input("Enter the number of cars: "))
#     truck_num = int(input("Enter the number of trucks: "))
#     return bike_num, car_num, truck_num
#
#
# def display_transport(bike_num, car_num, truck_num):
#     print("==========")
#     print(f"Bike: {bike_num}")
#     print(f"Car: {car_num}")
#     print(f"Truck: {truck_num}")
#     print("==========")

# 2

# class Bus:
#     def __init__(self, route, company, plate):
#         self.route = route
#         self.company = company
#         self.plate = plate
#
#     def printBus(self):
#         print(f'Route: {self.route}')
#         print('Company: %s' % self.company)
#         print('Plate: %s' % self.plate)
#
#
# busObj1 = Bus("90", "Dions Bus Service", "MO8182")
# busObj2 = Bus("91", "Dions Bus Service", "MO8888")
# busObj1.printBus()
# busObj2.printBus()

# 3
# def displayPattern(word, shape):
#     if shape == "triangle":
#         print("Triangle pattern:")
#         n = len(word)
#         for i in range(n):
#             print(" " * (n - 1 - i), end="")
#             print(word[0:i+1].lower())
#
#     elif shape == "rectangle":
#         print("rectangle pattern:")
#         n = len(word)
#         for i in range(n):
#             print(word.lower())
#
#     elif shape == "trapezoidal":
#         print("trapezoidal pattern:")
#         n = len(word)
#         for i in range(n):
#             print(" " * (n - 1 - i), end="")
#             print(word[0:i+1].lower() + word[i::-1].lower())
#
#     else:
#         print("Unknown shape.")


# displayPattern(word="One", shape="triangle")
# displayPattern(word="gooDDAY", shape="rectangle")
# displayPattern(word="abcd", shape="trapezoidal")
# displayPattern(word="thanks", shape="Hooray")
# displayPattern(word="allGood", shape=".~!")

# 4

def find_bike_car_truck(wheel):
    bike = 2
    car = 4
    truck = 8
    if wheel % 2 == 1:
        print("Not found")
    else:
        for i in range(int(wheel / bike) + 1):
            for j in range(int(wheel / car) + 1):
                for k in range(int(wheel / truck) + 1):
                    if i * bike + j * car + k * truck == wheel:
                        print(f"Bike: {i}, Car: {j}, Truck: {k}")

# find_bike_car_truck(11)

# 5

# def jersey_num_iron_on():
#     neme = ""
#     num = -1
#     while True:
#         name = input("Please enter a name with an odd number of (at most 9) let"
#                      + "ters: ")
#         if (len(name) % 2) == 1 and len(name) < 10:
#             break
#     while True:
#         num = int(input("Please enter an integer (0 - 999): "))
#         if 0 <= num <= 999:
#             break
#     print("  ___       ___")
#     print(" /   \\_____/   \\")
#     print("|_             _|")
#     print("  |" + " " * int((11-len(name))/2) + f"{name.upper()}" + " "
#           * int((11-len(name))/2) + "|")
#     print("  |           |")
#     if num > 100:
#         print(f"  |    {num}    |")
#     elif 0 <= num <= 9:
#         print(f"  |     {num}     |")
#     else:
#         print(f"  |    {int(num / 10)} {num % 10}    |")
#     print("  |           |")
#     print("  +___________+")
#
# jersey_num_iron_on()

# 6

# class Player:
#     def __init__(self, name, number, height, dob, position):
#         self.name = name
#         self.number = number
#         self.height = height
#         self.dob = dob
#         self.position = position
#
#     def __str__(self):
#         return f"Player[name=\"{self.name}\", number=\"{self.number}\", height=\"{self.height}\", dob=\"{self.dob}\", position=\"{self.position}\"]"
#
# # Example usage:
# playerObj1 = Player("Cristiano Ronaldo", "7", "1.87 m", "5 February 1985", "Forward")
# playerObj2 = Player("Kylian Mbappé", "7", "1.78 m", "20 December 1998", "Forward")
# print(playerObj1)
# print(playerObj2)


# def jersey_num_iron_on():
#     name = ""
#     num = -1
#     while (len(name) % 2) != 1 or len(name) > 9:
#         name = input("Please enter a name with an odd number of (at most 9) let"
#                      + "ters: ")
#     while not (0 <= num <= 999):
#         num = int(input("Please enter an integer (0 - 999): "))
#     print("  ___       ___")
#     print(" /   \_____/   \\")
#     print("|_             _|")
#     print("  |" + " " * int((11 - len(name)) / 2) + f"{name.upper()}" + " "
#           * int((11 - len(name)) / 2) + "|")
#     print("  |           |")
#
#     if num > 100:
#         print(f"  |    {num}    |")
#     elif 0 <= num <= 9:
#         print(f"  |     {num}     |")
#     else:
#         print(f"  |    {int(num / 10)} {num % 10}    |")
#     print("  |           |")
#     print("  +___________+")
#
# jersey_num_iron_on()
