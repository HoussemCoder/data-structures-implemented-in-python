## Hash Map ##
"""
the idea here is to implement a hashmap by storing some data using 2 keywords: key, value
the key indicates its value stored in memory in a specific place using a hash function (do some research, it has a lot of info to know)
this function returns (using some methods) the position of the key to store its value in that specific place
this DS is quite different from a simple array (or list), in python it's represented as dict

for deletion we use the tombstone method (there are other methods out there)

sometimes we get the same address for 2 or more keys, this called collision.
we have some technics to reduce it (not possible to eliminate the collision):
    
    1/ Open hashing (closed addressing) ==> using chaining method (used in our case ==> with a linked_list (ao list, or even a hashmap) in the same pos)
    
                                           |> linear probing (default choice for open hashing |
    2/ Closed hashing (open addressing) ==>|> quadratic probing                               |> looking for empty pos using 1 of these 3
                                           |> double hashing                                  |
                                           |> ... (there are other methods out there)
                                           to get a better understanding: https://medium.com/@Faris_PY/hash-map-in-python-collision-load-factor-rehashing-1484ea7d4bc0

    3/ Rehashing ==> by doubling the hashmap size when items_num/hashmap_size >= load_factor(=0.75 by default)
       & redistribute all items into the new doubled hashmap
       - this technic works well with open addressing hashmaps and not necessary for closed addressing
    
    - and every solution has its pros as well as cons, chaeck out that topic on the previous link above.

==> we suggest you take a good theoretical base information before working with hashmaps

#### we have implemented all these technics above ####
 """

from datastructures import LinkedList as ll

