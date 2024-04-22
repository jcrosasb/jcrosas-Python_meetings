class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)

    def insert(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            curr_node = queue.pop(0)
            if curr_node.left is None:
                curr_node.left = node
                break
            else:
                queue.append(curr_node.left)
            if curr_node.right is None:
                curr_node.right = node
                break
            else:
                queue.append(curr_node.right)


if __name__ == '__main__':

    binary_tree = BinaryTree(3)

    # data = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]

    # for number in data:
    #     binary_tree.insert(number)

    binary_tree.insert(3)
    print(binary_tree.root.data)

    binary_tree.insert(5)
    print(binary_tree.root.left.data)

    # binary_tree.insert(1)
    #print(binary_tree.root.right.value)

    #binary_tree.insert(6)
    #print(binary_tree.root.left.left.value)