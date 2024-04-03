#!/usr/bin/env python3
'''
Create a class BasicCache that inherits from
BaseCaching and is a caching system
'''
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    def put(self, key, item):
        if key and item:
            '''
            assigns to the dictionary self.cache_data
            the item value for the key key
            If key or item is None, this method should not do anything
            '''
            self.cache_data[key] = item

    def get(self, key):
        '''
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn`t
        exist in self.cache_data, return None.
        '''
        return self.cache_data.get(key)