#### using open hashing (chaining) for avoiding collision ####
class Hashmap:
    def __init__(self, size=17) -> None:
        self.__SIZE = size
        self.__arr = [None for _ in range(self.__SIZE)]
        self.__keys = []
        self.__values = []
        self.__len = 0

    def __setitem__(self, key, value):
        return self.append(key, value)

    def __getitem__(self, key):
        return self.find(key)

    def __delitem__(self, key):
        return self.remove(key)

    def __contains__(self, __o: object):
        return True if self.find(__o) is not None or __o is self else False

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < self.__len-1:
            self.index += 1
            return self.__keys[self.index-1]
        raise StopIteration

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Hashmap):
            if self.__keys == __o.__keys and self.__values == __o.__values:
                return True
            return False
        raise NotImplemented

    def __lt__(self, __o: object) -> bool:
        if isinstance(__o, Hashmap):
            return len(self) < len(__o)
        raise TypeError("(<) operator could not wokrs between different classes types")

    def __gt__(self, __o: object) -> bool:
        if isinstance(__o, Hashmap):
            return len(self) > len(__o)
        raise TypeError("(>) operator could not wokrs between different classes types")

    def __le__(self, __o: object) -> bool:
        if isinstance(__o, Hashmap):
            return len(self) <= len(__o)
        raise TypeError("(<=) operator could not wokrs between different classes types")

    def __ge__(self, __o: object) -> bool:
        if isinstance(__o, Hashmap):
            return len(self) >= len(__o)
        raise TypeError("(>=) operator could not wokrs between different classes types")

    def __add__(self, __o: object):
        if isinstance(__o, Hashmap):
            for i in range(len(__o)):
                self.append(__o[i])
        raise TypeError("(+) operator could not wokrs between different classes types")

    def __len__(self) -> int:
        return self.__len

    def __repr__(self) -> str:
        return (self.__arr)

    def __str__(self) -> str:
        hash_table = "{"
        for item in self.__arr:
            if isinstance(item, ll.SinglyLL):
                for i in range(len(item)):
                    hash_table += f", \"{item[i].value[0]}\": {item[i].value[1]}" if hash_table[-1] != "{" else f"\"{item[i].value[0]}\": {item[i].value[1]}"
            elif isinstance(item, tuple):
                hash_table += f", \"{item[0]}\": {item[1]}" if hash_table[-1] != "{" else f"\"{item[0]}\": {item[1]}"
        return hash_table + "}"

    # there are a lot of hashing methods out there, this is one of them (based on the ascii_letters value)
    # also you can use the built-in hash()
    def __getHash(self, key) -> int:
        if isinstance(key, str):
            hash = 0
            for i in range(len(key)):
                hash += (i + len(key)) * ord(key[i])
            return hash % len(self.__arr)
        raise ValueError("key must be str")

    def __addKeyValue(self, key=None, value=None, update=False):
        if update:
            self.__values[self.__keys.index(key)] = value
            return
        elif key and value:
            self.__keys.append(key)
            self.__values.append(value)

    def __delKeyValue(self, key):
        self.__values.remove(self.__keys.index(key))
        return self.__keys.remove(key)

    def isEmpty(self) -> bool:
        return self.__len == 0

    def append(self, key, value):
        pos = self.__getHash(key) # get position in self.__arr for key using our hash method
        item = self.__arr[pos]
        if item is None or item[0] == key:
            self.__arr[pos] = (key, value) # set the tuple (key, value) in self.__arr[pos] or update its value
            self.__addKeyValue(key, value, update=True) if item[0] == key else self.__addKeyValue(key, value)
            self.__len += 1 if item is None else 0
            return
        elif isinstance(item, tuple) and item[0] != key:
            # set a list (or linked_list) because we have a collision
            self.__arr[pos] = ll.SinglyLL(self.__arr[pos])
            self.__arr[pos].append((key, value)) # now we have just 2 items in self.__arr[pos]
            self.__addKeyValue(key, value)
            self.__len += 1
            return
        elif isinstance(item, ll.SinglyLL):
        # before assigning a new (key, value) we search for the key if it exist, so only update its value
            for i in range(len(item)):
                if item[i].value[0] == key:
                    index = self.__values.index(value)
                    self.__arr[pos][i].value = (key, value)
                    self.__values[index] = value
                    return
            self.__arr[pos].append((key, value))
            self.__addKeyValue(key, value)
            self.__len += 1
            return

    def find(self, key):
        pos = self.__getHash(key) # get position in self.__arr for key using our hash method
        item = self.__arr[pos]
        if item is None or (isinstance(item, tuple) and item[0] != key):
            return # return None if condition is True (empty pos or 1 item but not the same key)
        elif isinstance(item, tuple) and item[0] == key:
            return item[1] # return the value if we have only 1 item in that pos
        elif len(item) >= 2: # if we have a list so we need to search into it
            for i in range(len(item)):
                if item[i].value[0] == key:
                    return item[i].value[1]
            return # return None if we didn't find the corresponding key

    def pop(self, key=None) -> tuple:
        if key:
            if isinstance(key, str):
                self.remove(key)
                return (key, self.__values[self.__keys.index(key)])
            raise ValueError("key must be str only")
        self.remove(self.__keys[-1])
        return (key, self.__values[-1])

    def remove(self, key):
        pos = self.__getHash(key)
        item = self.__arr[pos]
        if item is None:
            return
        elif isinstance(item, ll.SinglyLL):
            for i in range(len(item)):
                if item[i].value[0] == key:
                    item.remove(item[i])
                    self.__delKeyValue(key)
                    self.__len -= 1
                    return
        elif isinstance(item, tuple):
            self.__arr[pos] = None
            self.__delKeyValue(key)
            self.__len -= 1

    def keys(self) -> list:
        return self.__keys

    def values(self)-> list:
        return self.__values

#### using linear probing (closed hashing) for avoiding collision ####
# class Hashmap:
#     def __init__(self, load_factor=0.75, size=17) -> None:
#         self.__SIZE = size
#         self.__THRESHOLD = load_factor
#         self.__arr = [None for _ in range(self.__SIZE)]
#         self.__keys = []
#         self.__values = []
#         self.__len = 0

#     def __setitem__(self, key, value):
#         return self.append(key, value)

#     def __getitem__(self, key):
#         return self.find(key)

#     def __delitem__(self, key):
#         return self.remove(key)

#     def __contains__(self, __o: object):
#         return True if self.find(__o) is not None or __o is self else False

#     def __iter__(self):
#         self.index = 0
#         return self

#     def __next__(self):
#         if self.index < self.__len:
#             self.index += 1
#             return self.__keys[self.index-1]
#         raise StopIteration

