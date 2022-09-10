import traceback
from collections import defaultdict

from objerve.color import CYAN, GREEN, YELLOW, set_color


class Hook:
    def __init__(self, name, hooks, trace_limit):
        self.public_name = name
        self.private_name = f"_{name}"
        self.hooks = hooks
        self.trace_limit = trace_limit

    def __set__(self, obj, value):
        if "set" in self.hooks:
            self.print_stack(CYAN, f"Set | {self.public_name} = {value}")
        setattr(obj, self.private_name, value)

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        else:
            value = getattr(obj, self.private_name)
            if "get" in self.hooks:
                self.print_stack(GREEN, f"Get | {self.public_name} = {value}")
            return value

    def __delete__(self, instance):
        if "delete" in self.hooks:
            self.print_stack(YELLOW, f"Delete | {self.public_name}")
        delattr(instance, self.private_name)

    def print_stack(self, color, msg):
        summary, *_ = traceback.extract_stack(limit=self.trace_limit)
        print(
            set_color(
                color, f"{msg}\n{' '.join(traceback.format_list([summary]))}"
            )
        )


def watch(**kwargs):
    attrs = defaultdict(list)
    trace_limit = kwargs.pop("trace_limit", 3)

    for hook in kwargs:
        for attr in kwargs[hook]:
            attrs[attr].append(hook)

    def inner(cls):
        for attr in attrs:
            setattr(cls, attr, Hook(attr, attrs[attr], trace_limit))
        return cls

    return inner
