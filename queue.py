## Queue DS Module ##

class Queue:
    """ 
    - This class contain the 4 types of queue:
    1. Circular Queue
    
    2. Input Restricted Queue     |
    3. output Restricted Queue    |==> these 3 type are included in the Deque class
    4. Double Ended Queue (Deque) |

                         |==> Ascending PQ
    4. Priority Queue:==>|
                         |==> Descending PQ

    - len func refers to a variable to minimize the times of looping through this DS
     """

    class Node:
        """ This class is used for all our DS which produce a node with some global properties """
        def __init__(self, value=None) -> None:
            self.prev = None
            self.value = value
            self.next = None


    class CircularQueue:
        """ This class has been implemented based on the circular linked list """
        def __init__(self, head=None) -> None:
            self.__head = head if not head else Queue.Node(head)
            self.__tail = self.__head
            self.__len = 0 if not head else 1

        def __contains__(self, __o: object) -> bool:
            """ return True if __o exist in this DS otherwise False """
            return True if type(self.getIndex(__o)) == int or self is __o else False

        def __getitem__(self, index: int):
            """ get a node value based on its index """
            return self.getData(index)

        def __iter__(self):
            self.index = 0
            return self

        def __next__(self):
            if self.index < self.__len:
                self.index += 1
                return self[self.index-1]
            raise StopIteration

        def __add__(self, __o: object):
            """ concatenate 2 data structures if they are from the same class """
            if isinstance(__o, Queue.CircularQueue):
                self.__tail.next = __o.__head
                return self
            raise TypeError("(+) operator could not wokrs between different classes types")

        def __lt__(self, __o: object) -> bool:
            """ compare the length of two object of the same class """
            if isinstance(__o, Queue.CircularQueue):
                return self.__len < __o.__len
            raise TypeError("(<) operator could not wokrs between different classes types")

        def __gt__(self, __o: object) -> bool:
            """ compare the length of two object of the same class """
            if isinstance(__o, Queue.CircularQueue):
                return self.__len > __o.__len
            raise TypeError("(>) operator could not wokrs between different classes types")

        def __le__(self, __o: object) -> bool:
            """ compare the length of two object of the same class """
            if isinstance(__o, Queue.CircularQueue):
                return self.__len <= __o.__len
            raise TypeError("(<=) operator could not wokrs between different classes types")

        def __ge__(self, __o: object) -> bool:
            """ compare the length of two object of the same class """
            if isinstance(__o, Queue.CircularQueue):
                return self.__len >= __o.__len
            raise TypeError("(>=) operator could not wokrs between different classes types")

        def __len__(self) -> int:
            return self.__len

        def __repr__(self) -> str:
            return f"Queue[type: Circular]({self.toList()})"

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

        def getData(self, index):
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
            """ make a circular queue from any iterable in python including dict & str """
            if len(itr) == 0:
                return
            for item in itr:
                self.enqueue(item)
            return

        def toList(self):
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

        def enqueue(self, data):
            f""" insert a node at the end of the {self.__class__.__name__} """
            node = Queue.Node(data)
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

        def peek(self):
            """ return the first element without removing it """
            if self.isEmpty():
                return
            return self.__head.value

        def dequeue(self):
            f""" remove the first element of this {self.__class__.__name__} """
            if self.isEmpty():
                raise ValueError("empty circular queue")
            del_item = self.__head.value
            self.__head = self.__head.next
            self.__tail.next = self.__head
            self.__len -= 1
            return del_item

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


    class Deque:
        """ This class has been implemented based on the doubly linked list """
        def __init__(self, head=None) -> None:
            self.__head = head if not head else Queue.Node(head)
            self.__tail = self.__head
            self.__len = 0 if not head else 1

        def __contains__(self, __o: object) -> bool:
            """ return True if __o exist in this DS otherwise False """
            return True if type(self.getIndex(__o)) == int or self is __o else False

        def __getitem__(self, index: int):
            """ get a node value based on its index """
            return self.getData(index)

        def __iter__(self):
            self.index = 0
            return self

        def __next__(self):
            if self.index < self.__len:
                self.index += 1
                return self[self.index-1]
            raise StopIteration

        def __add__(self, __o: object):
            """ concatenate 2 data structures if they are from the same class """
            if isinstance(__o, Queue.Deque):
                self.__tail.next = __o.__head
                return self
            raise TypeError("(+) operator could not wokrs between different classes types")

        def __lt__(self, __o: object) -> bool:
            """ compare the length of two object of the same class """
            if isinstance(__o, Queue.Deque):
                return self.__len < __o.__len
            raise TypeError("(<) operator could not wokrs between different classes types")

        def __gt__(self, __o: object) -> bool:
            """ compare the length of two object of the same class """
            if isinstance(__o, Queue.Deque):
                return self.__len > __o.__len
            raise TypeError("(>) operator could not wokrs between different classes types")

        def __le__(self, __o: object) -> bool:
            """ compare the length of two object of the same class """
            if isinstance(__o, Queue.Deque):
                return self.__len <= __o.__len
            raise TypeError("(<=) operator could not wokrs between different classes types")

        def __ge__(self, __o: object) -> bool:
            """ compare the length of two object of the same class """
            if isinstance(__o, Queue.Deque):
                return self.__len >= __o.__len
            raise TypeError("(>=) operator could not wokrs between different classes types")

        def __len__(self) -> int:
            return self.__len

        def __repr__(self) -> str:
            return f"Queue[type: Circular]({self.toList()})"

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

        def getData(self, index):
            f""" 1/ index must be an int & in the range of len({self.__class__.__name__}) otherwise it will raise an error.
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
            """ make a circulat queue from any iterable in python including dict & str """
            if len(itr) == 0:
                return
            for item in itr:
                self.enqueue(item)
            return

        def toList(self):
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

        def enqueue(self, data):
            f""" insert a node at the end of this {self.__class__.__name__} """
            node = Queue.Node(data)
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

        def lEnqueue(self, data):
            f""" insert a node in index 0 of this {self.__class__.__name__} """
            node = Queue.Node(data)
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

        def peek(self):
            """ return the first element without removing it """
            if self.isEmpty():
                return
            return self.__head.value

        def rPeek(self):
            """ return the last element without removing it """
            if self.isEmpty():
                return
            return self.__tail.value

        def dequeue(self):
            f""" remove the first element of this {self.__class__.__name__} """
            if self.isEmpty():
                raise ValueError("empty circular queue")
            del_item = self.__head.value
            self.__head = self.__head.next
            self.__tail.next = self.__head
            self.__len -= 1
            return del_item

        def rDequeue(self):
            f""" remove the last element of this {self.__class__.__name__} """
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

    class PriorityQueue:

        class ascendingPQ:
            def __init__(self, head=None) -> None:
                self.__head = head if not head else Queue.Node(head)
                self.__tail = self.__head
                self.__len = 0 if not head else 1

        class descendingPQ:
            def __init__(self, head=None) -> None:
                self.__head = head if not head else Queue.Node(head)
                self.__tail = self.__head
                self.__len = 0 if not head else 1

## Finished ##
