import traceback
from collections import defaultdict

from objerve.color import CYAN, GREEN, YELLOW, set_color


class Descriptor:
    def __init__(self, attribute, hooks, trace_limit):
        self.attribute = f"_{attribute}"
        self.hooks = hooks
        self.trace_limit = trace_limit

    def __set__(self, instance, value):
        if "set" in self.hooks:
            print(f"{set_color(CYAN, 'Set')} | {self.attribute[1:]} = {value}")
            self.print_stack(CYAN)
        setattr(instance, self.attribute, value)

    def __get__(self, instance, owner):
        if "get" in self.hooks:
            print(f"{set_color(GREEN, 'Get')} | {self.attribute[1:]}")
            self.print_stack(GREEN)
        return getattr(instance, self.attribute, None)

    def __delete__(self, instance):
        if "delete" in self.hooks:
            print(f"{set_color(YELLOW, 'Delete')} | {self.attribute[1:]}")
            self.print_stack(YELLOW)
        delattr(instance, self.attribute)

    def print_stack(self, color):
        summary, *_ = traceback.extract_stack(limit=self.trace_limit)
        print(f"{set_color(color, *traceback.format_list([summary]))}")


def watch(**kwargs):
    attrs = defaultdict(list)
    trace_limit = kwargs.pop("trace_limit", 3)

    for hook in kwargs:
        for attr in kwargs[hook]:
            attrs[attr].append(hook)

    def inner(cls):
        for attr in attrs:
            setattr(cls, attr, Descriptor(attr, attrs[attr], trace_limit))
        return cls

    return inner
