import functools


class Calculator:

    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        return functools.reduce(lambda x, y: x * y, args)

    @staticmethod
    def divide(*args):
        return functools.reduce(lambda x, y: x / y, args)

    @staticmethod
    def subtract(*args):
        return functools.reduce(lambda x, y: x - y, args)
