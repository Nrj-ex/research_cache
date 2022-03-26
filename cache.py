from sys import getsizeof


class Сache():
    def __init__(self, capacity):
        # capacity размер кеша в байтах
        # количество кешируемых значений
        self.capacity = capacity
        # self.max_value = 10000
        self.history = []
        self.cache = {}

    def get_cache(self, key):
        if key in self.cache.keys():
            return self.cache[key]

    def set_cache(self, key, value):
        # если кеш заполнен, освободить
        # это не работает т к выделенный размер памяти не уменьшается
        while getsizeof(self.cache) <= self.capacity - getsizeof(value):
            self.cache.pop(self.history[0])
            self.history.pop(0)
        self.history.append(key)
        self.cache[key] = value

    def proc(self, key, func):
        value = self.get_cache(key)
        if value is None:
            cache_value = func()
            # проверка на максимальный размер кешируемого значения
            if getsizeof(cache_value) <= self.capacity:
                self.set_cache(key, cache_value)
            return cache_value
        return value


if __name__ == '__main__':
    from random import randint

    cache = Сache(5)
    for i in range(2000):
        key = randint(1, 10)
        print(f"key - {key}")
        print(cache.proc(key, lambda: "1" * randint(1, 1000)))
