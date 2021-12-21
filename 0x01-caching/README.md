# 0x01. Caching

## Resources
Read or watch:

* [Cache replacement policies - FIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_%28FIFO%29)
* [Cache replacement policies - LIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#Last_In_First_Out_%28LIFO%29)
* [Cache replacement policies - LRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_Recently_Used_%28LRU%29)
* [Cache replacement policies - MRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Most_Recently_Used_%28MRU%29)
* [Cache replacement policies - LFU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least-Frequently_Used_%28LFU%29)

## Parent class `BaseCaching`

All your classes must inherit from `BaseCaching` defined:

# Tasks

## [0. Basic dictionary](./0-basic_cache.py)
Create a class `BasicCache` that inherits from `BaseCaching` and is a caching system:

* You must use `self.cache_data` - dictionary from the parent class `BaseCaching`
* This caching system doesn’t have limit
* `def put(self, key, item)`:
        Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
        If `key` or `item` is `None`, this method should not do anything.
* `def get(self, key)`:
        Must return the value in `self.cache_data` linked to `key`.
        If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, return `None`. 
```
@ubuntu:~/0x01$ ./0-main.py
Current cache:
Current cache:
A: Hello
B: World
C: Holberton
Hello
World
Holberton
None
Current cache:
A: Hello
B: World
C: Holberton
Current cache:
A: Street
B: World
C: Holberton
D: School
E: Battery
Street
``` 

## [1. FIFO caching](./1-fifo_cache.py)
Create a class `FIFOCache` that inherits from `BaseCaching` and is a caching system:

* You must use `self.cache_data` - dictionary from the parent class `BaseCaching`
* You can overload `def __init__(self)`: but don’t forget to call the parent init: `super().__init__()`
* `def put(self, key, item)`:
        Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
        If `key` or `item` is `None`, this method should not do anything.
        If the number of items in `self.cache_data` is higher that `BaseCaching.MAX_ITEMS`:
        you must discard the first item put in cache (FIFO algorithm)
        you must print `DISCARD`: with the `key` discarded and following by a new line
* `def get(self, key)`:
        Must return the value in `self.cache_data` linked to `key`.
        If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, return `None`.
```
@ubuntu:~/0x01$ ./1-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
DISCARD: A
Current cache:
B: World
C: Holberton
D: School
E: Battery
Current cache:
B: World
C: Street
D: School
E: Battery
DISCARD: B
Current cache:
C: Street
D: School
E: Battery
F: Mission
```

## [2. LIFO Caching](./2-lifo_cache.py)
Create a class `LIFOCache` that inherits from `BaseCaching` and is a caching system:

* You must use `self.cache_data` - dictionary from the parent class `BaseCaching`
* You can overload `def __init__(self)`: but don’t forget to call the parent init: `super().__init__()`
* `def put(self, key, item)`:
        Must assign to the dictionary self.cache_data the item value for the key key.
        If `key` or `item` is `None`, this method should not do anything.
        If the number of items in `self.cache_data` is higher that `BaseCaching.MAX_ITEMS`:
        you must discard the last item put in cache (LIFO algorithm)
        you must print `DISCARD`: with the `key` discarded and following by a new line
* `def get(self, key)`:
        Must return the value in `self.cache_data` linked to `key`.
        If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, return `None`.
```
@ubuntu:~/0x01$ ./2-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
DISCARD: D
Current cache:
A: Hello
B: World
C: Holberton
E: Battery
Current cache:
A: Hello
B: World
C: Street
E: Battery
DISCARD: C
Current cache:
A: Hello
B: World
E: Battery
F: Mission
DISCARD: F
Current cache:
A: Hello
B: World
E: Battery
G: San Francisco
```
