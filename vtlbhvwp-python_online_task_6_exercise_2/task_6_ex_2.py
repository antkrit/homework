"""
Create CustomList – the linked list of values of random type, which size changes dynamically and has an ability to index
elements.

The task requires implementation of the following functionality:
• Create the empty user list and the one based on enumeration of values separated by commas. The elements are stored
in form of unidirectional linked list. Nodes of this list must be implemented in class Item.
    Method name: __init__(self, *data) -> None;
• Add and remove elements.
    Method names: append(self, value) -> None - to add to the end,
                add_start(self, value) -> None - to add to the start,
                remove(self, value) -> None - to remove the first occurrence of given value;
• Operations with elements by index. Negative indexing is not necessary.
    Method names: __getitem__(self, index) -> Any,
                __setitem__(self, index, data) -> None,
                __delitem__(self, index) -> None;
• Receive index of predetermined value.
    Method name: find(self, value) -> Any;
• Clear the list.
    Method name: clear(self) -> None;
• Receive lists length.
    Method name: __len__(self) -> int;
• Make CustomList iterable to use in for-loops;
    Method name: __iter__(self);
• Raise exceptions when:
    find() or remove() don't find specific value
    index out of bound at methods __getitem__, __setitem__, __delitem__.


Notes:
    The class CustomList must not inherit from anything (except from the object, of course).
    Function names should be as described above. Additional functionality has no naming requirements.
    Indexation starts with 0.
    List length changes while adding and removing elements.
    Inside the list the elements are connected as in a linked list, starting with link to head.
"""


class Item:

    def __init__(self, data):
        self.data = data
        self.ref = None


class CustomList:

    def __init__(self, *data):
        self.length = 0
        self.start_node = None

        for value in data:
            self.append(value)

        self.iter_item = self.start_node

    def print_list(self):
        if self.start_node:
            item = self.start_node

            while item is not None:
                print(item.data, end=" ")
                item = item.ref

        return

    def append(self, value) -> None:
        new_item = Item(value)
        self.length += 1

        if self.start_node:
            item = self.start_node

            while item.ref is not None:
                item = item.ref
            item.ref = new_item
        else:
            self.start_node = new_item

    def add_start(self, value) -> None:
        self.length += 1
        new_item = Item(value)
        new_item.ref = self.start_node
        self.start_node = new_item

    def remove(self, value) -> None:
        if self.start_node:
            if self.start_node.data == value:
                self.start_node = self.start_node.ref
                return

            item = self.start_node
            while item.ref is not None:
                if item.ref.data == value:
                    break
                item = item.ref

            if not item.ref:
                raise ValueError("item not found")
            item.ref = item.ref.ref
            self.length -= 1

    def find(self, value):
        if self.start_node:
            index = 0
            item = self.start_node

            if item.data == value:
                self.start_node = self.start_node.ref
                return index

            while item.ref is not None:
                if item.ref.data == value:
                    break
                item = item.ref
                index += 1

            if not item.ref:
                raise ValueError("item not found")

            return index+1

    def clear(self) -> None:
        self.length = 0
        self.start_node = None

    def __getitem__(self, index):
        if self.start_node:
            if not isinstance(index, int) or not 0 <= index < self.length:
                raise IndexError

            item = self.start_node
            for _ in range(index):
                item = item.ref

            return item.data

    def __setitem__(self, index, value) -> None:
        if self.start_node:
            if not isinstance(index, int) or not 0 <= index < self.length:
                raise IndexError

            new_item = Item(value)
            item = self.start_node
            if not index:
                new_item.ref = self.start_node.ref
                self.start_node = new_item
                return

            for _ in range(index-1):
                item = item.ref

            new_item.ref = item.ref.ref
            item.ref = new_item

    def __delitem__(self, index) -> None:
        if self.start_node:
            if not isinstance(index, int) or not 0 <= index < self.length:
                raise IndexError

            item = self.start_node
            self.length -= 1
            if not index:
                self.start_node = self.start_node.ref
                return

            for _ in range(index-1):
                item = item.ref

            item.ref = item.ref.ref

    def __len__(self):
        return self.length

    def __iter__(self):
        self.iter_item = self.start_node
        return self

    def __next__(self):
        if self.iter_item:
            result = self.iter_item.data
            self.iter_item = self.iter_item.ref
            return result

        raise StopIteration
