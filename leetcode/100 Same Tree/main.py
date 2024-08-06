"""
Given the roots of two binary trees p and q,
write a function to check if they are the same or not.

Two binary trees are considered the same if they are 
structurally identical, and the nodes have the same value.
"""

"""
    SOLUTIONS OBSERVATIONS

    time complexity O(p+q) -> is going to iterate recursivly through both trees in the worst case
"""

def isSameTree(p: Node, q: Node) -> bool:
    if not p and not q:
        return True
    if not p or not q or p.data != q.data:
        return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

