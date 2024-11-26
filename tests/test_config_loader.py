import unittest
from src.config_loader import load_config


class TestConfigLoader(unittest.TestCase):
    def test_load_config(self):
        config = load_config('C:\\Users\\noubuk\\source\\python mirea\\git_graphviz\\config.ini')
        self.assertEqual(config['graphviz_path'], 'C:\\Graphviz\\bin\\dot.exe')
        self.assertEqual(config['repo_path'], 'C:\\Users\\noubuk\\source\\python mirea\\shell_task')
        self.assertEqual(config['output_path'], 'C:\\Users\\noubuk\\source\\python mirea\\git_graphviz\\output\\output.png')
        self.assertEqual(config['branch_name'], 'main')


if __name__ == "__main__":
    unittest.main()
