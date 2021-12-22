#!/usr/bin/python3
""" LRUCache that inherits from BaseCaching and is a caching system
"""


from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache defines:
      - inherits from BaseCaching and is a caching system
      - where your data are stored (in a dictionary)
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.count = {}

    def put(self, key, item):
        """assign to the {} self.cache_data the item value for the key
        """
        if key and item:
            if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                if key in self.cache_data.keys():
                    self.count[key] += 1
                else:
                    self.count[key] = 0
                self.cache_data[key] = item
            else:
                if key in self.cache_data.keys():
                    self.count[key] += 1
                else:
                    self.count[key] = 0
                self.cache_data[key] = item
                keys = list(self.cache_data.keys())
                lru = keys[0]
                for k, v in self.count.items():
                    if v < self.count[lru]:
                        lru = k
                if len(keys) > BaseCaching.MAX_ITEMS:
                    print("DISCARD: {}".format(lru))
                    del self.count[lru]
                    del self.cache_data[lru]

    def get(self, key):
        """return value in self.cache_data linked to key
        """
        if not key or not self.cache_data.get(key):
            return None
        self.count[key] += 1
        return self.cache_data.get(key)
