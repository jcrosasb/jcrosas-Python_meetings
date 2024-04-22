def swap(lst: list, index_1: int, index_2: int) -> None:
    '''Function to swap elements in index_1 and index_2 in a list'''
    lst[index_1], lst[index_2] = lst[index_2], lst[index_1]


def heapify(data:list, skip:int= 0) -> None:
        '''Function to heapify a list in-place. If 'skip' is provided,
           element number 'skip' from the end backwards will be ignored.
           Parameters:
                * data: (List) the list to be heapified
                * skip: (Integer) element number counting 
                        from the end backwards
           Returns:
                * The list in the proper MaxHeap order'''       
        index = ((len(data)-skip) // 2 - 1)  # First node with children
        while index >= 0:
            while True:
                largest = index
                left_index = 2 * index + 1
                right_index = 2 * index + 2
                if left_index < len(data)-skip:  # Check if left child exists
                    if data[left_index] > data[largest]:
                        largest = left_index
                if right_index < len(data)-skip:  # Check if right child exists
                    if data[right_index] > data[largest]:
                        largest = right_index
                if largest != index:  # Swap if current index does not correspond with largest
                    swap(data, index, largest)
                    index = largest
                else:
                    break
            index -= 1


class ArrayNumber:
    ''' Class ArrayNumber serves to create array-like objects made up of numbers.'''
    def __init__(self, data):
        '''Initialize a new instance of Array Object
            Attributes:
                data: numbers to be included in ArrayNumber object'''
        self.data = data


    def heapsort(self):
        '''Method to sort ArrayNumber in-place using HeapSort method. It employs the 
           external functions 'swap' and 'heapify'
           Returns:
                * The ArrayNumber object with elements sorted in ascending order'''
        index = len(self.data)-1
        skip = 0  # Skip the last element from the heapifying process
        while index >= 0:
            heapify(data=self.data, skip=skip)  # Heapify self.data, except the last 'skip' elements
            swap(data, 0, index)  # Swap the first and last elements
            index -= 1
            skip += 1


    def __str__(self):
        '''Method to print ArrayNumber object'''
        return f'{self.data}'


if __name__ == '__main__':

    data =  [12, 11, 13, 5, 6, 7]
    #data = [4, 10, 3, 5, 1]
    #data = [2,8,5,3,9,1]

    max_heap = ArrayNumber(data)

    max_heap.heapsort()

    print(max_heap)


    

   

   