#     def __eq__(self, __o: object) -> bool:
#         if isinstance(__o, Hashmap):
#             if self.__keys == __o.__keys and self.__values == __o.__values:
#                 return True
#             return False
#         raise NotImplemented

#     def __lt__(self, __o: object) -> bool:
#         if isinstance(__o, Hashmap):
#             return len(self) < len(__o)
#         raise TypeError("(<) operator could not wokrs between different classes types")

#     def __gt__(self, __o: object) -> bool:
#         if isinstance(__o, Hashmap):
#             return len(self) > len(__o)
#         raise TypeError("(>) operator could not wokrs between different classes types")

#     def __le__(self, __o: object) -> bool:
#         if isinstance(__o, Hashmap):
#             return len(self) <= len(__o)
#         raise TypeError("(<=) operator could not wokrs between different classes types")

#     def __ge__(self, __o: object) -> bool:
#         if isinstance(__o, Hashmap):
#             return len(self) >= len(__o)
#         raise TypeError("(>=) operator could not wokrs between different classes types")

#     def __add__(self, __o):
#         if isinstance(__o, Hashmap):
#             for i in range(len(__o)):
#                 self.append(__o.__keys[i], __o.__values[i])
#             return self
#         raise TypeError("(+) operator could not wokrs between different classes types")

#     def __len__(self):
#         return self.__len

#     def __repr__(self) -> str:
#         return (self.__arr)

#     def __str__(self) -> str:
#         hash_table = "{"
#         for key, value in zip(self.__keys, self.__values):
#             hash_table += f", \"{key}\": {value}" if hash_table[-1] != "{" else f"\"{key}\": {key}"
#         return hash_table + "}"

#     # there are a lot of hashing methods out there, this is one of them (based on the ascii_letters value)
#     def __getHash(self, key):
#         if isinstance(key, str):
#             hash = 0
#             for i in key:
#                 hash += ord(i)
#             return hash % len(self.__arr)
#         raise ValueError("key must be str")

#     def __reHash(self):
#         load_factor = self.__len / self.__SIZE
#         if load_factor > self.__THRESHOLD:
#             old_arr, self.__SIZE, self.__len = self.__arr, self.__SIZE*2, 0
#             self.__arr = [None for _ in range(self.__SIZE)]
#             for i in old_arr:
#                 if isinstance(i, tuple):
#                     self.__setitem__(i[0], i[1])

#     def __addKeyValue(self, key=None, value=None, update=False):
#         if update:
#             self.__values[self.__keys.index(key)] = value
#             return
#         elif key and value:
#             self.__keys.append(key)
#             self.__values.append(value)

#     def __delKeyValue(self, key, value):
#         return self.__keys.remove(key)
#         self.__values.remove(value)

#     def isEmpty(self):
#         return self.__len == 0

#     def append(self, key, value):
#         self.__reHash()
#         pos = self.__getHash(key) # get position in self.__arr for key using our hash method
#         item = self.__arr[pos]
#         if item is None or item == "RIP" or item[0] == key:
#             self.__addKeyValue(key, value, update=True) if isinstance(item, tuple) else self.__addKeyValue(key, value)
#             self.__arr[pos] = (key, value) # set the tuple (key, value) in self.__arr[pos] or update its value
#             self.__len += 1 if item is None or item == "RIP" else 0
#             return
#         elif item[0] != key:
#             i = pos
#             while isinstance(self.__arr[i], tuple):
#                 i += 1
#                 i = 0 if i == self.__SIZE else i
#             self.__arr[i] = (key, value)
#             self.__addKeyValue(key, value)
#             self.__len += 1
#             return

#     def find(self, key):
#         pos = self.__getHash(key) # get position of key in self.__arr using our hash method
#         item = self.__arr[pos]
#         if item is None:
#             return # return None if we didn't find the corresponding key
#         elif isinstance(item, tuple) and item[0] == key:
#             return item[1] # return the value if the key entered matches the item[0]
#         i = pos
#         while self.__arr[i] == "RIP" or self.__arr[i][0] != key:
#             i += 1
#             i = 0 if i == self.__SIZE else i # if keep the search linearly when it reach the end of the self.__arr
#             if self.__arr[i] is None:
#                 return # return None if we didn't find the corresponding key
#         return self.__arr[i][1] # if no any swapping, return the key's value

