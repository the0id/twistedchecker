from pylint.interfaces import IASTNGChecker
from pylint.checkers import BaseChecker

from twistedchecker.core.util import isTestModule


class TestClassNameChecker(BaseChecker):
    """
    A checker for checking test class names.

    Test classes should be named FooTests, where Foo is the name
    of the component/feature being tested.
    """
    msgs = {
        'W9701': ('Test class names should end with Tests',
                  'Used for checking test class names.'),
    }
    __implements__ = IASTNGChecker
    name = 'testclassname'
    options = ()

    def visit_module(self, node):
        """
        An interface will be called when visiting a module.

        @param node: node of current module
        """
        if isTestModule(node.name):
            self._checkTestClassNames(node)


    def _isTestClass(self, line, lines):
        """
        Check whether a class is a test class. Here we assume that a
        test class is any class that contains one or more test_*
        methods.

        @param line: The line that starts a class definition.
        @type line: L{str}

        @param lines: The lines of the node being checked as returned
            by node.file_stream.readlines().
        @type lines: L{list} of L{str}

        @return: A L{bool} representing whether a class is a test class
            or not.
        @rtype: L{bool}
        """
        linenum = lines.index(line) + 1
        for codeline in lines[linenum:]:
            if codeline == '\n':
                continue
            # Check for indentation
            if codeline.startswith('    '):
                strippedLine = codeline.strip()
                if strippedLine.startswith('def'):
                    # Extract the function name
                    functionName = strippedLine.split('(')[0].split()[1]
                    if functionName.startswith('test_'):
                        return True
            else:
                return False


    def _checkTestClassNames(self, node):
        """
        Check whether test classes are named correctly. A test
        class name should end with Tests (for instance, FooTests).

        @param node: node of current module
        """
        lines = node.file_stream.readlines()
        for linenum, line in enumerate(lines):
            if line.startswith('class')and self._isTestClass(line, lines):
                # Extract the test class name
                testClassName = line.split('(')[0].split()[1]
                if not testClassName.endswith('Tests'):
                    self.add_message('W9701', line=linenum + 1)
