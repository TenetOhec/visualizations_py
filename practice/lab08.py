# class Staff:
#     def __init__(self, staff_number, first_name, last_name, email):
#         self.staff_number = staff_number
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email

# staffObj1 = Staff(100001, "John", "Lee", "jl123@gmail.com")
# staffObj2 = Staff(100002, "Mary", "Zheng", "maryz@gmail.com")
# staffObj3 = Staff(100003, "Cindy", "Wilson", "cw456@hotmail.com")

class Staff:
    def __init__(self, staff_id, first_name, last_name, email):
        self.staff_id = staff_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def print_details(self, width):
        line1 = width - len("| Staff number: ") - len(str(self.staff_id)) - 1
        line2 = width - len("| ") - len(self.first_name) - len(self.last_name) - 2
        line3 = width - len("| ") - len(self.email) - 1
        print("{}".format("-" * width))  # Top border
        print(f"| Staff number: {self.staff_id}" + " " * line1 + "|")
        print(f"| {self.first_name} {self.last_name}" + " " * line2 + "|")
        print(f"| {self.email}" + " " * line3 + "|")
        print("{}".format("-" * width))


staffObj = Staff("012345", "John", "Smith", "js@gmail.com")
staffObj.print_details(50)
