import unittest

from objerve import Hook, watch


class TestObjerve(unittest.TestCase):
    def setUp(self):
        @watch(set={"foo", "bar"}, get={"bar"}, delete={"baz"})
        class M:
            qux = "blue"

            def __init__(self):
                self.bar = 55
                self.foo = 89
                self.baz = 121

        self.m = M()

    def test_instance(self):
        bar_vars = vars(type(self.m).bar)
        self.assertIsInstance(type(self.m).bar, Hook)
        self.assertIn("get", bar_vars["hooks"])
        self.assertIn("set", bar_vars["hooks"])
        self.assertEqual("bar", bar_vars["public_name"])
        self.assertEqual("_bar", bar_vars["private_name"])

        foo_vars = vars(type(self.m).foo)
        self.assertIsInstance(type(self.m).foo, Hook)
        self.assertIn("set", foo_vars["hooks"])
        self.assertEqual("foo", foo_vars["public_name"])
        self.assertEqual("_foo", foo_vars["private_name"])

        baz_vars = vars(type(self.m).baz)
        self.assertIsInstance(type(self.m).baz, Hook)
        self.assertIn("delete", baz_vars["hooks"])
        self.assertEqual("baz", baz_vars["public_name"])
        self.assertEqual("_baz", baz_vars["private_name"])
