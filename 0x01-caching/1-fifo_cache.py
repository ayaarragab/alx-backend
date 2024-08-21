#!/usr/bin/env python3
"""
FIFO cache?
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO cache class
    """

    def __init__(self):
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        to update
        """
        if key and item:
            if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                self.cache_data[key] = item
                self.queue.append({key: item})
            else:
                d_key = list(self.queue[0].keys())[0]
                del self.cache_data[d_key]
                del self.queue[0]
                print(f'DISCARD: {d_key}')
                self.cache_data[key] = item
                self.queue.append({key: item})

    def get(self, key):
        """
        retrieve data
        """
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
