# Complete data structures implementation in python
## 4 DS types

### ====> Linked List <====
- This class contains the 4 types of linked lists:
1. Singly linked list
2. Doubly linked list
3. Circular linked list
4. Circular Doubly linked list

- Each one has its own class and methods.
- Some methods seem to be similar such as clear or insert.

### ====> Stack <====
- This Stack DS class has been implemented using the Doubly LL methods due to thier simularity. 
- you can also use as an approch for stacks a module called collections:
   
   from collections import deque
   
   stack = deque()
   
   ...

### ====> Queue <====
- This class contain the 4 types of queue:
1. Circular Queue

2. Input Restricted Queue     |
3. output Restricted Queue    |==> these 3 type are included in the Deque class
4. Double Ended Queue (Deque) |

                      |==> Ascending PQ
4. Priority Queue: ==>|
                      |==> Descending PQ

- Some of them have been implemented based on some linked lists types.

### ====> Hash map <====
- the idea here is to implement a hashmap by storing some data using 2 keywords: key, value
the key indicates its value stored in memory in a specific place using a hash function (do some research, it has a lot of info to know)
this function returns (using some methods) the position of the key to store its value in that specific place
this DS is quite different from a simple array (or list), in python it's represented as dict

- for deletion we use the tombstone method (there are other methods out there)

- sometimes we get the same address for 2 or more keys, this called collision.
- we have some technics to reduce it (not possible to eliminate the collision):
    
    1/ Open hashing (closed addressing) ==> using chaining method (used in our case ==> with a linked_list (ao list, or even a hashmap) in the same pos)
    
                                           |> linear probing (default choice for open hashing |
    2/ Closed hashing (open addressing) ==>|> quadratic probing                               |> looking for empty pos using 1 of these 3
                                           |> double hashing                                  |
                                           |> ... (there are other methods out there)
                                           to get a better understanding read this [article](https://medium.com/@Faris_PY/hash-map-in-python-collision-load-factor-rehashing-1484ea7d4bc0)

    3/ Rehashing ==> by doubling the hashmap size when items_num/hashmap_size >= load_factor(=0.75 by default)
       & redistribute all items into the new doubled hashmap
       - this technic works well with open addressing hashmaps and not necessary for closed addressing
    
    - and every solution has its pros as well as cons, check out that topic on the previous link above.

==> we suggest you take a good theoretical base information before working with hashmaps

- **_we have implemented all these technics above_**
