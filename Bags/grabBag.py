class grabBag():
    """Similar to the bag ADT, but the remove operation is replaced with grabItem(), which randomly removes an item from the bag"""
    
    def __init__(self) -> None:
        """Create an empty bag"""
        self._elements = list()

    def __len__(self) -> int:
        """Returns the number of elements in the bag"""
        return len(self._elements)
    
    def contains(self, element: object) -> bool:
        return element in self._elements