#     def pop(self, key=None) -> tuple:
#         del_item = (key if key else self.__keys[-1], self.__values[self.__keys.index(key)] if key else self.__values[-1])
#         if key:
#             if isinstance(key, str):
#                 self.remove(key)
#                 return del_item
#             raise ValueError("key must be str only")
#         self.remove(self.__keys[-1])
#         return del_item

#     def remove(self, key):
#         pos = self.__getHash(key) # get position of key in self.__arr using our hash method
#         item = self.__arr[pos]
#         if item is None:
#             return
#         elif isinstance(item, tuple) and item[0] == key:
#             self.__arr[pos] = "RIP" # better than "None" to keep the __getitem__() works well
#             self.__delKeyValue(key, item[1])
#             self.__len -= 1
#             return
#         elif isinstance(item, tuple) and item[0] != key:
#             i = pos
#             while (isinstance(self.__arr[i], tuple) and self.__arr[i][0] != key) or self.__arr[i] == "RIP":
#                 i += 1
#                 if i == len(self.__arr): # to keep the search linearly when it reach the end of the self.__arr
#                     i = 0
#                 if self.__arr[i] is None:
#                     return # return None if we didn't find the corresponding key
#             self.__delKeyValue(key, self.__arr[i][1])
#             self.__arr[i] = "RIP"
#             self.__len -= 1
#             return

#     def keys(self) -> list:
#         return self.__keys

#     def values(self)-> list:
#         return self.__values


# #### using quadratic probing (closed hashing) for avoiding collision ####
# class Hashmap:
#     def __init__(self, load_factor=0.75, size=17) -> None:
#         self.__SIZE = size
#         self.__THRESHOLD = load_factor
#         self.__arr = [None for _ in range(self.__SIZE)]
#         self.__keys = []
#         self.__values = []
#         self.__len = 0

#     def __setitem__(self, key, value):
#         return self.append(key, value)

#     def __getitem__(self, key):
#         return self.find(key)

#     def __delitem__(self, key):
#         return self.remove(key)

#     def __contains__(self, __o: object):
#         return True if self.find(__o) is not None or __o is self else False

#     def __iter__(self):
#         self.index = 0
#         return self

#     def __next__(self):
#         if self.index < self.__len:
#             self.index += 1
#             return self.__keys[self.index-1]
#         raise StopIteration

#     def __eq__(self, __o: object) -> bool:
#         if isinstance(__o, Hashmap):
#             if self.__keys == __o.__keys and self.__values == __o.__values:
#                 return True
#             return False
#         raise NotImplemented

#     def __lt__(self, __o: object) -> bool:
#         if isinstance(__o, Hashmap):
#             return len(self) < len(__o)
#         raise TypeError("(<) operator could not wokrs between different classes types")

#     def __gt__(self, __o: object) -> bool:
#         if isinstance(__o, Hashmap):
#             return len(self) > len(__o)
#         raise TypeError("(>) operator could not wokrs between different classes types")

#     def __le__(self, __o: object) -> bool:
#         if isinstance(__o, Hashmap):
#             return len(self) <= len(__o)
#         raise TypeError("(<=) operator could not wokrs between different classes types")

#     def __ge__(self, __o: object) -> bool:
#         if isinstance(__o, Hashmap):
#             return len(self) >= len(__o)
#         raise TypeError("(>=) operator could not wokrs between different classes types")

#     def __add__(self, __o):
#         if isinstance(__o, Hashmap):
#             for i in range(len(__o)):
#                 self.append(__o.__keys[i], __o.__values[i])
#             return self
#         raise TypeError("(+) operator could not wokrs between different classes types")

#     def __len__(self):
#         return self.__len

#     def __repr__(self) -> str:
#         return (self.__arr)

#     def __str__(self) -> str:
#         hash_table = "{"
#         for item in self.__arr:
#             if isinstance(item, tuple):
#                 hash_table += f", \"{item[0]}\": {item[1]}" if hash_table[-1] != "{" else f"\"{item[0]}\": {item[1]}"
#         return hash_table + "}"

