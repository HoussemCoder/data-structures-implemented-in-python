## Linked List DS Module ##

class LinkedList:

    """ 
    - This class contain the 4 types of linked lists:
    1. Singly linked list
    2. Doubly linked list
    3. Circular linked list
    4. Circular Doubly linked list

    - Each one has its own class and methods.
    - Some methods seem to be similar such as clear or insert.
    - len func refers to a variable to minimize the times of looping through this DS

    """

    class Node:
        """ This class is used for all our DS which produce a node with some global properties """
        def __init__(self, value=None) -> None:
            self.prev = None
            self.value = value
            self.next = None

    class SinglyLL:
        def __init__(self, head=None) -> None:
            self.__head = head if not head else LinkedList.Node(head)
            self.__tail = self.__head
            self.__len = 0 if not self.__head else 1

        def __setitem__(self, index: int, value: object):
            """ change a node value based on its index """
            if index in range(self.__len):
                self[index].value = value

        def __getitem__(self, index: int):
            """ get a node value based on its index """
            return self.getData(index)

        def __delitem__(self, __o: object):
            """ remove a specific item from this DS """
            return self.remove(__o)

        def __contains__(self, __o: object) -> bool:
            """ return True if __o exist in this DS otherwise False """
            return True if type(self.getIndex(__o)) == int or self is __o else False

        def __iter__(self):
            self.index = 0
            return self

        def __next__(self):
            if self.index < self.__len-1:
                self.index += 1
                return self[self.index-1]
            raise StopIteration

        def __add__(self, __o: object):
            """ concatenate 2 data structures if they are from the same class """
            if isinstance(__o, LinkedList.SinglyLL):
                self.__tail.next = __o.__head
                self.__tail = __o.__tail
                self.__len += __o.__len
                return self
            raise TypeError("(+) operator could not wokrs between different classes types")

        def __lt__(self, __o: object) -> bool:
            """ compare the length of two object of the same class """
            if isinstance(__o, LinkedList.SinglyLL):
                return self.__len < __o.__len
            raise TypeError("(<) operator could not wokrs between different classes types")

        def __gt__(self, __o: object) -> bool:
            """ compare the length of two object of the same class """
            if isinstance(__o, LinkedList.SinglyLL):
                return self.__len > __o.__len
            raise TypeError("(>) operator could not wokrs between different classes types")

        def __le__(self, __o: object) -> bool:
            """ compare the length of two object of the same class """
            if isinstance(__o, LinkedList.SinglyLL):
                return self.__len <= __o.__len
            raise TypeError("(<=) operator could not wokrs between different classes types")

        def __ge__(self, __o: object) -> bool:
            """ compare the length of two object of the same class """
            if isinstance(__o, LinkedList.SinglyLL):
                return self.__len >= __o.__len
            raise TypeError("(>=) operator could not wokrs between different classes types")

        def __len__(self) -> int:
            return self.__len

        def __repr__(self) -> str:
            return f"Linked List[type: Singly]({str(self.toList())})"
            
        def __str__(self) -> str:
            return f"({self.toList()})"

        def isEmpty(self) -> bool:
            return self.__len == 0

        def getIndex(self, data):
            f""" raise ValueError if the {self.__class__.__name__} is empty """
            if self.isEmpty():
                raise ValueError(f"Empty {self.__class__.__name__}") 
            elif data == self.__tail.value:
                return self.__len - 1
            curr_item = self.__head
            index = 0
            while curr_item.value != data:
                if curr_item.next is None:
                    return None
                curr_item = curr_item.next
                index += 1
            if curr_item.value == data:
                return index
        
        def getData(self, index=int):
            f""" 1/ index must be an int & in the range of len({self.__class__.__name__}) otherwise it will raise an error.
            2/ to print the value if the node use .value """
            if not isinstance(index, int):
                raise TypeError("index must be an integer")
            if index >= self.__len or index < 0:
                raise IndexError(f"index range must be from 0 to len({self.__class__.__name__})")
            curr_item = self.__head
            count = 0
            while count != index:
                curr_item = curr_item.next
                count += 1
            if count == index:
                return curr_item

        def count(self, data):
            f""" counting the number of the same item in this {self.__class__.__name__} """
            if self.isEmpty():
                raise ValueError(f"empty {self.__class__.__name__}")
            if not self.getIndex(data):
                raise ValueError(f"{data} does not exist")
            curr_item = self.__head
            times = 0
            while curr_item != self.__tail:
                if curr_item.value == data:
                    times += 1
                curr_item = curr_item.next
            if self.__tail.value == data:
                times += 1
            return times

        def fromItr(self, itr):
            f""" make a {self.__class__.__name__} from any iterable in python including dict & str """
            if len(itr) == 0:
                return
            for item in itr:
                self.append(item)
            return

        def toList(self) -> list:
            f""" convert a {self.__class__.__name__} into a python list """
            if self.isEmpty():
                return []
            elif self.__head.next is None:
                return [self.__head.value]
            curr_item = self.__head
            result = []
            while curr_item.next is not None:
                result.append(curr_item.value)
                curr_item = curr_item.next
            result.append(curr_item.value)
            return result

        def append(self, data) -> None:
            f""" insert a node at the end of the {self.__class__.__name__} """
            node = LinkedList.Node(data)
            if self.isEmpty():
                self.__head = node
                self.__tail = node
                self.__len += 1
                return
            if self.__head.next is None:
                self.__head.next = node
                self.__tail = node
                self.__len += 1
                return
            self.__tail.next = node
            self.__tail = node
            self.__len += 1
            return
        
        def insert(self, data, index=0) -> None:
            f""" if the {self.__class__.__name__} is empty so this method will ignore the index arg """
            node = LinkedList.Node(data)
            if self.isEmpty():
                self.__head = node
                self.__tail = node
                self.__len += 1
                return
            if index == 0:
                if self.__tail is None:
                    self.__tail = self.__head
                node.next = self.__head
                self.__head = node
                self.__len += 1
                return
            elif index >= self.__len:
                self.__tail.next = node
                self.__tail = node
                self.__len += 1
                return
            curr_item = self.getData(index-1)
            node.next = curr_item.next
            curr_item.next = node
            self.__tail = node
            self.__len += 1
            return

        def pop(self):
            f""" remove the last element of this {self.__class__.__name__} """
            if self.isEmpty():
                raise ValueError(f"empty {self.__class__.__name__}")
            if self.__head.next is None:
                del_item = self.__head.value
                self.__head = None
                self.__len -= 1
                return  del_item
            del_item = self.__tail.value
            curr_item = self.__head
            while curr_item.next != self.__tail:
                curr_item = curr_item.next
            curr_item.next = None
            self.__tail = curr_item
            self.__len -= 1
            return del_item

        def remove(self, value):
            f""" raise ValueError if the {self.__class__.__name__} is empty or if the value does not exist """
            if self.isEmpty():
                raise ValueError(f"Empty {self.__class__.__name__}")
            elif self.__head.next is None and self.__head.value != value:
                raise ValueError(f"{value} does not exist")
            elif self.__head.value == value:
                self.__head = self.__head.next
                self.__len -= 1
                return
            curr_item = self.__head
            next_item = self.__head.next
            while next_item.value != value:
                if next_item.next is None:
                    raise ValueError(f"{value} does not exist")
                curr_item = next_item
                next_item = next_item.next
            if next_item.next is None:
                curr_item.next = None
                self.__tail = curr_item
                self.__len -= 1
                return
            curr_item.next = next_item.next
            self.__len -= 1
            return

        def clear(self):
            f""" remove all this {self.__class__.__name__} elements """
            self.__head = None
            self.__tail = None
            self.__len = 0

        def display(self):
            f""" showing this {self.__class__.__name__} in a nice & readable way """
            if self.isEmpty():
                return
            elif self.__head.next is None:
                print(self.__head.value)
                return
            curr_item = self.__head
            result = ""
            while curr_item.next is not None:
                result += str(curr_item.value) + " --> "
                curr_item = curr_item.next
            result += str(curr_item.value)
            print(result)
            return


    class DoublyLL:
        def __init__(self, head=None) -> None:
            self.__head = head
            self.__tail = None
            self.__len = 0

        def __setitem__(self, index: int, value: object):
            """ change a node value based on its index """
            if index in range(self.__len):
                self[index].value = value

        def __getitem__(self, index: int):
            """ get a node value based on its index """
            return self.getData(index)

        def __delitem__(self, __o: object):
            """ remove a specific item from this DS """
            return self.remove(__o)

        def __contains__(self, __o: object) -> bool:
            """ return True if __o exist in this DS otherwise False """
            return True if type(self.getIndex(__o)) == int or self is __o else False

        def __iter__(self):
            self.index = 0
            return self

        def __next__(self):
            if self.index < self.__len-1:
                self.index += 1
                return self[self.index-1]
            raise StopIteration

        def __add__(self, __o: object):
            """ concatenate 2 data structures if they are from the same class """
            if isinstance(__o, LinkedList.DoublyLL):
                self.__tail.next = __o.__head
                __o.__head.prev = self.__tail
                self.__tail = __o.__tail
                self.__len += __o.__len
                return self
            raise TypeError("(+) operator could not wokrs between different classes types")

        def __lt__(self, __o: object) -> bool:
            """ compare the length of two object of the same class """
            if isinstance(__o, LinkedList.DoublyLL):
                return self.__len < __o.__len
            raise TypeError("(<) operator could not wokrs between different classes types")

        def __gt__(self, __o: object) -> bool:
            """ compare the length of two object of the same class """
            if isinstance(__o, LinkedList.DoublyLL):
                return self.__len > __o.__len
            raise TypeError("(>) operator could not wokrs between different classes types")

        def __le__(self, __o: object) -> bool:
            """ compare the length of two object of the same class """
            if isinstance(__o, LinkedList.DoublyLL):
                return self.__len <= __o.__len
            raise TypeError("(<=) operator could not wokrs between different classes types")

        def __ge__(self, __o: object) -> bool:
            """ compare the length of two object of the same class """
            if isinstance(__o, LinkedList.DoublyLL):
                return self.__len >= __o.__len
            raise TypeError("(>=) operator could not wokrs between different classes types")

        def __len__(self) -> int:
            return self.__len

        def __repr__(self) -> str:
            return f"Linked List[type: Doubly]({self.toList()})"
            
        def __str__(self) -> str:
            return f"({self.toList()})"

        def isEmpty(self):
            return self.__len == 0

        def getIndex(self, data):
            f""" raise ValueError if the {self.__class__.__name__} is empty """
            if self.isEmpty():
                raise ValueError(f"Empty {self.__class__.__name__}")
            if data == self.__tail.value:
                return self.__len - 1
            curr_item = self.__head
            index = 0
            while curr_item.value != data:
                if curr_item.next is None:
                    return None
                curr_item = curr_item.next
                index += 1
            if curr_item.value == data:
                return index
        
        def getData(self, index=int):
            f""" index must be an int & in the range of len({self.__class__.__name__}) otherwise it will raise an error.
            2/ to print the value if the node use .value """
            if not isinstance(index, int):
                raise TypeError("index must be an integer")
            elif index >= self.__len or index < -self.__len:
                raise IndexError(f"{self.__class__.__name__} index out of range")
            elif index in range(-1, -self.__len-1, -1):
                curr_item = self.__tail
                count = -1
                while index != count:
                    curr_item = curr_item.prev
                    count -= 1
                return curr_item
            curr_item = self.__head
            count = 0
            while count != index:
                curr_item = curr_item.next
                count += 1
            if count == index:
                return curr_item

        def count(self, data):
            f""" counting the number of the same item in this {self.__class__.__name__} """
            if self.isEmpty():
                raise ValueError(f"empty {self.__class__.__name__}")
            if not self.getIndex(data):
                raise ValueError(f"{data} does not exist")
            curr_item = self.__head
            times = 0
            while curr_item != self.__tail:
                if curr_item.value == data:
                    times += 1
                curr_item = curr_item.next
            if self.__tail.value == data:
                times += 1
            return times

        def fromItr(self, itr):
            f""" make a {self.__class__.__name__} from any iterable in python including dict & str """
            if len(itr) == 0:
                return
            for item in itr:
                self.append(item)
            return

        def toList(self) -> list:
            f""" convert a {self.__class__.__name__} into a python list """
            if self.isEmpty():
                return []
            elif self.__head.next is None:
                return [self.__head.value]
            curr_item = self.__head
            result = []
            while curr_item.next is not None:
                result.append(curr_item.value)
                curr_item = curr_item.next
            result.append(curr_item.value)
            return result

        def append(self, data) -> None:
            f""" insert a node at the end of the {self.__class__.__name__} """
            node = LinkedList.Node(data)
            if self.isEmpty():
                self.__head = node
                self.__len += 1
                return
            if self.__head.next is None:
                node.prev = self.__head
                self.__head.next = node
                self.__tail = node
                self.__len += 1
                return
            self.__tail.next = node
            node.prev = self.__tail
            self.__tail = node
            self.__len += 1
            return
        
        def appendFirst(self, data) -> None:
            f""" insert a node at the 0 index of the {self.__class__.__name__} """
            node = LinkedList.Node(data)
            if self.isEmpty():
                self.__head = node
                self.__len += 1
                return
            if self.__head.next is None:
                self.__head.prev = node
                node.next = self.__head
                self.__tail = self.__head
                self.__head = node
                self.__len += 1
                return
            self.__head.prev = node
            node.next = self.__head
            self.__head = node
            self.__len += 1
            return
        
        def insert(self, data, index=0) -> None:
            f""" if the {self.__class__.__name__} is empty so this method will ignore the index arg """
            node = LinkedList.Node(data)
            if self.isEmpty():
                self.__head = node
                self.__len += 1
                return
            if index == 0:
                if self.__tail is None:
                    self.__head.next = node
                    self.__tail = self.__head
                    self.__tail.next = None
                self.__head.prev = node
                node.next = self.__head
                self.__head = node
                self.__len += 1
                return
            elif index >= self.__len:
                self.__tail.next = node
                node.prev = self.__tail
                self.__tail = node
                self.__len += 1
                return
            curr_item = self.getData(index)
            node.prev = curr_item.prev
            node.next = curr_item
            curr_item.prev.next = node
            curr_item.prev = node
            self.__len += 1
            return

        def pop(self):
            f""" remove the last element of the {self.__class__.__name__} """
            if self.isEmpty():
                raise ValueError(f"empty {self.__class__.__name__}")
            if self.__head.next is None:
                del_item = self.__head
                self.__head = None
                self.__len -= 1
                return del_item
            del_item = self.__tail.value
            self.__tail.prev.next = None
            self.__tail = self.__tail.prev
            self.__len -= 1
            return del_item

        def remove(self, value):
            f""" raise ValueError if the {self.__class__.__name__} is empty or if the value does not exist """
            if self.isEmpty():
                raise ValueError(f"Empty {self.__class__.__name__}")
            elif self.__head.next is None and self.__head.value != value:
                raise ValueError(f"{value} does not exist")
            elif self.__head.value == value:
                self.__head = self.__head.next
                self.__len -= 1
                return
            curr_item = self.__head
            while curr_item.value != value:
                if curr_item.next is None:
                    raise ValueError(f"{value} does not exist")
                curr_item = curr_item.next
            if curr_item.value == value:
                if curr_item.next is None:
                    curr_item.prev.next = None
                    self.__tail = curr_item.prev
                    self.__len -= 1
                    return
                curr_item.prev.next = curr_item.next
                curr_item.next.prev = curr_item.prev
                self.__len -= 1
                return

        def clear(self):
            f""" remove all this {self.__class__.__name__} elements """
            self.__head = None
            self.__tail = None
            self.__len = 0

        def display(self):
            f""" showing this {self.__class__.__name__} in a nice & readable way """
            if self.isEmpty():
                return
            if self.__head.next is None:
                print(self.__head.value)
                return
            curr_item = self.__head
            result = ""
            while curr_item.next is not None:
                result += str(curr_item.value) + " <--> "
                curr_item = curr_item.next
            result += str(curr_item.value)
            print(result)
            return

    class CircularLL:
        def __init__(self, head=None) -> None:
            self.__head = head
            self.__tail = None
            self.__len = 0

        def __setitem__(self, index: int, value: object):
            """ change a node value based on its index """
            if index in range(self.__len):
                self[index].value = value

        def __getitem__(self, index: int):
            """ get a node value based on its index """
            return self.getData(index)

        def __delitem__(self, __o: object):
            """ remove a specific item from this DS """
            return self.remove(__o)

        def __contains__(self, __o: object) -> bool:
            """ return True if __o exist in this DS otherwise False """
            return True if type(self.getIndex(__o)) == int or self is __o else False

        def __iter__(self):
            self.index = 0
            return self

        def __next__(self):
            if self.index < self.__len-1:
                self.index += 1
                return self[self.index-1]
            raise StopIteration

        def __add__(self, __o: object):
            """ concatenate 2 data structures if they are from the same class """
            if isinstance(__o, LinkedList.CircularLL):
                self.__tail.next = __o.__head
                self.__len += __o.__len
                return self
            raise TypeError("(+) operator could not wokrs between different classes types")

        def __lt__(self, __o: object) -> bool:
            """ compare the length of two object of the same class """
            if isinstance(__o, LinkedList.CircularLL):
                return self.__len < __o.__len
            raise TypeError("(<) operator could not wokrs between different classes types")

        def __gt__(self, __o: object) -> bool:
            """ compare the length of two object of the same class """
            if isinstance(__o, LinkedList.CircularLL):
                return self.__len > __o.__len
            raise TypeError("(>) operator could not wokrs between different classes types")

        def __le__(self, __o: object) -> bool:
            """ compare the length of two object of the same class """
            if isinstance(__o, LinkedList.CircularLL):
                return self.__len <= __o.__len
            raise TypeError("(<=) operator could not wokrs between different classes types")

        def __ge__(self, __o: object) -> bool:
            """ compare the length of two object of the same class """
            if isinstance(__o, LinkedList.CircularLL):
                return self.__len >= __o.__len
            raise TypeError("(>=) operator could not wokrs between different classes types")

        def __len__(self) -> int:
            return self.__len

        def __repr__(self) -> str:
            return f"Linked List[type: Circular]({self.toList()})"
            
        def __str__(self) -> str:
            return f"({self.toList()})"

        def isEmpty(self):
            return self.__len == 0

        def getIndex(self, data):
            f""" raise ValueError if the {self.__class__.__name__} is empty """
            if self.isEmpty():
                raise ValueError(f"Empty {self.__class__.__name__}")
            if data == self.__tail.value:
                return self.__len - 1
            curr_item = self.__head
            index = 0
            while curr_item.value != data:
                if curr_item.next == self.__head:
                    return None
                curr_item = curr_item.next
                index += 1
            if curr_item.value == data:
                return index
        
        def getData(self, index=int):
            f""" 1/ index must be an int & in the range of len({self.__class__.__name__}) otherwise it will raise an error.
            2/ to print the value if the node use .value """
            if not isinstance(index, int):
                raise TypeError("index must be an integer")
            if index >= self.__len or index < 0:
                raise IndexError(f"index range must be from 0 to len({self.__class__.__name__})")
            curr_item = self.__head
            count = 0
            while count != index:
                curr_item = curr_item.next
                count += 1
            if count == index:
                return curr_item

        def count(self, data) -> int:
            f""" counting the number of the same item in this {self.__class__.__name__} """
            if self.isEmpty():
                raise ValueError(f"empty {self.__class__.__name__}")
            curr_item = self.__head
            times = 0
            while curr_item != self.__tail:
                if curr_item.value == data:
                    times += 1
                curr_item = curr_item.next
            if self.__tail.value == data:
                times += 1
            return times

        def fromItr(self, itr):
            f""" make a {self.__class__.__name__} from any iterable in python including dict & str """
            if len(itr) == 0:
                return
            for item in itr:
                self.append(item)
            return

        def toList(self) -> list:
            f""" convert a {self.__class__.__name__} into a python list """
            if self.isEmpty():
                return []
            elif self.__head.next is None:
                return [self.__head.value]
            curr_item = self.__head
            result = []
            while curr_item.next != self.__head:
                result.append(curr_item.value)
                curr_item = curr_item.next
            result.append(curr_item.value)
            return result

        def append(self, data) -> None:
            f""" insert a node at the end of the {self.__class__.__name__} """
            node = LinkedList.Node(data)
            if self.isEmpty():
                self.__head = node
                self.__len += 1
                return
            if self.__head.next is None:
                node.next = self.__head
                self.__head.next = node
                self.__tail = node
                self.__len += 1
                return
            self.__tail.next = node
            node.next = self.__head
            self.__tail = node
            self.__len += 1
            return

        def insert(self, data, index=0) -> None:
            f""" if the {self.__class__.__name__} is empty so this method will ignore the index arg """
            node = LinkedList.Node(data)
            if self.isEmpty():
                self.__head = node
                self.__len += 1
                return
            if index == 0:
                if self.__tail is None:
                    self.__tail = self.__head
                node.next = self.__head
                self.__tail.next = node
                self.__head = node
                self.__len += 1
                return
            elif index >= self.__len:
                self.__tail.next = node
                node.next = self.__head
                self.__tail = node
                self.__len += 1
                return
            curr_item = self.getData(index-1)
            node.next = curr_item.next
            curr_item.next = node
            self.__len += 1
            return

        def pop(self):
            f""" remove the last element of this {self.__class__.__name__} """
            if self.isEmpty():
                raise ValueError(f"empty {self.__class__.__name__}")
            if self.__head.next is None:
                del_item = self.__head.value
                self.__head = None
                self.__len -= 1
                return  del_item
            del_item = self.__tail.value
            curr_item = self.__head
            while curr_item.next != self.__tail:
                curr_item = curr_item.next
            self.__tail = curr_item
            curr_item.next = self.__head
            self.__len -= 1
            return del_item

        def remove(self, value):
            f""" raise ValueError if the {self.__class__.__name__} is empty or if the value does not exist """
            if self.isEmpty():
                raise ValueError(f"Empty {self.__class__.__name__}")
            elif self.__head.next is None and self.__head.value != value:
                raise ValueError(f"{value} does not exist")
            elif self.__head.value == value:
                self.__head = self.__head.next
                self.__tail.next = self.__head
                self.__len -= 1
                return
            curr_item = self.__head
            next_item = self.__head.next
            while next_item.value != value:
                if next_item.next == self.__head:
                    raise ValueError(f"{value} does not exist")
                curr_item = next_item
                next_item = next_item.next
            if next_item.next == self.__head:
                curr_item.next = self.__head
                self.__tail = curr_item
                self.__len -= 1
                return
            curr_item.next = next_item.next
            self.__len -= 1
            return

        def clear(self):
            f""" remove all this {self.__class__.__name__} elements """
            self.__head = None
            self.__tail = None
            self.__len = 0

        def display(self):
            f""" showing this {self.__class__.__name__} in a nice & readable way """
            if self.isEmpty():
                return
            elif self.__head.next is None:
                print(self.__head.value)
                return
            curr_item = self.__head
            result = ""
            while curr_item.next != self.__head:
                result += str(curr_item.value) + " --> "
                curr_item = curr_item.next
            result += str(curr_item.value) + " --> [first_item]"
            print(result)
            return

    class CircularDoublyLL:
        def __init__(self, head=None) -> None:
            self.__head = head
            self.__tail = None
            self.__len = 0

        def __setitem__(self, index: int, value: object):
            """ change a node value based on its index """
            if index in range(self.__len):
                self[index].value = value

        def __getitem__(self, index: int):
            """ get a node value based on its index """
            return self.getData(index)

        def __delitem__(self, __o: object):
            """ remove a specific item from this DS """
            return self.remove(__o)

        def __contains__(self, __o: object) -> bool:
            """ return True if __o exist in this DS otherwise False """
            return True if type(self.getIndex(__o)) == int or self is __o else False

        def __iter__(self):
            self.index = 0
            return self

        def __next__(self):
            if self.index < self.__len-1:
                self.index += 1
                return self[self.index-1]
            raise StopIteration

        def __add__(self, __o: object):
            """ concatenate 2 data structures if they are from the same class """
            if isinstance(__o, LinkedList.CircularDoublyLL):
                self.__tail.next = __o.__head
                __o.__head.prev = self.__tail
                self.__head.prev = __o.__tail
                __o.__tail.next = self.__head
                self.__tail = __o.__tail
                self.__len += __o.__len
                return self
            raise TypeError("(+) operator could not wokrs between different classes types")

        def __lt__(self, __o: object) -> bool:
            """ compare the length of two object of the same class """
            if isinstance(__o, LinkedList.CircularDoublyLL):
                return self.__len < __o.__len
            raise TypeError("(<) operator could not wokrs between different classes types")

        def __gt__(self, __o: object) -> bool:
            """ compare the length of two object of the same class """
            if isinstance(__o, LinkedList.CircularDoublyLL):
                return self.__len > __o.__len
            raise TypeError("(>) operator could not wokrs between different classes types")

        def __le__(self, __o: object) -> bool:
            """ compare the length of two object of the same class """
            if isinstance(__o, LinkedList.CircularDoublyLL):
                return self.__len <= __o.__len
            raise TypeError("(<=) operator could not wokrs between different classes types")

        def __ge__(self, __o: object) -> bool:
            """ compare the length of two object of the same class """
            if isinstance(__o, LinkedList.CircularDoublyLL):
                return self.__len >= __o.__len
            raise TypeError("(>=) operator could not wokrs between different classes types")

        def __len__(self) -> int:
            return self.__len

        def __repr__(self) -> str:
            return f"Linked List[type: Circular Doubly]({self.toList()})"
            
        def __str__(self) -> str:
            return f"({self.toList()})"

        def isEmpty(self):
            return self.__len == 0

        def getIndex(self, data):
            f""" raise ValueError if the {self.__class__.__name__} is empty """
            if self.isEmpty():
                raise ValueError(f"Empty {self.__class__.__name__}")
            if data == self.__tail.value:
                return self.__len - 1
            curr_item = self.__head
            index = 0
            while curr_item.value != data:
                if curr_item.next is None:
                    return None
                curr_item = curr_item.next
                index += 1
            if curr_item.value == data:
                return index
        
        def getData(self, index=int):
            f""" index must be an int & in the range of len({self.__class__.__name__}) otherwise it will raise an error.
            2/ to print the value if the node use .value """
            if not isinstance(index, int):
                raise TypeError("index must be an integer")
            elif index >= self.__len or index < -self.__len:
                raise IndexError(f"{self.__class__.__name__} index out of range")
            elif index in range(-1, -self.__len-1, -1):
                curr_item = self.__tail
                count = -1
                while index != count:
                    curr_item = curr_item.prev
                    count -= 1
                return curr_item
            curr_item = self.__head
            count = 0
            while count != index:
                curr_item = curr_item.next
                count += 1
            if count == index:
                return curr_item

        def count(self, data):
            f""" counting the number of the same item in this {self.__class__.__name__} """
            if self.isEmpty():
                raise ValueError(f"empty {self.__class__.__name__}")
            if not self.getIndex(data):
                raise ValueError(f"{data} does not exist")
            curr_item = self.__head
            times = 0
            while curr_item != self.__tail:
                if curr_item.value == data:
                    times += 1
                curr_item = curr_item.next
            if self.__tail.value == data:
                times += 1
            return times

        def fromItr(self, itr):
            f""" make a {self.__class__.__name__} from any iterable in python including dict & str """
            if len(itr) == 0:
                return
            for item in itr:
                self.append(item)
            return

        def toList(self) -> list:
            f""" convert a {self.__class__.__name__} into a python list """
            if self.isEmpty():
                return []
            elif self.__head.next is None:
                return [self.__head.value]
            curr_item = self.__head
            result = []
            while curr_item.next != self.__head:
                result.append(curr_item.value)
                curr_item = curr_item.next
            result.append(curr_item.value)
            return result

        def append(self, data) -> None:
            f""" insert a node at the end of the {self.__class__.__name__} """
            node = LinkedList.Node(data)
            if self.isEmpty():
                self.__head = node
                self.__len += 1
                return
            if self.__head.next is None:
                node.prev = self.__head
                node.next = self.__head
                self.__head.next = node
                self.__head.prev = node
                self.__tail = node
                self.__len += 1
                return
            self.__tail.next = node
            self.__head.prev = node
            node.prev = self.__tail
            node.next = self.__head
            self.__tail = node
            self.__len += 1
            return
        
        def appendFirst(self, data) -> None:
            f""" insert a node at the 0 index of the {self.__class__.__name__} """
            node = LinkedList.Node(data)
            if self.isEmpty():
                self.__head = node
                self.__len += 1
                return
            if self.__head.next is None:
                self.__head.prev = node
                self.__head.next = node
                node.next = self.__head
                node.prev = self.__head
                self.__tail = self.__head
                self.__head = node
                self.__len += 1
                return
            self.__head.prev = node
            self.__tail.next = node
            node.next = self.__head
            node.prev = self.__tail
            self.__head = node
            self.__len += 1
            return
        
        def insert(self, data, index=0) -> None:
            f""" if the {self.__class__.__name__} is empty so this method will ignore the index arg """
            node = LinkedList.Node(data)
            if self.isEmpty():
                self.__head = node
                self.__len += 1
                return
            if index == 0:
                if self.__tail is None:
                    self.__head.next = node
                    self.__tail = self.__head
                self.__head.prev = node
                node.next = self.__head
                node.prev = self.__tail
                self.__tail.next = node
                self.__head = node
                self.__len += 1
                return
            elif index >= self.__len:
                self.__tail.next = node
                node.prev = self.__tail
                node.next = self.__head
                self.__tail = node
                self.__len += 1
                return
            curr_item = self.getData(index)
            node.prev = curr_item.prev
            node.next = curr_item
            curr_item.prev.next = node
            curr_item.prev = node
            self.__len += 1
            return

        def pop(self):
            f""" remove the last element of this {self.__class__.__name__} """
            if self.isEmpty():
                raise ValueError(f"empty {self.__class__.__name__}")
            if self.__head.next is None:
                del_item = self.__head.value
                self.__head = None
                self.__len -= 1
                return  del_item
            del_item = self.__tail.value
            self.__tail.prev.next = self.__head
            self.__tail = self.__tail.prev
            self.__head.prev = self.__tail
            self.__len -= 1
            return del_item

        def remove(self, value):
            f""" raise ValueError if the {self.__class__.__name__} is empty or if the value does not exist """
            if self.isEmpty():
                raise ValueError(f"Empty {self.__class__.__name__}")
            elif self.__head.next is None and self.__head.value != value:
                raise ValueError(f"{value} does not exist")
            elif self.__head.value == value:
                self.__head = self.__head.next
                self.__tail.next = self.__head
                self.__len -= 1
                return
            curr_item = self.__head
            while curr_item.value != value:
                if curr_item.next is None:
                    raise ValueError(f"{value} does not exist")
                curr_item = curr_item.next
            if curr_item.value == value:
                if curr_item.next == self.__head:
                    curr_item.prev.next = self.__head
                    self.__tail = curr_item.prev
                    self.__len -= 1
                    return
                curr_item.prev.next = curr_item.next
                self.__len -= 1
                return

        def clear(self):
            f""" remove all this {self.__class__.__name__} elements """
            self.__head = None
            self.__tail = None
            self.__len = 0

        def display(self):
            f""" showing this {self.__class__.__name__} in a nice & readable way """
            if self.isEmpty():
                return
            elif self.__head.next is None:
                print(self.__head.value)
                return
            curr_item = self.__head
            result = ""
            while curr_item.next != self.__head:
                result += str(curr_item.value) + " <--> "
                curr_item = curr_item.next
            result += str(curr_item.value) + " <--> [first_item]"
            print(result)
            return

## Finished ##
