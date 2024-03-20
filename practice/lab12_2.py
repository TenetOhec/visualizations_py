# import csv
#
#
# def read_csv(file_name):
#     with open(file_name, 'r') as file:
#         reader = csv.reader(file)
#         data = [row for row in reader]
#     return data
#
#
# def display_table(data, col1_len, col2_len, col3_len):
#     col1_format = '{:<' + str(col1_len) + '}'
#     col2_format = '{:^' + str(col2_len) + '}'
#     col3_format = '{:>' + str(col3_len) + '}'
#
#     print(col1_format.format("Code"), col2_format.format("Name"), col3_format.format("CP"))
#
#     for row in data:
#         code, name, cp = row
#         print(col1_format.format(code), col2_format.format(name), col3_format.format(cp))
#
#
# def main():
#     file_name = input("Enter subject file name: ")
#     col1_len = int(input("Enter 1st column length: "))
#     col2_len = int(input("Enter 2nd column length: "))
#     col3_len = int(input("Enter 3rd column length: "))
#
#     data = read_csv(file_name)
#     display_table(data, col1_len, col2_len, col3_len)
#
#
# if __name__ == "__main__":
#     main()

def main():
    # file_name = input("Enter student file name: ")
    data = []
    result = []
    with open('/Users/air/visualizations_py/practice/student_list.txt') as f:
        for line in f:
            data.append(line.rstrip())
    # 列表解析，将每三个元素作为一个子列表，组成最终的列表
    result = [data[i:i + 3] for i in range(0, len(data), 3)]

    col1_len = int(input("Enter 1st column length: "))
    col2_len = int(input("Enter 2nd column length: "))
    col3_len = int(input("Enter 3rd column length: "))

    col1 = "Student Number"
    col2 = "First Name"
    col3 = "Last Name"
    print(f"{col1:>{col1_len}}{col2:>{col2_len}}{col3:>{col3_len}}")
    for row in result:
        print(f"{row[0]:>{col1_len}}{row[1]:>{col2_len}}{row[2]:>{col3_len}}")


if __name__ == "__main__":
    main()
