def BinaryTree(r):
    return [r, [], []]


def insertLeft(root, newBranch):
    t = root.pop(1)

    if len(t) > 1:

        root.insert(1, [newBranch, t, []])

    else:

        root.insert(1, [newBranch, [], []])

    return root


def insertRight(root, newBranch):
    t = root.pop(2)

    if len(t) > 1:

        root.insert(2, [newBranch, [], t])

    else:

        root.insert(2, [newBranch, [], []])

    return root


def getRootVal(root):
    return root[0]


def setRootVal(root, newVal):
    root[0] = newVal


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]


def setRootVal(root, newVal):
    root[0] = newVal


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]


def get_str(root):
    if not root:
        return "None"  # 如果树为空，则返回 "None"

    # 获取根节点的值
    root_val = getRootVal(root)

    # 获取左子树和右子树
    left_child = getLeftChild(root)
    right_child = getRightChild(root)

    # 递归处理左子树和右子树
    left_str = get_str(left_child)
    right_str = get_str(right_child)

    # 格式化输出字符串
    result_str = f"{left_str} <--({root_val})--> {right_str}"

    return result_str


def BinaryTree_str(root):
    print(get_str(root))



# def BinaryTree_str(root):
#     if not root:
#         return "空树"  # 如果树为空，则返回 "空树"
#
#     stack = [root]
#     result_str = ""
#
#     while stack:
#         current_node = stack.pop()
#
#         root_val = getRootVal(current_node)
#         left_child = getLeftChild(current_node)
#         right_child = getRightChild(current_node)
#
#         left_str = BinaryTree_str(left_child)
#         right_str = BinaryTree_str(right_child)
#
#         result_str += f"{left_str} <--({root_val})--> {right_str}"
#
#         if left_child:
#             stack.append(left_child)
#         if right_child:
#             stack.append(right_child)
#
#     return result_str


r = BinaryTree(3)
insertLeft(r, 4)
insertLeft(r, 5)
insertRight(r, 6)
insertRight(r, 7)
print(r)


# 转换为字符串并输出
# tree_str = get_str(r)
# print(tree_str)

BinaryTree_str(r)

# l = getLeftChild(r)
# print(l)
# setRootVal(l, 9)
# print(r)
# insertLeft(l, 11)
# print(r)
# print(getRightChild(getRightChild(r)))
