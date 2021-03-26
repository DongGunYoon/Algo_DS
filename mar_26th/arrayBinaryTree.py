import array

class BinaryTree:
    def __init__(self, arr):
        self.array = array.array('l', arr)    

    def preorder(self):
        def recursive(index):
            nonlocal result

            if index >= len(self.array):
                return

            result += str(self.array[index]) + ' '

            recursive(2*index + 1)
            recursive(2*index + 2)

        result = '['
        recursive(0)

        print(result.rstrip() + ']')

    def inorder(self):
        def recursive(index):
            nonlocal result

            left = index*2 + 1
            right = index*2 + 2

            if left < len(self.array):
                recursive(left)

            result += str(self.array[index]) + ' '
            
            if right < len(self.array):
                recursive(right)
        
        result = '['
        recursive(0)

        print(result.rstrip() + ']')

    def postorder(self):
        def recursive(index):
            nonlocal result

            left = index*2 + 1
            right = index*2 + 2

            if left < len(self.array):
                recursive(left)
            
            if right < len(self.array):
                recursive(right)

            result += str(self.array[index]) + ' '
        
        result = '['
        recursive(0)
        print(result.rstrip() + ']')
    
    def bfs(self, value):
        for elem in self.array:
            if elem == value:
                print('Found it')
                return True
        print("Nothing here")
        return False

    def dfs(self, value):
        isFound = False
        
        def recursive(index):
            nonlocal isFound

            if isFound is True:
                return

            if self.array[index] == value:
                isFound = True
                return

            left = index*2 + 1
            right = index*2 + 2

            if left < len(self.array):
                recursive(left)
            if right < len(self.array):
                recursive(right)
        
        recursive(0)
        return print('Found It') if isFound else print('Nothing Here')

tree = BinaryTree([i for i in range(1, 11)])

tree.preorder()
tree.inorder()
tree.postorder()
tree.bfs(10)
tree.dfs(15)