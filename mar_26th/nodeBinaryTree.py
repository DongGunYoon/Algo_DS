class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, array):
        node_list = [Node(value, None, None) for value in array]
        for ind, node in enumerate(node_list):
            left = 2 * ind + 1
            right = 2 * ind + 2
            if left < len(node_list):
                node.left = node_list[left]
            if right < len(node_list):
                node.right = node_list[right]

        self.root = node_list[0]

    def preorder(self):
        result = '['
        def recursive(node):
            nonlocal result
            if node is None:
                return
            
            result += str(node.value) + ' '

            recursive(node.left)
            recursive(node.right)
        
        recursive(self.root)
        print(result.rstrip() + ']')

    def inorder(self):
        result = '['
        def recursive(node):
            nonlocal result
            if node is None:
                return

            recursive(node.left)
            result += str(node.value) + ' '
            recursive(node.right)
        
        recursive(self.root)
        print(result.rstrip() + ']')
    
    def postorder(self):
        result = '['
        def recursive(node):
            nonlocal result
            if node is None:
                return

            recursive(node.left)
            recursive(node.right)
            result += str(node.value) + ' '
        
        recursive(self.root)
        print(result.rstrip() + ']')

    def bfs(self, value):
        isFound = False
        queue = [self.root]
        while queue:
            pop = queue.pop(0)
            if pop.value == value:
                isFound = True
                return isFound
            else:
                if pop.left is not None:
                    queue.append(pop.left)
                if pop.right is not None:
                    queue.append(pop.right)
        
        return isFound

    def dfs(self, value):
        isFound = False

        def recursive(node):
            nonlocal isFound

            if node is None:
                return
            
            if node.value == value:
                isFound = True
                return isFound

            recursive(node.left)
            recursive(node.right)
        
        recursive(self.root)
        return isFound

# 1 ~ 10????????? ?????? ????????? ?????? ????????? ??????
nodes = [i for i in range(1, 11)]
# ??????????????? ?????? ????????? ??????
tree = BinaryTree(nodes)

# ?????? ?????? ?????? ?????????
tree.preorder()

# ?????? ?????? ?????????
tree.inorder()

# ?????? ?????? ?????????
tree.postorder()

# dfs ?????? ?????? ?????????
print(tree.dfs(1))
print(tree.dfs(15))

# bfs ?????? ?????? ?????????
print(tree.bfs(5))
print(tree.bfs(12))