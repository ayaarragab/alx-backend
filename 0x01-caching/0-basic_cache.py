#!/usr/bin/env python3

 
"""
basic cache?
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    basic cache
    """

    def put(self, key, item):
        """
        to update
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        retrieve data
        """
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