#     # there are a lot of hashing methods out there, this is one of them (based on the ascii_letters value)
#     def __getHash(self, key):
#         if isinstance(key, str):
#             hash = 0
#             for i in key:
#                 hash += ord(i)
#             return hash % len(self.__arr)
#         raise ValueError("key must be str")

#     def __reHash(self):
#         load_factor = self.__len / self.__SIZE
#         if load_factor > self.__THRESHOLD:
#             old_arr, self.__SIZE, self.__len = self.__arr, self.__SIZE*2, 0
#             self.__arr = [None for _ in range(self.__SIZE)]
#             for i in old_arr:
#                 if isinstance(i, tuple):
#                     self.__setitem__(i[0], i[1])

#     def __addKeyValue(self, key=None, value=None, update=False):
#         if update:
#             self.__values[self.__keys.index(key)] = value
#             return
#         elif key and value:
#             self.__keys.append(key)
#             self.__values.append(value)

#     def __delKeyValue(self, key, value):
#         self.__keys.remove(key)
#         self.__values.remove(value)

#     def isEmpty(self):
#         return self.__len == 0

#     def append(self, key, value):
#         self.__reHash()
#         pos = self.__getHash(key) # get position in self.__arr for key using our hash method
#         item = self.__arr[pos]
#         if item is None or item == "RIP" or item[0] == key:
#             self.__addKeyValue(key, value, update=True) if isinstance(item, tuple) else self.__addKeyValue(key, value)
#             self.__arr[pos] = (key, value) # set the tuple (key, value) in self.__arr[pos] or update its value
#             self.__len += 1 if item is None or item == "RIP" else 0
#             return
#         elif item[0] != key:
#             i, new_pos = 0, pos
#             while isinstance(self.__arr[new_pos], tuple):
#                 i += 1
#                 i = 0 if i == self.__SIZE else i # if keep the search linearly when it reach the end of the self.__arr
#                 new_pos = (pos + i*i) % self.__SIZE
#             self.__arr[new_pos] = (key, value)
#             self.__addKeyValue(key, value)
#             self.__len += 1
#             return

#     def find(self, key):
#         pos = self.__getHash(key) # get position of key in self.__arr using our hash method
#         item = self.__arr[pos]
#         if item is None or item == "RIP" or item[0] != key:
#             return # return None if we didn't find the corresponding key
#         elif isinstance(item, tuple) and item[0] == key:
#             return item[1] # return the value if the key entered matches the item[0]
#         i, new_pos = 0, pos
#         while self.__arr[new_pos] == "RIP" or self.__arr[new_pos][0] != key:
#             i += 1
#             i = 0 if i == self.__SIZE else i # if keep the search linearly when it reach the end of the self.__arr
#             new_pos = (pos + i*i) % self.__SIZE
#             if self.__arr[new_pos] is None:
#                 return # return None if we didn't find the corresponding key
#         return self.__arr[i][1]

#     def pop(self, key=None) -> tuple:
#         del_item = (key if key else self.__keys[-1], self.__values[self.__keys.index(key)] if key else self.__values[-1])
#         if key:
#             if isinstance(key, str):
#                 self.remove(key)
#                 return del_item
#             raise ValueError("key must be str")
#         self.remove(self.__keys[-1])
#         return del_item

#     def remove(self, key):
#         pos = self.__getHash(key) # get position of key in self.__arr using our hash method
#         item = self.__arr[pos]
#         if item is None:
#             return
#         elif isinstance(item, tuple) and item[0] == key:
#             self.__arr[pos] = "RIP" # better than "None" to keep the __getitem__() works well
#             self.__delKeyValue(key, item[1])
#             self.__len -= 1
#             return
#         elif (isinstance(item, tuple) and item[0] != key) or item == "RIP":
#             i, new_pos = 0, pos
#             while (isinstance(self.__arr[new_pos], tuple) and self.__arr[new_pos][0] != key) or self.__arr[new_pos] == "RIP":
#                 i += 1
#                 i = 0 if i == self.__SIZE else i # if keep the search linearly when it reach the end of the self.__arr
#                 new_pos = (pos + i*i) % self.__SIZE
#                 if self.__arr[new_pos] is None:
#                     return # return None if we didn't find the corresponding key
#             self.__delKeyValue(key, self.__arr[new_pos][1])
#             self.__arr[new_pos] = "RIP"
#             self.__len -= 1
#             return

