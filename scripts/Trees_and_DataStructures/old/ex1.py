from itertools import accumulate

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


    def _left_height(self):
        current_node = self.root
        height = 1
        while current_node is not None:
            if current_node.left:
               height += 1
            current_node = current_node.left
        return height
    

    def _right_height(self):
        current_node = self.root
        height = 1
        while current_node is not None:
            if current_node.right:
               height += 1
            current_node = current_node.right
        return height
    

    def get_height(self):
        return max(self._left_height(), self._right_height())
    

    def get_level(self, level):
        nodes = []
        queue = [(self.root, 0)]
        i = 0
        while queue:
            current_node, current_level = queue.pop(0)
            if current_level == level:
                nodes.append(current_node.value)
            elif current_level > level:
                break
            else:
                if current_node.left:
                    queue.append((current_node.left, current_level+1))
                if current_node.right:
                    queue.append((current_node.right, current_level+1))      
        return nodes
    

    def traverse(self):
        nodes = [self.root]
        j = 0
        while nodes:
            if nodes[j].left:
                nodes.append(nodes[j].left) if nodes[j].right.value != None else None
                node_value = nodes[j].left.value
            if nodes[j].right:
                nodes.append(nodes[j].right) if nodes[j].right.value != None else None
                node_value = nodes[j].right.value
            else:
                break
            j += 1
        return [node.value for node in nodes]

        # nodes = [self.root]
        # j = 0
        # while nodes:
        #     if nodes[j].left:
        #         if nodes[j].left.value != None:
        #             nodes.append(nodes[j].left)
        #         node_value = nodes[j].left.value
        #     if nodes[j].right:
        #         if nodes[j].right.value != None:
        #             nodes.append(nodes[j].right)
        #         node_value = nodes[j].right.value
        #     if not nodes[j].right:
        #         break
        #     j += 1
        # return [node.value for node in nodes]

    
    def print_binary_tree(self):
       
        height = self.get_height()
        spacing = 9

        nodes = self.get_level(height-1)
        num_nodes = 2 ** (height-1)
        len_nodes = [len(str(node)) for node in nodes]
        len_nodes_c = list(accumulate(len_nodes))

        for level in range(height-1,-1,-1):

            if level == height - 1:
                b = [(i*spacing + len_nodes_c[i-1] + 1) for i in range(1, len(len_nodes))]  # Spacing coords for the begining of each node         
                e = [(i*spacing + len_nodes_c[i]) for i in range(len(len_nodes))]  # Spacing coords for the ending of each node

                if len(b) < (num_nodes - 1):
                    b_acum = b[-1]
                    e_acum = e[-1]
                    for _ in range((num_nodes-1) - len(b)):
                        b_acum += spacing +1
                        e_acum += spacing + 1
                        b.append(b_acum)
                        e.append(e_acum)

                print((' ' * spacing).join(str(node) for node in nodes))  # Print last level
            else:
                for n, s in zip(self.get_level(level), m_between):
                    print(f'{n:>{s}}', end=' ')
                print()

            if level > 0:
                     
                m = [(e[i]+b[i])//2 for i in range(0,len(b),2)]  # Location of nodes of next level
                m_between = [m[0]] + [m[i] - m[i - 1]-1 for i in range(1, len(m))]  # Spacing between nodes of next level

                nodes = self.get_level(level-1)
                len_nodes = [len(str(node)) for node in nodes]

                e = [m[i] + len_nodes[i] for i in range(len(m))]
                b = m[1:]  
            

if __name__ == '__main__':

    binary_tree = BinaryTree()

    #data = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]

    data = [1, 2, 3, 4, 5, 8, None, None, None, 6, 7, 9, 10]

    # for number in data:
    #     binary_tree.insert(number)

    # print(binary_tree.traverse())

    binary_tree.print_binary_tree()

    # print(data[:1])
    # print(data[1:3])
    # print(data[3:7])

    # binary_tree.insert(3)
    # print(binary_tree.root.value)

    # binary_tree.insert(5)
    # print(binary_tree.root.left.value)

    # binary_tree.insert(1)
    # print(binary_tree.root.right.value)

    # binary_tree.insert(6)
    # print(binary_tree.root.left.left.value)

    # binary_tree.insert(2)
    # print(binary_tree.root.left.right.value)

    # binary_tree.insert(0)
    # print(binary_tree.root.right.left.value)

    # binary_tree.insert(8)
    # print(binary_tree.root.right.right.value)

    # binary_tree.insert(None)
    # print(binary_tree.root.left.left.left.value)

    # binary_tree.insert(None)
    # print(binary_tree.root.left.left.right.value)

    # binary_tree.insert(7)
    # print(binary_tree.root.left.right.left.value)

    # binary_tree.insert(4)
    # print(binary_tree.root.left.right.right.value)


    # # print(binary_tree.left_height())
    # # print(binary_tree.right_height())
    # #print(binary_tree.get_height())

    # binary_tree.print_binary_tree()
    # #print(binary_tree.get_level(2))

    

 