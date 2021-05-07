# Create node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = 0

# Create a queue class for level order dfs
class Queue(object):
    def __init__(self):
        self.items=[]
    
    def enqueue(self, node):
        self.items.insert(0, node)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

# Create a stack class for reverse level order dfs
class Stack(object):    
    def __init__(self):
        self.items=[]

    def push(self, node):
        self.items.append(node)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)
    
    def __len__(self):
        return self.size()
        
class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:            
            self.root = Node(data)
        else:
            self._insert(data, self.root)
    
    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)                
        else:
            print("Value is already presented in the tree!")

    def find(self, data):
        if self.root:            
            return self._find(data, self.root)            
        else: 
            return None
    
    def _find(self, data, cur_node):
        if data > cur_node.data and cur_node.right:            
            return self._find(data, cur_node.right)
        elif data < cur_node.data and cur_node.left:            
            return self.find(data, cur_node.left)  
        elif data == cur_node.data:            
            return True
        else:
            return False
    
    def inorder_print_tree(self):
        if self.root:
            self._inorder_print_tree(self.root)
    
    def _inorder_print_tree(self,node):
        if node:
            self._inorder_print_tree(node.left)
            print(str(node.data))
            self._inorder_print_tree(node.right)
    
    def is_bst(self):
        if self.root:
            if self._is_bst(self.root) is None:
                return True
            return False
        return True

    def _is_bst(self,node):            
        if node.left:            
            if (node.data > node.left.data):                
                return self._is_bst(node.left)
            else:
                return False
        
        if node.right:            
            if (node.data < node.right.data):                
                return self._is_bst(node.right)
            else:
                return False

def topView(root):
  #Write your code here
    if root is None:
        return

    queue = Queue()
    # stack = Stack()
    # q = []
    m = dict()
    root.level = 0 
    
    queue.enqueue(root)

    while len(queue) > 0:        
        node = queue.dequeue()
        level = node.level

        if level not in m:
            m[level] = node.data

        if node.left:            
            node.left.level = level - 1            
            queue.enqueue(node.left)
        
        if node.right:
            node.right.level = level + 1            
            queue.enqueue(node.right)

    for i in sorted(m):                
        print(str(m[i]), end=" ") 

bst = BST()
bst.insert(2)
bst.insert(4)
bst.insert(5)
bst.insert(6)
bst.insert(1)
bst.insert(10)

# print(bst.find(11))
print(topView(bst.root))

bst = BST()
# 78 25 50 22 66 46 104 98 81 90 68 40 103 77 74 18 69 82 41 4 48 83 67 6 2 95 54 100 99 84 34 88 27 72 32 62 9 56 109 115 33 15 91 29 85 114 112 20 26 30 93 96 87 42 38 60 7 73 35 12 10 57 80 13 52 44 16 70 8 39 107 106 63 24 92 45 75 116 5 61 49 101 71 11 53 43 102 110 1 58 36 28 76 47 113 21 89 51 19 3
bst.insert(37)
bst.insert(23)
bst.insert(108)
bst.insert(59)
bst.insert(86)
bst.insert(64)
bst.insert(94)
bst.insert(14)
bst.insert(105)
bst.insert(17)
bst.insert(111)
bst.insert(65)
bst.insert(55)
bst.insert(31)
bst.insert(79)
bst.insert(97)
inputs=[78,25,50,22,66,46,104,98,81,90,68,40,103,77,74,18,69,82,41,4,48,83,67,6,2,95,54,100,99,84,34,88,27,72,32,62,9,56,109,115,33,15,91,29,85,114,112,20,26,30,93,96,87,42,38,60,7,73,35,12,10,57,80,13,52,44,16,70,8,39,107,106,63,24,92,45,75,116,5,61,49,101,71,11,53,43,102,110,1,58,36,28,76,47,113,21,89,51,19,3]
for input in inputs:
    bst.insert(input)

print(topView(bst.root))

bst = BST()
bst.root = Node(1)
bst.root.left = Node(2)
bst.root.left.right = Node(4)
bst.root.left.right = Node(5)
bst.root.left.right = Node(6)
bst.root.right = Node(3)

print(topView(bst.root))





# tree = BST()
# tree.root = Node(1)
# tree.root.left = Node(2)
# tree.root.right = Node(3)

# print(tree.inorder_print_tree())
# print(tree.is_bst())
# print("-------------------")
# print(bst.inorder_print_tree())
# print(bst.is_bst())
