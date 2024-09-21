class bag():
    """Implementation of a Bag ADT using a list data structure"""
    
    def __init__(self) -> None:
        """Creates an empty bag"""
        self._items = list()
    
    def __len__(self) -> int:
        """Returns the length of the items in the bag"""
        return len(self._items)
    
    def contains(self, item) -> bool:
        """Determines if a given item exists in the bag"""

        return item in self._items
    
    def add(self, item) -> None:
        """Adds an item to the list"""
        self._items.append(item)

    def remove(self, item) -> object:
        """Removes an item from the bag if it exists and returns it, otherwise raises an exception"""
        assert self.contains(item), "The item does not exist in the bag"
        index = self._items.index(item) 
        return self._items.pop(index)
    
    def __iter__(self):
        """Creates an iterator for the bag"""
        return BagIterator(self._items)
    
    def __str__(self) -> str:
        """Prints what is currently contained in the list"""
        return str(f"The Bag contains: {self._items}")
    

class BagIterator:
    """An iterator for the Bag ADT"""
    def __init__(self, items) -> None:
        self._elements = items
        self._index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index < len(self._elements):
            item = self._elements[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration
        




    