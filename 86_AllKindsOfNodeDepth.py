"""
o(nlogn) time and O(h) space
"""


def allKindsOfNodeDepths(root):
    sumOfAllDepths=0
    stack=[root]
    while len(stack)>0:
        node=stack.pop()
        if node is None:
            continue
        sumOfAllDepths +=nodeDepths(node)
        stack.append(node.left)
        stack.append(node.right)


def nodeDepths(node,depth=0):
    if node is None:
        return 0
    return depth+nodeDepths(node.left,depth+1)+nodeDepths(node.right,depth+1)

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


"""
O(nlogn) time and O(h) space
"""


def allKindsOfNodeDepths(root):
    if root is None:
        return 0
    return allKindsOfNodeDepths(root.left)+allKindsOfNodeDepths(root.right)+nodeDepths(root)

def nodeDepths(node,depth=0):
    if node is None:
        return 0
    return depth+nodeDepths(node.left,depth+1)+nodeDepths(node.right,depth+1)

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



"""
O(n) time and O(h) space

"""
def allKindsOfNodeDepths(root):
    return getTreeInfo(root).sumOfAllDepths

def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(0,0,0)

    leftTreeInfo=getTreeInfo(tree.left)
    rightTreeInfo=getTreeInfo(tree.right)

    sumOfLeftDepths=leftTreeInfo.sumOfDepths+leftTreeInfo.numNodesInTree
    sumOfRightDepths=rightTreeInfo.sumOfDepths+rightTreeInfo.numNodesInTree

    numNodesInTree=1+leftTreeInfo.numNodesInTree+ rightTreeInfo.numNodesInTree
    sumOfDepths=sumOfLeftDepths+sumOfRightDepths

    sumOfAllDepths=sumOfDepths+leftTreeInfo.sumOfAllDepths+rightTreeInfo.sumOfAllDepths

    return TreeInfo(numNodesInTree,sumOfDepths,sumOfAllDepths)


class TreeInfo:
    def __init__(self,numNodesInTree,sumOfDepths,sumOfAllDepths):
        self.numNodesInTree = numNodesInTree
        self.sumOfDepths=sumOfDepths
        self.sumOfAllDepths=sumOfAllDepths


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
