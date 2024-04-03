#!/usr/bin/python3
"""
LFUCache module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache inherits from BaseCaching
    """
    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                _frequency = min(self.frequency.values())
                _frequency = [k for k, v in self.frequency.items() if v == _frequency]
                if len(_frequency) > 1:
                    lru_key = min(self.cache_data, key=self.frequency.get)
                    del self.cache_data[lru_key]
                    del self.frequency[lru_key]
                    print("DISCARD:", lru_key)
                else:
                    removed_key = _frequency[0]
                    del self.cache_data[removed_key]
                    del self.frequency[removed_key]
                    print("DISCARD:", removed_key)
            self.cache_data[key] = item
            self.frequency[key] = self.frequency.get(key, 0) + 1

    def get(self, key):
        """
        Get an item by key
        """
        if key is not None and key in self.cache_data:
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
