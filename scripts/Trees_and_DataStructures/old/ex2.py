class Node:

    def __init__(self, value):
        '''Initializer of Node for BinaryTree. Each Node is assigned a 'value', 
           with attributes 'left' and 'right' set to None
           Parameters:
                * value: (Integer) the value of the node to be inserted'''
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        '''Initializer of BinaryTree. Only the root of the tree 
           is created (assigned None)'''
        self.root = None


    def level_order_insert(self, value):
        '''Method to insert a new node on binary tree. The order of insertion will be
           top-to-bottom, left-to-right. To insert each node, class Node is used.
           Parameters:
                * value: (Integer) the value of the node to be inserted'''
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
    

    def traverse(self):
        '''Method to traverse a binary tree. The method relies on the tree being filled
           from top-to-bottom, left-to-right. In this way, iteration stops once 
           a node is not found. Nodes whose values are 'None' are omitted
           Returns:
                * A list containing the value of all non-None nodes from 
                  top-to-bottom, left-to-right'''
        if not self.root:
            raise ValueError('The binary tree is empty')
        nodes = [self.root]
        index = 0
        while nodes:
            if nodes[index].left:
                nodes.append(nodes[index].left) if nodes[index].left.value != None else None
            else:
                return [node.value for node in nodes]
            if nodes[index].right:
                nodes.append(nodes[index].right) if nodes[index].right.value != None else None
            else:
                return [node.value for node in nodes]
            index += 1


    def find_path(self, target):
        '''Method to find the path from the root of a binary tree to a target
           Parameters:
                * target: (Node) the target node to which we want to get the path
           Returns:
                * path: (List) the path with all nodes appended'''
        path = []
        return self._find_path_helper(current_node=self.root, 
                                      path=path, 
                                      target=target)
        

    def _find_path_helper(self, current_node, path, target):
        '''Recursive helper method to find the path from one node (current_node) to 
           another node (target)
           Parameters:
                * current_node: (Node) the initial node from which we find the path
                * path: (List) the list on which we save the nodes to the value
                * target: (Node) the target node to which we want to get the path
           Returns:
                * path: (List) the path with all nodes appended'''
        if not self.root:
            raise ValueError('The binary tree is empty')
        path.append(current_node.value)
        if current_node.value == target:
            return path
        if ((current_node.left) and self._find_path_helper(current_node=current_node.left,
                                                            path=path, 
                                                            target=target)) or \
           ((current_node.right) and self._find_path_helper(current_node=current_node.right, 
                                                            path=path, 
                                                            target=target)):
            return path
        path.pop()
        return None  
    
    def LCA(self, p, q):
        '''Method to find the Lowest Common Ancestor (lca).
           Parameters:
                * p: (Integer) first node
                * q: (Integer) second node
           Returns:
                * lca: (Integer) lowest common ancestor for p and q'''
        p_path = self.find_path(target=p)
        q_path = self.find_path(target=q)

        index = 0
        while p_path[index] == q_path[index]:
            lca = p_path[index]
            index += 1
        return lca

if __name__ == '__main__':

    binary_tree = BinaryTree()

    data = [3, 5, 1, 0, 2, 0, 8, None, None, 7, 4]

    #data = [1, 2, 3, 4, 5, 8, None, None, None, 6, 7, 9, 10]

    #data = [1,2,3,4,5,6,2]

    for number in data:
        binary_tree.level_order_insert(number)

    path = []
#    print(binary_tree._find_path_helper(binary_tree.root, path, 7))

    print(binary_tree.find_path(0))
    # print(binary_tree.find_path(6))

    print(binary_tree.LCA(0,8))

    # print(binary_tree.traverse())

    #binary_tree.print_binary_tree()

    # print(binary_tree.root.value)

    # print(binary_tree.root.left.value)

    # print(binary_tree.root.right.value)

    # print(binary_tree.root.left.left.value)

    # print(binary_tree.root.left.right.value)

    # print(binary_tree.root.right.left.value)

    # print(binary_tree.root.right.right.value)

    # print(binary_tree.root.left.left.left.value)

    # print(binary_tree.root.left.left.right.value)

    # print(binary_tree.root.left.right.left.value)

    # print(binary_tree.root.left.right.right.value)

    # print(binary_tree.root.right.left.left.value)

    # print(binary_tree.root.right.left.right.value)


    # # print(binary_tree.left_height())
    # # print(binary_tree.right_height())
    # #print(binary_tree.get_height())

    # binary_tree.print_binary_tree()
    # #print(binary_tree.get_level(2))

    

 