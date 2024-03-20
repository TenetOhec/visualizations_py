"""
1

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


def BinaryTree_str(root):
    if not root:
        return "None"
    root_val = getRootVal(root)

    left_child = getLeftChild(root)
    right_child = getRightChild(root)

    if left_child:
        left_val = getRootVal(left_child)
    else:
        left_val = None
    if right_child:
        right_val = getRootVal(right_child)
    else:
        right_val = None

    return f"{left_val} <--({root_val})--> {right_val}"
"""

# 2
# class BinaryHeap:
#
#     def __init__(self):
#
#         self.heapList = [0]
#
#         self.currentSize = 0
#
#     def __str__(self):
#         return str(self.heapList[1:])
#
#     def percUp(self, i):
#
#         while i // 2 > 0:
#
#             if self.heapList[i] < self.heapList[i // 2]:
#                 tmp = self.heapList[i // 2]
#
#                 self.heapList[i // 2] = self.heapList[i]
#
#                 self.heapList[i] = tmp
#
#             i = i // 2
#
#     def insert(self, k):
#
#         self.heapList.append(k)
#
#         self.currentSize = self.currentSize + 1
#
#         self.percUp(self.currentSize)
#
#     def percDown(self, i):
#
#         while (i * 2) <= self.currentSize:
#
#             mc = self.minChild(i)
#
#             if self.heapList[i] > self.heapList[mc]:
#                 tmp = self.heapList[i]
#
#                 self.heapList[i] = self.heapList[mc]
#
#                 self.heapList[mc] = tmp
#
#             i = mc
#
#     def minChild(self, i):
#
#         if i * 2 + 1 > self.currentSize:
#
#             return i * 2
#
#         else:
#
#             if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
#
#                 return i * 2
#
#             else:
#
#                 return i * 2 + 1
#
#     def delMin(self):
#
#         retval = self.heapList[1]
#
#         self.heapList[1] = self.heapList[self.currentSize]
#
#         self.currentSize = self.currentSize - 1
#
#         self.heapList.pop()
#
#         self.percDown(1)
#
#         return retval
#
#     def buildHeap(self, alist):
#
#         i = len(alist) // 2
#
#         self.currentSize = len(alist)
#
#         self.heapList = [0] + alist[:]
#
#         while (i > 0):
#             self.percDown(i)
#
#             i = i - 1

# 3
# class TreeNode:
#     def __init__(self, key, val, left=None, right=None, parent=None):
#         self.key = key
#         self.payload = val
#         self.leftChild = left
#         self.rightChild = right
#         self.parent = parent
#
#     def hasLeftChild(self):
#         return self.leftChild
#
#     def hasRightChild(self):
#         return self.rightChild
#
#     def isLeftChild(self):
#         return self.parent and self.parent.leftChild == self
#
#     def isRightChild(self):
#         return self.parent and self.parent.rightChild == self
#
#     def isRoot(self):
#         return not self.parent
#
#     def isLeaf(self):
#         return not (self.rightChild or self.leftChild)
#
#     def hasAnyChildren(self):
#         return self.rightChild or self.leftChild
#
#     def hasBothChildren(self):
#         return self.rightChild and self.leftChild
#
#     def spliceOut(self):
#         if self.isLeaf():
#             if self.isLeftChild():
#                 self.parent.leftChild = None
#             else:
#                 self.parent.rightChild = None
#         elif self.hasAnyChildren():
#             if self.hasLeftChild():
#                 if self.isLeftChild():
#                     self.parent.leftChild = self.leftChild
#                 else:
#                     self.parent.rightChild = self.leftChild
#                 self.leftChild.parent = self.parent
#             else:
#                 if self.isLeftChild():
#                     self.parent.leftChild = self.rightChild
#                 else:
#                     self.parent.rightChild = self.rightChild
#                 self.rightChild.parent = self.parent
#
#     def findSuccessor(self):
#         succ = None
#         if self.hasRightChild():
#             succ = self.rightChild.findMin()
#         else:
#             if self.parent:
#                 if self.isLeftChild():
#                     succ = self.parent
#                 else:
#                     self.parent.rightChild = None
#                     succ = self.parent.findSuccessor()
#                     self.parent.rightChild = self
#
#         return succ
#
#     def findMin(self):
#         current = self
#         while current.hasLeftChild():
#             current = current.leftChild
#         return current
#
#     def replaceNodeData(self, key, value, lc, rc):
#         self.key = key
#         self.payload = value
#         self.leftChild = lc
#         self.rightChild = rc
#         if self.hasLeftChild():
#             self.leftChild.parent = self
#         if self.hasRightChild():
#             self.rightChild.parent = self
#
#     def __str__(self):
#         result = f"Node:[Key:{self.key},value:{self.payload}],"
#         result += f"Left Child:[key:{self.leftChild.key},value:{self.leftChild.payload}]," if self.hasLeftChild() else "Left Child:None,"
#         result += f"Right Child:[key:{self.rightChild.key},value:{self.rightChild.payload}]," if self.hasRightChild() else "Right Child:None,"
#         result += f"Parent:[key:{self.parent.key},value:{self.parent.payload}]" if self.parent else "Parent:None"
#         return result