#     def keys(self) -> list:
#         return self.__keys

#     def values(self)-> list:
#         return self.__values


# #### using double hashing (closed hashing) for avoiding collision ####
# class Hashmap:
#     def __init__(self, load_factor=0.75, size=17) -> None:
#         self.__SIZE = size
#         self.__THRESHOLD = load_factor
#         self.__arr = [None for _ in range(self.__SIZE)]
#         self.__keys = []
#         self.__values = []
#         self.__len = 0

#     def __setitem__(self, key, value):
#         return self.append(key, value)

#     def __getitem__(self, key):
#         return self.find(key)

#     def __delitem__(self, key):
#         return self.remove(key)

#     def __contains__(self, __o: object):
#         return True if self.find(__o) is not None or __o is self else False

#     def __iter__(self):
#         self.index = 0
#         return self

#     def __next__(self):
#         if self.index < self.__len:
#             self.index += 1
#             return self.__keys[self.index-1]
#         raise StopIteration

#     def __eq__(self, __o: object) -> bool:
#         if isinstance(__o, Hashmap):
#             if self.__keys == __o.__keys and self.__values == __o.__values:
#                 return True
#             return False
#         raise NotImplemented

#     def __lt__(self, __o: object) -> bool:
#         if isinstance(__o, Hashmap):
#             return len(self) < len(__o)
#         raise TypeError("(<) operator could not wokrs between different classes types")

#     def __gt__(self, __o: object) -> bool:
#         if isinstance(__o, Hashmap):
#             return len(self) > len(__o)
#         raise TypeError("(>) operator could not wokrs between different classes types")

#     def __le__(self, __o: object) -> bool:
#         if isinstance(__o, Hashmap):
#             return len(self) <= len(__o)
#         raise TypeError("(<=) operator could not wokrs between different classes types")

#     def __ge__(self, __o: object) -> bool:
#         if isinstance(__o, Hashmap):
#             return len(self) >= len(__o)
#         raise TypeError("(>=) operator could not wokrs between different classes types")

#     def __add__(self, __o):
#         if isinstance(__o, Hashmap):
#             for i in range(len(__o)):
#                 self.append(__o.__keys[i], __o.__values[i])
#             return self
#         raise TypeError("(+) operator could not wokrs between different classes types")

#     def __len__(self):
#         return self.__len

#     def __repr__(self) -> str:
#         return (self.__arr)

#     def __str__(self) -> str:
#         hash_table = "{"
#         for item in self.__arr:
#             if isinstance(item, tuple):
#                 hash_table += f", \"{item[0]}\": {item[1]}" if hash_table[-1] != "{" else f"\"{item[0]}\": {item[1]}"
#         return hash_table + "}"

#     # there are a lot of hashing methods out there, this is one of them (based on the ascii_letters value)
#     def __getHash(self, key: str) -> int:
#         if isinstance(key, str):
#             hash = 0
#             for i in key:
#                 hash += ord(i)
#             return hash % len(self.__arr)
#         raise ValueError("key must be str")

#     def __getHash_2(self, key):
#         if isinstance(key, str):
#             hash = 0
#             for i in range(len(key)):
#                 hash += (i + len(key)) * ord(key[i])
#             return hash % len(self.__arr)
#         raise ValueError("key must be str")

#     def __reHash(self):
#         load_factor = self.__len / self.__SIZE
#         if load_factor > self.__THRESHOLD:
#             old_arr, self.__SIZE, self.__len = self.__arr, self.__SIZE*2, 0
#             self.__arr = [None for _ in range(self.__SIZE)]
#             for i in old_arr:
#                 if isinstance(i, tuple):
#                     self.__setitem__(i[0], i[1])
#                     print(self.__arr, i)

#     def __addKeyValue(self, key=None, value=None, update=False):
#         if update:
#             self.__values[self.__keys.index(key)] = value
#             return
#         elif key and value:
#             self.__keys.append(key)
#             self.__values.append(value)

