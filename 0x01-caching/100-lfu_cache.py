#!/usr/bin/env python3
"""
LFU cache?
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
        self.freq = {}
        self.order = []

    def put(self, key, item):
        """
        to update
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.freq[key] += 1
            self.cache_data[key] = item
        else:
            if len(self.cache_data) == self.MAX_ITEMS:
                d_key = min(self.freq, key=lambda k: (self.freq[k],
                                                      self.order.index(k)))
                del self.cache_data[d_key]
                del self.freq[d_key]
                del self.order.remove(d_key)
                print(f"DISCARD: {d_key}")
            self.freq[key] = 1
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        retrieve data
        """
        if not key or key not in self.cache_data.keys():
            return None
        self.freq[key] += 1
        return self.cache_data[key]
