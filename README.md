<div align="center">
  <img src="https://github.com/furkanonder/objerve/blob/main/assets/logo/objerve.png" width=300px />
  <h2>objerve</h2>
  <h3>A tiny observer for the attributes of Python objects.</h3>
  <a href="https://github.com/furkanonder/objerve/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/furkanonder/objerve"></a>
  <a href="https://github.com/furkanonder/objerve/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/furkanonder/objerve"></a>
  <a href="https://github.com/furkanonder/objerve/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/furkanonder/objerve"></a>
</div>

## Installation
_objerve_ can be installed by running `pip install objerve`

## Example Usage

Let's say you have a class like that;

```python
class M:
    qux = "blue"

    def __init__(self):
        self.bar = 55
        self.foo = 89
        self.baz = 121
```

To watch the changes, you need the add the ```@watch()```  as a class decorator. Within the arguments of the ``watch`` decorator you should pass in lists for the keyword arguments of the attributes you wish to watch.

```python
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
```
Output:
```sh
Set | foo = 89
  File "/home/blue/objerve/examples/example.py", line 9, in __init__
    self.foo = 89

Set | qux = red
  File "/home/blue/objerve/examples/example.py", line 21, in <module>
    m.qux = "red"

Get | foo
  File "/home/blue/objerve/examples/example.py", line 18, in abc
    m.foo += 10

Set | foo = 99
  File "/home/blue/objerve/examples/example.py", line 18, in abc
    m.foo += 10

Get | foo
  File "/home/blue/objerve/examples/example.py", line 29, in <module>
    m.foo

Delete | baz
  File "/home/blue/objerve/examples/example.py", line 30, in <module>
    del m.baz

Get | bar
  File "/home/blue/objerve/examples/example.py", line 25, in get_foo
    m.bar
```
