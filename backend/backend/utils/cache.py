# -*- coding: utf-8 -*-
"""
T2B Cache Utils
"""
# Python imports
from __future__ import unicode_literals
from urllib import parse

# lib imports
import pickle
from redis import Redis

# project imports
from .. import constants


class Cache:
    """
    Granite cache using redis
    """

    is_configured = False
    cache_url = constants.CACHE_URL

    def __init__(self):
        """
        Creating client to interact with
        """
        self.__client = Redis(**self.parse())
        if self.__client.ping():
            self.is_configured = True

    def parse(self):
        """
        Checking the url
        Returns:

        """
        parse_url = parse.urlparse(self.cache_url)
        return {
            "host": parse_url.hostname,
            "port": parse_url.port,
            "db": parse_url.path.replace("/", ""),
            "password": parse_url.password,
            "username": parse_url.username,
        }

    def set(self, key, value, seconds=None):
        if not self.is_configured:
            return False
        if seconds:
            self.__client.set(key, pickle.dumps(value), seconds)
        else:
            self.__client.set(key, pickle.dumps(value))

    def get(self, key):
        if not self.is_configured:
            return False
        data = self.__client.get(key)
        if data:
            return pickle.loads(data)

    def keys(self, keys):
        if not self.is_configured:
            return False
        return self.__client.keys(keys)

    def delete_many(self, keys):
        if not self.is_configured:
            return False
        if not keys:
            return False
        self.__client.delete(*keys)


def cache(invalidate=True, seconds=None):
    """
    Cache gateway functions
    """

    def decorator(func):
        """
        Cache decorator
        """
        core_cache = Cache()
        module_name = func.__module__.split(".")[-1]

        def wrapper(*args, **kwargs):
            """
            key generations
            """
            _pk = kwargs.get("pk", None)
            key = f"{func.__name__}__{module_name}"
            if _pk:
                key += f"__pk={_pk}"
            if not invalidate:
                kwarg_copy = kwargs.copy()
                kwarg_copy.pop("pk", None)
                decoded_kwargs = parse.urlencode(kwarg_copy)
                key += f"__{decoded_kwargs}"
                data = core_cache.get(key)
                if data is not None:
                    return data
                data = func(*args, **kwargs)
                if seconds:
                    core_cache.set(key, data, seconds)
                else:
                    core_cache.set(key, data)
            else:
                keys = core_cache.keys(f"{key}__*")
                keys.extend(core_cache.keys(f"*__{module_name}__*"))
                keys.extend(core_cache.keys(f"*__{module_name}_id={_pk}*"))
                core_cache.delete_many(keys)
                data = func(*args, **kwargs)
            return data

        return wrapper

    return decorator
