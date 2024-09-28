import random as random

class grabBag():
    """Similar to the bag ADT, but the remove operation is replaced with grabItem(), which randomly removes an item from the bag"""
    
    def __init__(self) -> None:
        """Create an empty bag"""
        self._elements = list()

    def __len__(self) -> int:
        """Returns the number of elements in the bag"""
        return len(self._elements)
    
    def contains(self, element: object) -> bool:
        """Determines if a specific item exists in a bag"""
        return element in self._elements
    
    def add(self, element: object) -> None:
        """Adds a bag to the container"""
        self._elements.append(element)

    def grabItem(self) -> object:
        """Removes and returns an item at random"""
        return self._elements.pop(random.randint(0, len(self._elements) - 1))
    
    def iter(self) -> object:
        """Returns an iter for the object"""
        return grabBagIterator(self._elements)
    
    def str(self) -> str:
        """Displays the contents of the bag"""
        return str(f"The Bag contains: {self._elements}")


class grabBagIterator:
    """Creates an iterator for the grabbag class"""
    def __init__(self, element_list) -> None:
        self._elements = element_list
        self._counter = 0
    
    def __iter__(self):
        return self
    
    def __next__(self) -> object:
        if self._counter < len(self._elements):
            item = self._elements[self._counter]
            self._counter += 1
            return item
        else:
            raise StopIteration


