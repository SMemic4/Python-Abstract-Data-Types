# Python Abstract Data Types

An **Abstract Data Type** refers to an object or class that are defined by the values and the set of that can be performed on them. This is a project to implement various ADTs for practice and future reference.

For each ADT, I will provide a definition, their operations, and analysis on their time complexity.


Current ADTs:

 * [Bags](#bags)
 * * [Bag](#Bag)
   * [Grab Bag](#grab-bag)

---

## Bags 

### Bag

> A bag is a container that stores a collection in which duplicate values are allowed. The items, each of which is individually stored, have no particular order but they must be comparable

### Details of Implementation 

* Unordered container
* Duplicate elements are allowed
* Mutable elements

### Basic Operations

* **Bag()**: Creates an empty bag
* **length()**: Return the number of tiems stored in the bag. Accessed using the **len()** function
* **contains(***item***)**: Determines if the *item* is contained within the bag and returns the appropriate boolean value. Accessed with the **in** operator
* **add(***item***)**: Adds *item* to the bag
* **remove(***item***)**: Removes *item* from the bag if it exists. Raises an exception otherwise
* **iterator()**: Creates and returns an iterator that can be used to iterate over the collection of items

### Grab Bag

> Similar to the bag ADT, except the **remove()** operation is replaced with **grabItem()** which removes an item at random
