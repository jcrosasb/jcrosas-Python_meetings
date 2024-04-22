class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.root = None


    def insert(self, value):
        new_node = Node(value=value)
        if self.root is None:
            self.root = new_node
            return True
        queue = [self.root]
        i = 0
        while queue:
            current_node = queue[i]
            if current_node.left is None:
                current_node.left = new_node
                return True
            else:
                queue.append(current_node.left)
            if current_node.right is None:
                current_node.right = new_node
                return True
            else:
                queue.append(current_node.right)
            i += 1
        
  

    def print_tree(self):
        def print_helper(node, depth):
            if node:
                print_helper(node.right, depth + 1)
                print("   " * depth + str(node.value))
                print_helper(node.left, depth + 1)

        print_helper(self.root, 0)


    def print_level(self, level):
        if self.root is None:
            print("Tree is empty")
            return

        queue = [(self.root, 1)]
        while queue:
            current_node, current_level = queue.pop(0)
            if current_level == level:
                print(current_node.value, end=" ")
            elif current_level > level:
                break  # If we've passed the desired level, we stop traversing further
            else:
                if current_node.left:
                    queue.append((current_node.left, current_level + 1))
                if current_node.right:
                    queue.append((current_node.right, current_level + 1))

    

    # def insert(self, value):
    #     new_node = Node(value=value)
    #     if self.root is None:
    #         self.root = new_node
    #         return True
    #     queue = [self.root]
    #     while queue:
    #         current_node = queue.pop(0)
    #         print(current_node.value)
    #         if current_node.left is None:
    #             current_node.left = new_node
    #             return True
    #         elif current_node.right is None:
    #             current_node.right = new_node
    #             return True
    #         if current_node.left:
    #             queue.append(current_node.left)
    #         if current_node.right:
    #             queue.append(current_node.right)


if __name__ == '__main__':

    binary_tree = BinaryTree()

    # data = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]

    # for number in data:
    #     binary_tree.insert(number)

    # print(data[:1])
    # print(data[1:3])
    # print(data[3:7])

    binary_tree.insert(3)
    print(binary_tree.root.value)

    binary_tree.insert(5)
    print(binary_tree.root.left.value)

    binary_tree.insert(1)
    print(binary_tree.root.right.value)

    binary_tree.insert(6)
    print(binary_tree.root.left.left.value)

    binary_tree.insert(2)
    print(binary_tree.root.left.right.value)

    binary_tree.insert(0)
    print(binary_tree.root.right.left.value)

    binary_tree.insert(8)
    print(binary_tree.root.right.right.value)

    binary_tree.insert(None)
    print(binary_tree.root.left.left.left.value)

    binary_tree.insert(None)
    print(binary_tree.root.left.left.right.value)

    binary_tree.insert(7)
    print(binary_tree.root.left.right.left.value)

    binary_tree.print_tree()

    print(binary_tree.print_level(3))
 
