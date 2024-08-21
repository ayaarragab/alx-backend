#!/usr/bin/env python3
"""
LRUCache cache?
"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRU cache class
    """

    def __init__(self):
        """
        d
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        to update
        """
        if not key or not item:
            return
        if len(self.cache_data) == self.MAX_ITEMS and not key in self.queue:
            d_key = self.queue.pop(0)
            del self.cache_data[d_key]
            print(f'DISCARD {d_key}')
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        retrieve data
        """
        if not key or key not in self.cache_data:
            return None
        self.queue.remove(key)
        self.queue.append(key)
        return self.cache_data[key]
