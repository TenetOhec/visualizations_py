# def get_assessment_mark(assessment_name, mark_min, mark_max):
#     input_user = input(f"Enter {assessment_name} mark ({mark_min}-{mark_max}): ")
#     try:
#         mark = int(input_user)
#     except:
#         raise ValueError(f"{assessment_name} mark is invalid")
#     if mark_min <= mark <= mark_max:
#         return mark
#     else:
#         raise ValueError(f"{assessment_name} mark must be between {mark_min} and {mark_max}")
#
#
# try:
#     result = get_assessment_mark("Quiz 4", 0, 50)
#     print(result)
# except ValueError as e:
#     print(e)


# 2
#
# def get_assessment_mark(assessment_name, mark_min, mark_max):
#     # {
#     """
#     Ask user to enter assessment mark and return the mark.
#     Raise ValueError if one of the following occurs:
#     - mark is not an integer
#     - mark is out of range
#     """
#
#     # ask user to enter mark
#     user_input = input("Enter {0} mark ({1}-{2}): "
#                        .format(assessment_name, mark_min, mark_max))
#
#     # check if mark is integer
#     try:
#         mark = int(user_input)
#     except ValueError as e:
#         raise ValueError("{0} mark is invalid".format(assessment_name))
#
#         # check mark between max and min
#     if (mark > mark_max):
#         raise ValueError("{0} mark must be between {1} and {2}"
#                          .format(assessment_name, mark_min, mark_max))
#
#     if (mark < mark_min):
#         raise ValueError("{0} mark must be between {1} and {2}"
#                          .format(assessment_name, mark_min, mark_max))
#
#     return mark
#
#
# # }
#
# # write your code here
# try:
#     assignment_mark = get_assessment_mark("assignment", 0, 20)
#     project_mark = get_assessment_mark("project", 0, 30)
#     final_mark = get_assessment_mark("final exam", 0, 50)
#     Total_mark = assignment_mark + project_mark + final_mark
#     print("Total mark: {0}".format(Total_mark))
# except ValueError as e:
#     print(f"Error: {e}")

# 3

# class TreeNode:
# #{
#     """
#     Representing a tree node consisting of
#     - datum: the datum stored at the node
#     - left: reference to the left child node
#     - right: reference to the right child node
#     """
#
#     def __init__(self, datum, left, right):
#         self.datum = datum
#         self.left = left
#         self.right = right
#
# #}
#
# class MyBinaryTree:
# #{
#     """
#     Implementation of a binary tree
#     """
#
#     def __init__(self):
#         self.root = None
#     #{
#         """
#         Constructs an empty tree
#         """
#
#     #}
#
#     def print_in_order(self):
#     #{
#         if self != None:
#             result = self.datum
#         """
#         Use in-order traversal and print each tree node's datum
#         """
#
#     #}
#
#     def print_pre_order(self):
#     #{
#         """
#         Use pre-order traversal and print each tree node's datum
#         """
#
#     #}
#
#     def print_post_order(self):
#     #{
#         """
#         Use post-order traversal and print each tree node's datum
#         """
#
#     #}
#
# #}

class TreeNode:
    """
    Representing a tree node consisting of
    - datum: the datum stored at the node
    - left: reference to the left child node
    - right: reference to the right child node
    """
    def __init__(self, datum, left=None, right=None):
        self.datum = datum
        self.left = left
        self.right = right

class MyBinaryTree:
    """
    Implementation of a binary tree
    """
    def __init__(self):
        """
        Constructs an empty tree
        """
        self.root = None

    def in_order_traversal(self, start, result):
        """
        Helper method for in-order traversal
        """
        if start:
            result = self.in_order_traversal(start.left, result)
            result.append(start.datum)
            result = self.in_order_traversal(start.right, result)
        return result

    def pre_order_traversal(self, start, result):
        """
        Helper method for pre-order traversal
        """
        if start:
            result.append(start.datum)
            result = self.pre_order_traversal(start.left, result)
            result = self.pre_order_traversal(start.right, result)
        return result

    def post_order_traversal(self, start, result):
        """
        Helper method for post-order traversal
        """
        if start:
            result = self.post_order_traversal(start.left, result)
            result = self.post_order_traversal(start.right, result)
            result.append(start.datum)
        return result

    def print_in_order(self):
        """
        Use in-order traversal and print each tree node's datum
        """
        result = self.in_order_traversal(self.root, [])
        print("In-Order Traversal:", result)

    def print_pre_order(self):
        """
        Use pre-order traversal and print each tree node's datum
        """
        result = self.pre_order_traversal(self.root, [])
        print("Pre-Order Traversal:", result)

    def print_post_order(self):
        """
        Use post-order traversal and print each tree node's datum
        """
        result = self.post_order_traversal(self.root, [])
        print("Post-Order Traversal:", result)


tree = MyBinaryTree()
tree.root = TreeNode('A')
tree.root.left = TreeNode('B')
tree.root.right = TreeNode('C')
tree.root.left.left = TreeNode('D')
tree.root.left.right = TreeNode('E')
tree.root.left.right.left = TreeNode('I')
tree.root.left.right.right = TreeNode('J')
tree.root.right.left = TreeNode('F')
tree.root.right.left.left = TreeNode('K')
tree.root.right.left.right = TreeNode('L')
tree.root.right.right = TreeNode('H')
tree.root.right.right.left = TreeNode('M')

# Print traversals
tree.print_in_order()
tree.print_pre_order()
tree.print_post_order()

#
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
# class BinaryTree:
#     def __init__(self, root):
#         self.root = TreeNode(root)
#
#     def insert(self, value):
#         self._insert(self.root, value)
#
#     def _insert(self, node, value):
#         if value < node.data:
#             if node.left is None:
#                 node.left = TreeNode(value)
#             else:
#                 self._insert(node.left, value)
#         else:
#             if node.right is None:
#                 node.right = TreeNode(value)
#             else:
#                 self._insert(node.right, value)
#
#     def in_order_traversal(self, start, result):
#         if start:
#             result = self.in_order_traversal(start.left, result)
#             result.append(start.data)
#             result = self.in_order_traversal(start.right, result)
#         return result
#
#     def print_in_order(self):
#         print("In-Order Traversal:", self.in_order_traversal(self.root, []))
#
# # Example usage:
# tree = BinaryTree(5)
# tree.insert(3)
# tree.insert(7)
# tree.insert(2)
# tree.insert(4)
# tree.insert(6)
# tree.insert(8)
#
# tree.print_in_order()
