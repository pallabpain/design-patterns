#!/usr/bin/env python3

class Singleton(type):
    def __call__(cls, *args, **kwargs):
        try:
            return cls.__instance
        except AttributeError:
            cls.__instance = super(Singleton, cls).__call__(*args, **kwargs)
            return cls.__instance


class Router(metaclass=Singleton):

    def __init__(self): # __init__() is invoked only once
        self.__routes = []

    def add_routes(self, routes):
        self.__routes.extend(routes)

    def get_routes(self):
        return self.__routes


if __name__ == "__main__":
    router = Router()
    router.add_routes(["/api/user", "/api/book"])
    print(router.get_routes())

    new_router = Router()
    new_router.add_routes(["/api/v1/devices", "/api/v1/network"])
    print(new_router.get_routes())

    assert(router == new_router)
