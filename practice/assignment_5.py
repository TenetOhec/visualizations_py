# 1
# class Node:
#     # {
#     def __init__(self, datum, next):
#         self.datum = datum
#         self.next = next
#
#
# # }
#
# class MyDigitQueue:
#     # {
#     def __init__(self):
#         self.frontNode = None
#         self.endNode = None
#
#     def front(self):
#         if self.frontNode is None:
#             return None
#         return self.frontNode.datum
#
#     def enqueue(self, item):
#         if 0 <= item <= 9:
#             new_node = Node(datum=item, next=None)
#             if self.frontNode is None:
#                 self.frontNode = new_node
#                 self.endNode = new_node
#             else:
#                 self.endNode.next = new_node
#                 self.endNode = new_node
#
#     def dequeue(self):
#         if self.frontNode is None:
#             return None
#
#         item = self.frontNode.datum
#         self.frontNode = self.frontNode.next
#
#         if self.frontNode is None:
#             self.endNode = None
#         return item
#
# # }
# queueObj = MyDigitQueue()
#
# # enqueue() add item to the queue
# queueObj.enqueue(0)
# queueObj.enqueue(17) # ignored
# queueObj.enqueue(-1) # ignored
# queueObj.enqueue(9)
#
# # front() get front item of the queue
# print(queueObj.front())
# print(queueObj.front())
#
# # dequeue() remove item from queue
# print(queueObj.dequeue())
# print(queueObj.dequeue())
# print(queueObj.dequeue())

# 2
# list_input = []
# while True:
#     user_input = input("Enter a word (or type EXIT to quit): ")
#     if user_input == "EXIT":
#         break
#     else:
#         list_input.append(user_input)
# print(f"Word list you have entered: {list_input}")

# 3
# num1_input = int(input("Enter a min integer: "))
# num2_input = int(input("Enter a max integer: "))
# # 1 < 2
# num1_input, num2_input = (num1_input, num2_input) if num1_input < num2_input else (num2_input, num1_input)
# list_result = []
# for i in range(num2_input, num1_input - 1, -1):
#     for j in range(0, 3):
#         list_result.append(i)
# print("Here is a list of numbers constructed:")
# print(list_result)

# 4

# user_input = input("Enter a sentence: ")
# len_input = len(user_input)
# list_result = []
# for i in range(len_input):
#     if i % 2 == 1:
#         list_result.append(user_input[i])
# print("List of characters at odd index:")
# print(list_result)

# 5
# list_input = []
# while True:
#     user_input = input("Enter a word (or type Q to quit): ")
#     if user_input == "Q":
#         break
#     else:
#         if len(user_input) < 5:
#             continue
#         else:
#             list_input.append(user_input[4])
# print("List of characters:")
# print(list_input)

# 6
# list_input = []
# while True:
#     user_input = input("Enter a word (or enter QUIT to quit): ")
#     if user_input == "QUIT":
#         break
#     else:
#         list_input.append(user_input)
# print("List of last 5 words:")
# if len(list_input) < 5:
#     print(list_input)
# else:
#     print(list_input[-5:])

# 7

# def add_list(list1, list2):
#     len1 = len(list1)
#     len2 = len(list2)
#     if len1 > len2:
#         for i in range(0, len2):
#             list1[i] = list1[i] + list2[i]
#         return list1
#     else:
#         for i in range(0, len1):
#             list2[i] = list1[i] + list2[i]
#         return list2

# 8

def list_character(word, index_list):
    len1 = len(word)
    list_result = []
    for i in range(0, len(index_list)):
        if index_list[i] > len1-1:
            continue
        else:
            list_result.append(word[index_list[i]])
    return list_result


result = list_character(word="ABCXYZ", index_list=[0, 0, 6, 100, 1, 5])
print(result)