#     def __delKeyValue(self, key, value):
#         self.__keys.remove(key)
#         self.__values.remove(value)

#     def isEmpty(self):
#         return self.__len == 0

#     def append(self, key, value):
#         self.__reHash()
#         pos = self.__getHash(key) # get position in self.__arr for key using our hash method
#         item = self.__arr[pos]
#         if item is None or item == "RIP" or item[0] == key:
#             self.__arr[pos] = (key, value) # set the tuple (key, value) in self.__arr[pos] or update its value
#             self.__addKeyValue(key, value, update=True) if isinstance(item, tuple) else self.__addKeyValue(key, value)
#             self.__len += 1 if item is None or item == "RIP" else 0
#             return
#         elif item[0] != key:
#             i, new_pos = 0, pos
#             while isinstance(self.__arr[new_pos], tuple):
#                 i += 1
#                 i = 0 if i == self.__SIZE else i # if keep the search linearly when it reach the end of the self.__arr
#                 new_pos = (pos + i + self.__getHash_2(key)) % self.__SIZE
#                 # this next line is the official equation of the double hashing method, but for me the above works very well
#                 # new_pos = (pos + i*self.__getHash_2(key)) % self.__SIZE
#             self.__arr[new_pos] = (key, value)
#             self.__addKeyValue(key, value)
#             self.__len += 1
#             return

#     def find(self, key):
#         pos = self.__getHash(key) # get position of key in self.__arr using our hash method
#         item = self.__arr[pos]
#         if item is None or item == "RIP" or item[0] != key:
#             return # return None if we didn't find the corresponding key
#         elif isinstance(item, tuple) and item[0] == key:
#             return item[1] # return the value if the key entered matches the item[0]
#         i, new_pos = 0, pos
#         while self.__arr[new_pos] == "RIP" or self.__arr[new_pos][0] != key:
#             i += 1
#             i = 0 if i == self.__SIZE else i # if keep the search linearly when it reach the end of the self.__arr
#             new_pos = (pos + i + self.__getHash_2(key)) % self.__SIZE
#                 # this next line is the official equation of the double hashing method, but for me the above works very well
#                 # new_pos = (pos + i*self.__getHash_2(key)) % self.__SIZE
#             if self.__arr[new_pos] is None:
#                 return # return None if we didn't find the corresponding key
#         return self.__arr[i][1] # if no any swapping, return the key's value

#     def pop(self, key=None) -> tuple:
#         del_item = (key if key else self.__keys[-1], self.__values[self.__keys.index(key)] if key else self.__values[-1])
#         if key:
#             if isinstance(key, str):
#                 self.remove(key)
#                 return del_item
#             raise ValueError("key must be str")
#         self.remove(self.__keys[-1])
#         return del_item

#     def remove(self, key):
#         pos = self.__getHash(key) # get position of key in self.__arr using our hash method
#         item = self.__arr[pos]
#         if item is None:
#             return
#         elif isinstance(item, tuple) and item[0] == key:
#             self.__arr[pos] = "RIP" # better than "None" to keep the __getitem__() works well
#             self.__delKeyValue(key, item[1])
#             self.__len -= 1
#             return
#         elif (isinstance(item, tuple) and item[0] != key) or item == "RIP":
#             i, new_pos = 0, pos
#             while (isinstance(self.__arr[new_pos], tuple) and self.__arr[new_pos][0] != key) or self.__arr[new_pos] == "RIP":
#                 i += 1
#                 i = 0 if i == self.__SIZE else i # if keep the search linearly when it reach the end of the self.__arr
#                 new_pos = (pos + i + self.__getHash_2(key)) % self.__SIZE
#                 # this next line is the official equation of the double hashing method, but for me the above works very well
#                 # new_pos = (pos + i*self.__getHash_2(key)) % self.__SIZE
#                 if self.__arr[new_pos] is None:
#                     return # return None if we didn't find the corresponding key
#             self.__delKeyValue(key, self.__arr[new_pos][1])
#             self.__arr[new_pos] = "RIP"
#             self.__len -= 1
#             return

#     def keys(self) -> list:
#         return self.__keys

#     def values(self)-> list:
#         return self.__values


