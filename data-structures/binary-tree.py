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

def isSameTree(p: Node, q: Node) -> bool:
    if not p and not q:
        return True
    if not p or not q or p.data != q.data:
        return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

# tree = ['g', 'c', 'b', 'a', 'e', 'd', 'f', 'i', 'h', 'j', 'k']
# tree = [1,None,2]
# tree = [3,9,20,None,None,15,7]

# root = init_tree(tree)
# maxDepth(root)

# p = [1,2,3]
# q = [1,2,3]

# p_root = init_tree(p)
# q_root = init_tree(q)

# print(isSameTree(p_root, q_root))

#--------------------------------------------------------------

class BSTIterator:

    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        res = self.stack.pop()
        cur = res.right
        while cur:
            self.stack.append(cur)
            cur = cur.left

        return res.data

    def hasNext(self) -> bool:
        return self.stack != []

bst_tree = [7, 3, 15, None, None, 9, 20]

root_bst = init_tree(bst_tree)

bSTIterator = BSTIterator(root_bst)
print(bSTIterator.next())   
print(bSTIterator.next())   
print(bSTIterator.hasNext())
print(bSTIterator.next())   
print(bSTIterator.hasNext())
print(bSTIterator.next())   
print(bSTIterator.hasNext())
print(bSTIterator.next())   
print(bSTIterator.hasNext())