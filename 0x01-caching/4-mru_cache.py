#!/usr/bin/env python3
"""Class representation of LRU caching
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """"MRUCache that inherits from BaseCaching
    """
    def __init__(self):
        """Initialize LRUCache
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Assign key and item to the cache system
        """
        if len(self.cache_data) == self.MAX_ITEMS and key not in self.queue:
            discard = self.queue.pop()
            del self.cache_data[discard]
            print("DISCARD: {}".format(discard))

        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Fetch data from the cache system with key
        """
        if not key or key not in self.cache_data:
            return None
        self.queue.remove(key)
        self.queue.append(key)

        return self.cache_data[key]
