from ConcreteFlyweight import *


class FlyweightFactory:
    """
    Create and manage flyweight objects.
    Ensure that flyweights are shared properly. When a client requests a
    flyweight, the FlyweightFactory object supplies an existing instance
    or creates one, if none exists.
    """

    def __init__(self):
        self._flyweights = {}

    def get_flyweight(self, key):
        # print("You are asking for an object with intrinsic value", key)
        key_parts = key.split(',')
        try:
            flyweight = self._flyweights[key]
        except KeyError:
            flyweight = ConcreteFlyweight()
            flyweight.set_color(key_parts[0])
            flyweight.set_shape(key_parts[1])
            self._flyweights[key] = flyweight
        return flyweight

    def count_flyweights(self):
        return len(self._flyweights.keys())
