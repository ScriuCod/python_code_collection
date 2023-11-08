def findClosestValueInBst(tree, target):
    # Base case: We've run off the end of the tree
    if not tree:
        return float("inf")

    next_node = tree.right
    if tree.value > target:
        next_node = tree.left

    closest_node = findClosestValueInBst(next_node, target)

    closest = closest_node if abs(closest_node - target) < abs(tree.value - target) else tree.value

    return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
