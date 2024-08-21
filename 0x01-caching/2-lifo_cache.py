#!/usr/bin/env python3
"""
FIFO cache?
"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    FIFO cache class
    """

    def __init__(self):
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """
        to update
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        self.stack.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = self.stack.pop(-2)
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

    def get(self, key):
        """
        retrieve data
        """
        return self.cache_data.get(key, None)
