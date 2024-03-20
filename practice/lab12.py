import csv




# ['code', 'name', 'cp']
# ['MATH101', 'Abstract Algebra', '4']
# ['CSCI200', 'C++ Programming', '5']
# ['MATH202', 'Geometry', '6']
# ['IT103', 'Java', '7']


# 1

# def main():
#     file_name = input("Enter subject file name: ")
#     data = []
#     with open(file_name) as f:
#         reader = csv.reader(f)
#         for row in reader:
#             data.append(row)

# data: [['code', 'name', 'cp'], ['MATH101', 'Abstract Algebra', '4'], ['CSCI200', 'C++ Programming', '5'], ['MATH202', 'Geometry', '6'], ['IT103', 'Java', '7']]

#     col1_len = int(input("Enter 1st column length: "))
#     col2_len = int(input("Enter 2nd column length: "))
#     col3_len = int(input("Enter 3rd column length: "))
#     data[0] = [(data[0][0].capitalize()), (data[0][1].capitalize()), (data[0][2].upper())]
#     for row in data:
#         print(f"{row[0]:<{col1_len}}{row[1]:^{col2_len}}{row[2]:>{col3_len}}")
#
#
# if __name__ == "__main__":
#     main()


#
# def main():
#     with open('student_list.txt') as f:
#         contents = f.read()
#     print(contents)
#
# if __name__ == "__main__":
#     main()

# 6354625
# John
# Smith
# 0657373
# Mary
# Wilson
# 0042627
# Lee
# Davis


# 2

def main():
    # file_name = input("Enter student file name: ")
    data = []
    result = []
    with open('/Users/air/visualizations_py/practice/student_list.txt') as f:
        for line in f:
            data.append(line.rstrip())
    # 列表解析，将每三个元素作为一个子列表，组成最终的列表
    # result = [data[i:i + 3] for i in range(0, len(data), 3)]
    col1_len = int(input("Enter 1st column length: "))
    col2_len = int(input("Enter 2nd column length: "))
    col3_len = int(input("Enter 3rd column length: "))
    col1 = "Student Number"
    col2 = "First Name"
    col3 = "Last Name"
    print(f"{col1:>{col1_len}}{col2:>{col2_len}}{col3:>{col3_len}}")
    # 将每三个元素作为一个子列表，组成最终的列表
    for i in range(0, len(data), 3):
        result.append(data[i:i + 3])
    for row in result:
        print(f"{row[0]:>{col1_len}}{row[1]:>{col2_len}}{row[2]:>{col3_len}}")


if __name__ == "__main__":
    main()
