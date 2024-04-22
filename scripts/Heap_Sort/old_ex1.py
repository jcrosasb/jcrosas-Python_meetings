def swap(lst: list, index_1: int, index_2: int) -> None:
    '''Function to swap elements in index_1 and index_2 in a list'''
    lst[index_1], lst[index_2] = lst[index_2], lst[index_1]


def heapify(data: list) -> None:
        '''Function to heapify a list in-place. 
           Parameters:
                * data: (List) the list to be heapified
           Returns:
                * The list in the proper MaxHeap order'''       
        if len(data) % 2 == 0:  # First node with children
            index = len(data) // 2
        else:
            index = len(data) // 2 - 1
        while index >= 0:
            while True:
                largest = index
                left_index = 2 * index + 1
                right_index = 2 * index + 2
                if left_index < len(data):  # Check if left child exists
                    if data[left_index] > data[largest]:
                        largest = left_index
                if right_index < len(data):  # Check if right child exists
                    if data[right_index] > data[largest]:
                        largest = right_index
                if largest != index:  # Swap if current index does not correspond with largest
                    swap(data, index, largest)
                    index = largest
                else:
                    break
            index -= 1


class MaxHeap:

    def __init__(self, data):
        '''Initializer of a MaxHeap.
           Parameters:
                * data: (List) values to be added to MaxHeap'''
        self.data = data


    def _left_child(self, index):
        '''Method to get the left child index of a parent located at 'index'
           Parameters:
                * index: (Integer) the index of the parent
           Returns:
                * (Integer) the index of the left child'''
        return 2 * index + 1
    

    def _right_child(self, index):
        '''Method to get the right child index of a parent located at 'index'
           Parameters:
                * index: (Integer) the index of the parent
           Returns:
                * (Integer) the index of the right child'''
        return 2 * index + 2
    

    def heapify(self):
        '''Method to heapify the MaxHeap object. 
           Returns:
                * The data of MaxHeap in the proper MaxHeap order'''
        index = 0
        while index < len(self.data):
            data_ = self.data
            current = self.data[index]
            left_index = self._left_child(index)
            right_index = self._right_child(index)
            #left = self.data[left_index]
            #right = self.data[right_index]

            if left_index < len(self.data):  # Check if left child exists
                if current < self.data[left_index]:
                    swap(self.data, index, left_index)
            if right_index < len(self.data):  # Check if right child exists
                if current < self.data[right_index]:
                    swap(self.data, index, right_index)
            index += 1
        return self.data
       
    

    def heapsort(self):
        
        data = self.data
       
        heapify(data)
        print(data)

        swap(data, 0, len(data)-1)
        print(data)

        heapify(data[0:len(data)-2])
        print(data)


if __name__ == '__main__':

    #data =  [12, 11, 13, 5, 6, 7]
    #data = [4, 10, 3, 5, 1]
    
    data = [2,8,5,3,9,1]

    max_heap = MaxHeap(data)

    max_heap.heapsort()

    

   

   



