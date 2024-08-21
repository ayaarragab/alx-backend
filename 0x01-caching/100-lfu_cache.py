#!/usr/bin/env python3
"""
FIFO cache?
"""


from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LRUCache cache class
    """

    def __init__(self):
        """
        LRUCache cache class
        """
        super().__init__()
        self.per_access_store = {}

    def put(self, key, item):
        """
        to update
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            min_accesses_val = min(self.per_access_store.keys())
            d_key = self.per_access_store[min_accesses_val]
            del self.per_access_store[min_accesses_val]
            del self.cache_data[d_key]
            self.per_access_store[0] = key
            print(f"DISCARD: {d_key}")

    def get(self, key):
        """
        retrieve data
        """
        if not key or key not in self.cache_data.keys():
            return None
        for k, v in self.per_access_store:
            if v == key:
                del self.per_access_store[k]
                self.per_access_store[k + 1] = v
        return self.cache_data[key]
