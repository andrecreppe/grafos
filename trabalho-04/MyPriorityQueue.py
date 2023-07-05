from queue import PriorityQueue

class MyPriorityQueue(PriorityQueue):
    def __init__(self):
        super().__init__()
        self.elements = {}  # Dictionary to track elements and priorities

    def put(self, item, priority):
        super().put((priority, item))  # Add element to the priority queue
        self.elements[item] = priority  # Update the elements dictionary

    def update_priority(self, item, new_priority):
        if item not in self.elements:
            raise ValueError("Item not found in the priority queue.")

        del self.elements[item]  # Remove the item from the elements dictionary

        # Remove and re-add the item with the updated priority
        with self.mutex:
            self.queue = [(p, i) for p, i in self.queue if i != item]
            self.elements[item] = new_priority
            self.queue.append((new_priority, item))
            self._put((new_priority, item))


