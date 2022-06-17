import traceback


class Descriptor:
    def __init__(self, attribute, hooks):
        self.attribute = f"_{attribute}"
        self.hooks = hooks

    def __set__(self, instance, value):
        if "set" in self.hooks:
            print(f"Set | {self.attribute[1:]} = {value}")
            self.print_stack()
        setattr(instance, self.attribute, value)

    def __get__(self, instance, owner):
        if "get" in self.hooks:
            print(f"Get | {self.attribute[1:]}")
            self.print_stack()
        return getattr(instance, self.attribute, None)

    def __delete__(self, instance):
        if "delete" in self.hooks:
            print(f"Delete | {self.attribute[1:]}")
            self.print_stack()
        delattr(instance, self.attribute)

    def print_stack(self):
        summary, *_ = traceback.extract_stack(limit=3)
        print(*traceback.format_list([summary]))


def watch(**kwargs):
    attrs = {}
    for hook in kwargs:
        for attr in kwargs[hook]:
            if attr in attrs:
                attrs[attr].append(hook)
            else:
                attrs[attr] = [hook]

    def decorator(cls):
        for attr in attrs:
            setattr(cls, attr, Descriptor(attr, attrs[attr]))
        return cls
    return decorator
