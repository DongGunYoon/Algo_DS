class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)


    def _display_aux(self):
        # Ref: https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python/40885162
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value, None, None)
            return
        else:
            par_node = None
            cur_node = self.root
            direction = ''
            while cur_node:
                if value > cur_node.value:
                    par_node = cur_node
                    cur_node = cur_node.right
                    direction = 'r'
                elif value < cur_node.value:
                    par_node = cur_node
                    cur_node = cur_node.left
                    direction = 'l'
                else:
                    return
            if direction == 'r':
                par_node.right = Node(value, None, None)
            else:
                par_node.left = Node(value, None, None)

    def search(self, value):
        isFound = False
        if self.root is None:
            return isFound
        
        cur_node = self.root
        while cur_node:
            if value > cur_node.value:
                cur_node = cur_node.right
            elif value < cur_node.value:
                cur_node = cur_node.left
            else:
                isFound = True
                return isFound
        
        return isFound

    def remove(self, value):
        if self.root.left is None and self.root.right is None:
            self.root = None
            return

        par_node = None
        cur_node = self.root
        direction = ''
        while cur_node:
            if value > cur_node.value:
                par_node = cur_node
                cur_node = cur_node.right
                direction = 'r'
            elif value < cur_node.value:
                par_node = cur_node
                cur_node = cur_node.left
                direction = 'l'

            # value값과 일치하는 노드 확인 
            # 삭제할 노드 = cur_node
            # 삭제할 노드의 부모 = par_node
            # 부모 노드로부터의 방향 = direction

            else:

                # 자식이 없는 노드 삭제
                if cur_node.left is None and cur_node.right is None:
                    if direction == 'l':
                        par_node.left = None
                    else:
                        par_node.right = None
                    break
                
                # 자식이 오른쪽에만 있는 노드 삭제
                elif cur_node.left is None and cur_node.right is not None:
                    if direction == 'l':
                        par_node.left = cur_node.right
                    else:
                        par_node.right = cur_node.right
                    break
                
                # 자식이 오른쪽에만 있는 노드 삭제
                elif cur_node.left is not None and cur_node.right is None:
                    if direction == 'l':
                        par_node.left = cur_node.left
                    else:
                        par_node.right = cur_node.left
                    break
                
                # 자식이 양쪽 모두에 있는 경우 
                # 왼쪽 서브 트리에서 가장 큰 값을 찾기
                else:
                    prev = cur_node
                    curr = cur_node.left
                    sec_dir = 'l'

                    while curr.right:
                        prev = curr
                        curr = curr.right
                        sec_dir = 'r'

                    # 바로 왼쪽의 노드가 가장 큰 값이었을때
                    if sec_dir == 'l':
                        if direction == 'l':
                            curr.right = prev.right
                            par_node.left = curr
                        else:
                            curr.right = prev.right
                            par_node.right = curr
                        return
                    
                    # 왼쪽의 노드에 더 큰 자식이 존재할때
                    else: 
                        if direction == 'r':
                            prev.right = curr.left
                            par_node.right = curr
                            curr.right = cur_node.right
                            curr.left = cur_node.left
                        else:
                            prev.right = curr.left
                            par_node.left = curr
                            curr.right = cur_node.right
                            curr.left = cur_node.left
                        return
        return


bst = BinarySearchTree()

import random
x = [4, 3, 3.5, 8, 1, 0, 2, 6, 9, 5, 7, 11]
for el in x:
    bst.insert(el)


bst.root.display()

# 모든 상황에 remove() 함수 테스트

bst.remove(3)
bst.remove(8)
bst.remove(2)
bst.remove(7)
bst.remove(6)
bst.remove(1)
bst.remove(5)
bst.remove(9)
bst.remove(11)
bst.remove(0)
bst.remove(3.5)

bst.root.display()