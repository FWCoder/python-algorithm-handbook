# Create node class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    # the height of a node is the number of edges on the longest path between that node and a leaf
    def get_height(self):
        pass

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

# Create BinaryTree Class
class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)
    # Helper method to print out all traversal type
    def printTree(self, printType):
        if(printType == "pre_order"):
            return self.pre_order_print(self.root, "")
        elif(printType == "in_order"):
            return self.in_order_print(self.root, "")
        elif(printType == "post_order"):
            return self.post_order_print(self.root, "")
        elif(printType == "level_order"):
            return self.level_order_print(self.root)
        elif(printType == "reverse_level_order"):
            return self.reverse_level_order_print(self.root)
        else:
            return ("Traversal type "+ str(printType)+ " is not supported.")

    # Pre order depth first search: root->left->right
    def pre_order_print(self, start, traversal):
        if start:
            traversal += (str(start.value)+"-")
            traversal = self.pre_order_print(start.left, traversal)
            traversal = self.pre_order_print(start.right, traversal)
        return traversal
    
    # In order depth first search: left->root->right
    def in_order_print(self, start, traversal):
        if start:
            traversal = self.in_order_print(start.left, traversal)
            traversal += (str(start.value)+"-")            
            traversal = self.in_order_print(start.right, traversal)
        return traversal
    
    # Post order depth first search: left->right->root
    def post_order_print(self, start, traversal):
        if start:
            traversal = self.post_order_print(start.left, traversal)                        
            traversal = self.post_order_print(start.right, traversal)
            traversal += (str(start.value)+"-")
        return traversal
    
    # Level order dfs: print base on order 1-2-3-4-5-6-7
    def level_order_print(self, start):
        if start is None:
            return
        queue = Queue()
        queue.enqueue(start)
        
        traversal = ''
        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()

            if (node.left):
                queue.enqueue(node.left)

            if (node.right):
                queue.enqueue(node.right)

        return traversal
    
    def reverse_level_order_print(self, start):
        if start is None:
            return

        queue = Queue()
        stack = Stack()

        queue.enqueue(start)
              
        traversal = ''

        while len(queue) > 0:            
            node = queue.dequeue()            
            stack.push(node)
            
            if (node.right):
                queue.enqueue(node.right)

            if (node.left):
                queue.enqueue(node.left)            

        while len(stack) > 0:
            node=stack.pop()
            traversal += str(node.value)+"-"

        return traversal
    
    # the height of a tree is the height of its root node
    def get_height(self, node):
        if (node is None):
            return -1
        
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)

        return 1 + max(left_height, right_height)

    def get_size_dynamically(self, node):
        if (node is None):
            return 0
        return 1 + self.get_size_dynamically(node.left) + self.get_size_dynamically(node.right)
        
    def get_size(self):
        if (self.root is None):
            return 0

        stack = Stack()
        stack.push(self.root)
        size = 1

        while stack:
            node = stack.pop()
            if (node.left):
                size += 1
                stack.push(node.left)
            
            if (node.right):
                size += 1
                stack.push(node.right)

        return size

def topView(root):
  #Write your code here
    if root is None:
        return

    queue = Queue()
    stack = Stack()

    if root.left:        
        queue.enqueue(root.left)
    
    traversal = ''
    while (len(queue) > 0):
        node = queue.dequeue()
        stack.push(node)
        if node.left:
            queue.enqueue(node.left)
  
    while (len(stack) > 0):
        node = stack.pop()
        traversal += (str(node.value)) + " "

    queue = Queue()
    queue.enqueue(root)
    
    while len(queue) > 0:
        node = queue.dequeue()
        traversal += (str(node.value)) + " "
        if node.right:
            queue.enqueue(node.right)
                
    print (traversal)




        

# Create a sample tree data
#      1
#    /   \
#   2     3
#  / \   / \
# 4   5 6   7

bt = BinaryTree(1)
bt.root.left = Node(2)
bt.root.right = Node(3)
bt.root.left.left = Node(4)
bt.root.left.right = Node(5)
bt.root.right.left = Node(6)
bt.root.right.right = Node(7)
bt.root.right.right.right = Node(8)

# print("pre order dfs: " + bt.printTree("pre_order"))
# print("in order dfs: " + bt.printTree("in_order"))
# print("post order dfs: " + bt.printTree("post_order"))
# print("level order dfs: " + bt.printTree("level_order"))
# print("reverse level order dfs: " + bt.printTree("reverse_level_order"))
# print("height of the tree: " + str(bt.get_height(bt.root)))
# print("size of the tree: " + str(bt.get_size()))
# print("size of the tree: " + str(bt.get_size()))
topView(bt.root)

bt = BinaryTree(1)
bt.root.left = Node(3)
bt.root.left.right = Node(5)
bt.root.left.left = Node(6)
bt.root.left.left.left = Node(7)
bt.root.left.left.right = Node(3)
bt.root.right = Node(2)
bt.root.right.right = Node(5)
bt.root.right.right.right = Node(6)
bt.root.right.right.left = Node(3)
bt.root.right.right.left.right = Node(4)

topView(bt.root)