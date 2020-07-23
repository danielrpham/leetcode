"""
Problem: Leetcode LRU Cache
LRU Cache https://leetcode.com/problems/lru-cache/
Description: Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1. put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up: Could you do both operations in O(1) time complexity?
"""
from collections import deque class LRUCache:

def __init__(self, capacity: int):
    self._size = 0
    self._counter = 1
    if capacity > 0:
        self._capacity = capacity
        self._queue = deque() 
        self._dict = dict()

def rotate_queue(self, key:int):
    if self._queue: # checks to see if anything in the que
        if self._queue[-1] == key: # at the very right -> do nothing
            pass
        elif self._queue[0] == key: # at the very left
            self._queue.rotate(-1)
        else: # somewhere in the middle
            counter = 0
            while(self._queue[0] != key): #rotate until the front
                self._queue.rotate(-1)
                counter += 1
            a = self._queue.popleft()
            self._queue.rotate(counter)
            self._queue.append(a)

def get(self, key: int) -> int:
    if key in self._dict:
        self.rotate_queue(key)
        return abs(self._dict[key])
    else:
        return -1

def put(self, key: int, value: int) -> None:
    if key not in self._dict: # also not in queue
        if (self._size == self._capacity): # max size
            a = self._queue.popleft()
            self._dict.pop(a)     
        else: # not max size
                       self._size += 1
        self._queue.append(key)
        self._dict[key] = value
    else: # key in dict 
        self.rotate_queue(key) # need to reset queue
        self._dict[key] = value