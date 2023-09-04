from functools import cache
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
T = TypeVar("T")


def cached_class_property(func: Callable[P, T]) -> T:
    return classmethod(property(cache(func)))
