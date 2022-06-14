from objerve import watch


@watch
class M:
    watch_dict = {"foo": "set", "bar": "get", "baz": "del", "qux": "set"}
    qux = "blue"

    def __init__(self):
        self.bar = 55
        self.foo = 89
        self.baz = 121


m = M()
m.bar = 233


def abc():
    m.foo += 10


m.qux = "red"


def get_foo(m):
    m.bar


abc()
del m.baz
get_foo(m)
