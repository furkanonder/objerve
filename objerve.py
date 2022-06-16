import traceback


class Descriptor:
    def __init__(self, attribute, hook):
        self.attribute = f"_{attribute}"
        self.hook = hook

    def add_hook(self, hook):
        self.hook.append(hook)

    def __set__(self, instance, value):
        if "set" in self.hook:
            print(f"Set | {self.attribute[1:]} = {value}")
            self.print_stack()
        setattr(instance, self.attribute, value)

    def __get__(self, instance, owner):
        if "get" in self.hook:
            print(f"Get | {self.attribute[1:]}")
            self.print_stack()
        return getattr(instance, self.attribute, None)

    def __delete__(self, instance):
        if "delete" in self.hook:
            print(f"Delete | {self.attribute[1:]}")
            self.print_stack()
        delattr(instance, self.attribute)

    def print_stack(self):
        summary, *_ = traceback.extract_stack(limit=3)
        print(*traceback.format_list([summary]))


def watch(**kwargs):
    def decorator(cls):
        for kwarg in kwargs:
            for attr in kwargs[kwarg]:
                try:
                    attribute = getattr(cls, attr)
                    attribute.add_hook(kwarg)
                except:
                    setattr(cls, attr, Descriptor(attr, [kwarg]))
        return cls
    return decorator
