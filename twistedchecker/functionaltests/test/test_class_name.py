# enable: W9701

# A test class name should end with Tests (for instance, FooTests).
# Here we are assuming that a test class is any class that contains
# one or more test_* methods.

from twisted.trial import unittest


# Classes that should not be checked by the checker.
class SampleTestMixin(object):
    """
    A sample mixin with additional assertion helpers.
    """
    def assertSomething(self):
        """
        An assertion helper.
        """
        pass



class SpecializedTestCaseSubclass(unittest.TestCase):
    """
    A specialized TestCase subclass that test classes can
    inherit from. Note that even though this class inherits
    from TestCase, this class should not be checked by the
    checker, as this class does not contain a test_* method.
    """
    def doSomething(self):
        """
        Some method.
        """
        pass



# Good examples
class SomethingTests(unittest.TestCase):
    """
    A correctly named test class.
    """
    def test_something(self):
        """
        A test method.
        """



class SomethingElseTests(SampleTestMixin, unittest.TestCase):
    """
    Another correctly named test class.
    """
    def test_somethingElse(self):
        """
        A test method.
        """



class FooTests(SpecializedTestCaseSubclass):
    """
    One more correctly named test class.
    """
    def test_foo(self):
        """
        A test method.
        """



# Bad examples
class SomethingTestCase(unittest.TestCase):
    """
    An incorrectly named test class.
    """
    def test_something(self):
        """
        A test method.
        """
        pass



class SomethingElseTest(SampleTestMixin, unittest.TestCase):
    """
    Another incorrectly named test class.
    """
    def test_somethingElse(self):
        """
        A test method.
        """
        pass



class TestFoo(SpecializedTestCaseSubclass):
    """
    One more incorrectly named test class.
    """
    def test_foo(self):
        """
        A test method.
        """
        pass
