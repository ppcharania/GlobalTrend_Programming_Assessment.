class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def delete(self, value):
        try:
            index = self.heap.index(value)
            self.heap[index] = self.heap[-1]
            self.heap.pop()
            self._heapify_down(index)
        except ValueError:
            print("Value not found in the heap")

    def get_max(self):
        if self.heap:
            return self.heap[0]
        return None

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        largest = index
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
            largest = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)


heap = MaxHeap()
heap.insert(10)
heap.insert(20)
heap.insert(5)
heap.insert(45)
heap.insert(60)
heap.insert(3)
heap.insert(2)
heap.insert(90)
heap.insert(40)
heap.insert(67)
heap.insert(78)
heap.insert(9)
print(heap.get_max())
heap.delete(90)
print(heap.get_max()) 
