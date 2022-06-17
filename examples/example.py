from objerve import watch

@watch(set={"foo", "qux"}, get={"bar", "foo"}, delete={"baz"})
class M:
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
m.foo
del m.baz
get_foo(m)