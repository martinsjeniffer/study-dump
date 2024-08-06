# tree = ['g', 'c', 'b', 'a', 'e', 'd', 'f', 'i', 'h', 'j', 'k']
# tree = [3,9,20,None,None,15,7]
tree = [1,None,2]

class Node:
    def __init__(self, data):
        self.left  = None
        self.right = None
        self.data  = data

    def insert(self, input_data):
        if input_data is None:
            return

        # no data on the root? put data there
        if self.data == None:
            self.data = input_data
        else:
            if input_data < self.data:
                # no child node so put in left as the child
                if self.left is None: 
                    self.left = Node(input_data)
                # recursion going deeper in the tree
                else:
                    self.left.insert(input_data)

            elif input_data > self.data:
                if self.right is None:
                    self.right = Node(input_data)
                else:
                    self.right.insert(input_data)

def init_tree(tree):
    root = Node(tree[0])

    for n in range(1,len(tree)):
        root.insert(tree[n])

    return root

def maxDepth(root):
    if not root:
        return 0
    
    l = 1 + maxDepth(root.left)
    r = 1 + maxDepth(root.right)

    print('profundidade maxima:', max(l, r))

    return max(l, r)



root = Node(tree[0])

for n in range(1,len(tree)):
    root.insert(tree[n])

maxDepth(root)

