import os
import unittest
from src.dependency_graph import DependencyGraph


class TestDependencyGraph(unittest.TestCase):
    def setUp(self):
        self.graph = DependencyGraph('C:\\Graphviz\\bin\\dot.exe', 'C:\\Users\\noubuk\\source\\python mirea\\shell_task',
                                     'C:\\Users\\noubuk\\source\\python mirea\\git_graphviz\\output\\output.png')

    def test_build_graph(self):
        self.graph.build_graph()
        with open('graph.dot') as f:
            content = f.read()
            self.assertIn('digraph G {', content)

    def test_run(self):
        self.graph.run()
        self.assertTrue(os.path.exists('C:\\Users\\noubuk\\source\\python mirea\\git_graphviz\\output\\output.png'))


if __name__ == "__main__":
    unittest.main()