# 4

# class TreeNode:
#
#     def __init__(self, key, val, left=None, right=None, parent=None):
#         self.key = key
#         self.payload = val
#         self.leftChild = left
#         self.rightChild = right
#         self.parent = parent
#
#     def hasLeftChild(self):
#         return self.leftChild
#
#     def hasRightChild(self):
#         return self.rightChild
#
#     def isLeftChild(self):
#         return self.parent and self.parent.leftChild == self
#
#     def isRightChild(self):
#         return self.parent and self.parent.rightChild == self
#
#     def isRoot(self):
#         return not self.parent
#
#     def isLeaf(self):
#         return not (self.leftChild or self.rightChild)
#
#     def hasAnyChildren(self):
#         return self.leftChild or self.rightChild
#
#     def hasBothChildren(self):
#         return self.leftChild and self.rightChild
#
#     def spliceOut(self):
#         if self.isLeaf():
#             if self.isLeftChild():
#                 self.parent.leftChild = None
#             else:
#                 self.parent.rightChild = None
#         elif self.hasAnyChildren():
#             if self.hasLeftChild():
#                 if self.isLeftChild():
#                     self.parent.leftChild = self.leftChild
#                 else:
#                     self.parent.rightChild = self.leftChild
#                 self.leftChild.parent = self.parent
#
#             else:
#                 if self.isLeftChild():
#                     self.parent.leftChild = self.rightChild
#                 else:
#                     self.parent.rightChild = self.rightChild
#                 self.rightChild.parent = self.parent
#
#     def findSuccessor(self):
#         succ = None
#         if self.hasRightChild():
#             succ = self.rightChild.findMin()
#         else:
#             if self.parent:
#                 if self.isLeftChild():
#                     succ = self.parent
#                 else:
#                     self.parent.rightChild = None
#                     succ = self.parent.findSuccessor()
#                     self.parent.rightChild = self
#         return succ
#
#     def findMin(self):
#         current = self
#         while current.hasLeftChild():
#             current = current.leftChild
#         return current
#
#     def replaceNodeData(self, key, value, lc, rc):
#         self.key = key
#         self.payload = value
#         self.leftChild = lc
#         self.rightChild = rc
#         if self.hasLeftChild():
#             self.leftChild.parent = self
#         if self.hasRightChild():
#             self.rightChild.parent = self
#
#     def __str__(self):
#         left_child_str = str(self.leftChild) if self.leftChild else "None"
#         right_child_str = str(self.rightChild) if self.rightChild else "None"
#         return f"[node:{{{self.key}: '{self.payload}'}}], Left Child:[{left_child_str}], Right Child:[{right_child_str}]"
#
#
# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
#         self.size = 0
#
#     def length(self):
#         return self.size
#
#     def __len__(self):  # print (len(mytree))
#         return self.size
#
#     def put(self, key, val):
#         if self.root:
#             self._put(key, val, self.root)
#         else:
#             self.root = TreeNode(key, val)
#         self.size = self.size + 1
#
#     def _put(self, key, val, currentNode):
#         if key < currentNode.key:
#             if currentNode.hasLeftChild():
#                 self._put(key, val, currentNode.leftChild)
#             else:
#                 currentNode.leftChild = TreeNode(key, val, parent=currentNode)
#         else:
#             if currentNode.hasRightChild():
#                 self._put(key, val, currentNode.rightChild)
#             else:
#                 currentNode.rightChild = TreeNode(key, val, parent=currentNode)
#
#     def __setitem__(self, k, v):  # mytree[3]="red" : k=3 v="red"
#         self.put(k, v)
#
#     def get(self, key):
#         if self.root:
#             res = self._get(key, self.root)
#             if res:
#                 return res.payload
#             else:
#                 return None
#         else:
#             return None
#
#     def _get(self, key, currentNode):
#         if not currentNode:
#             return None
#         elif currentNode.key == key:
#             return currentNode
#         elif key < currentNode.key:
#             return self._get(key, currentNode.leftChild)
#         else:
#             return self._get(key, currentNode.rightChild)
#
#     def __getitem__(self, key):  # print(mytree[6]): key = 6
#         return self.get(key)
#
#     def __contains__(self, key):  # print(3 in mytree): key = 3
#         if self._get(key, self.root):
#             return True
#         else:
#             return False
#
#     def delete(self, key):
#         if self.size > 1:
#             nodeToRemove = self._get(key, self.root)
#             if nodeToRemove:
#                 self.remove(nodeToRemove)
#                 self.size = self.size - 1
#             else:
#                 raise KeyError('Error, key not in tree')
#         elif self.size == 1 and self.root.key == key:
#             self.root = None
#             self.size = self.size - 1
#         else:
#             raise KeyError('Error, key not in tree')
#
#     def __delitem__(self, key):  # del mytree[3] : key = 3
#         self.delete(key)
#
#     def remove(self, currentNode):
#         if currentNode.isLeaf():  # leaf
#             if currentNode == currentNode.parent.leftChild:
#                 currentNode.parent.leftChild = None
#             else:
#                 currentNode.parent.rightChild = None
#         elif currentNode.hasBothChildren():  # interior
#             succ = currentNode.findSuccessor()
#             succ.spliceOut()
#             currentNode.key = succ.key
#             currentNode.payload = succ.payload
#         else:  # this node has one child
#             if currentNode.hasLeftChild():
#                 if currentNode.isLeftChild():
#                     currentNode.leftChild.parent = currentNode.parent
#                     currentNode.parent.leftChild = currentNode.leftChild
#                 elif currentNode.isRightChild():
#                     currentNode.leftChild.parent = currentNode.parent
#                     currentNode.parent.rightChild = currentNode.leftChild
#                 else:
#                     currentNode.replaceNodeData(
#                         currentNode.leftChild.key, currentNode.leftChild.payload,
#                         currentNode.leftChild.leftChild, currentNode.leftChild.rightChild)
#
#             else:
#                 if currentNode.isLeftChild():
#                     currentNode.rightChild.parent = currentNode.parent
#                     currentNode.parent.leftChild = currentNode.rightChild
#                 elif currentNode.isRightChild():
#                     currentNode.rightChild.parent = currentNode.parent
#                     currentNode.parent.rightChild = currentNode.rightChild
#
#                 else:
#
#                     currentNode.replaceNodeData(
#                         currentNode.rightChild.key, currentNode.rightChild.payload,
#                         currentNode.rightChild.leftChild, currentNode.rightChild.rightChild)
#
#     def __str__(self):
#         return str(self.root)



