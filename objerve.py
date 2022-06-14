import traceback


class Descriptor:
    def __init__(self, attribute, hook):
        self.attribute = f"_{attribute}"
        self.hook = hook

    def __set__(self, instance, value):
        if self.hook == "set":
            print(f"Set | {self.attribute[1:]} = {value}")
            self.print_stack()
        setattr(instance, self.attribute, value)

    def __get__(self, instance, owner):
        if self.hook == "get":
            print(f"Get | {self.attribute[1:]}")
            self.print_stack()
        return getattr(instance, self.attribute, None)

    def __delete__(self, instance):
        if self.hook == "del":
            print(f"Delete | {self.attribute[1:]}")
            self.print_stack()
        delattr(instance, self.attribute)

    def print_stack(self):
        summary, *_ = traceback.extract_stack(limit=3)
        print(*traceback.format_list([summary]))


def watch(cls):
    for key, val in cls.watch_dict.items():
        setattr(cls, key, Descriptor(key, val))
    return cls