# 10
# class BinaryTree:
#     def __init__(self, rootObj):
#         self.key = rootObj
#         self.leftChild = None
#         self.rightChild = None
#
#     def insertLeft(self, newNode):
#         if self.leftChild == None:
#             self.leftChild = BinaryTree(newNode)
#         else:
#             t = BinaryTree(newNode)
#             t.leftChild = self.leftChild
#             self.leftChild = t
#
#     def insertRight(self, newNode):
#         if self.rightChild == None:
#             self.rightChild = BinaryTree(newNode)
#         else:
#             t = BinaryTree(newNode)
#             t.rightChild = self.rightChild
#             self.rightChild = t
#
#     def getRightChild(self):
#         return self.rightChild
#
#     def getLeftChild(self):
#         return self.leftChild
#
#     def setRootVal(self, obj):
#         self.key = obj
#
#     def getRootVal(self):
#         return self.key
#
#     def preorder_traversal(self):
#         self._preorder_traversal(self)
#
#     def _preorder_traversal(self, root):
#         if root:
#             print(f"Node {root.getRootVal()} visited")
#             self._preorder_traversal(root.getLeftChild())
#             self._preorder_traversal(root.getRightChild())

# 11
class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.leftChild or self.rightChild)

    def hasAnyChildren(self):
        return self.leftChild or self.rightChild

    def hasBothChildren(self):
        return self.leftChild and self.rightChild

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent

            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def __str__(self):
        left_child_str = str(self.leftChild) if self.leftChild else "None"
        right_child_str = str(self.rightChild) if self.rightChild else "None"
        return f"[node:{{{self.key}: '{self.payload}'}}], Left Child:[{left_child_str}], Right Child:[{right_child_str}]"

    def __iter__(self):
        if self.leftChild:
            for elem in self.leftChild:
                yield elem
        yield self.key
        if self.rightChild:
            for elem in self.rightChild:
                yield elem


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):  # print (len(mytree))
        return self.size

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def __setitem__(self, k, v):  # mytree[3]="red" : k=3 v="red"
        self.put(k, v)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, key):  # print(mytree[6]): key = 6
        return self.get(key)

    def __contains__(self, key):  # print(3 in mytree): key = 3
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):  # del mytree[3] : key = 3
        self.delete(key)

    def remove(self, currentNode):
        if currentNode.isLeaf():  # leaf
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():  # interior
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        else:  # this node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(
                        currentNode.leftChild.key, currentNode.leftChild.payload,
                        currentNode.leftChild.leftChild, currentNode.leftChild.rightChild)

            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild

                else:

                    currentNode.replaceNodeData(
                        currentNode.rightChild.key, currentNode.rightChild.payload,
                        currentNode.rightChild.leftChild, currentNode.rightChild.rightChild)

    def __str__(self):
        return str(self.root)

    def __iter__(self):
        if self.root:
            for elem in self.root:
                yield elem