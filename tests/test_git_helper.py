import unittest
from src.git_helper import get_commits


class TestGitHelper(unittest.TestCase):
    def test_get_commits(self):
        commits = get_commits('C:\\Users\\noubuk\\source\\python mirea\\shell_task')
        self.assertIsInstance(commits, list)
        self.assertGreater(len(commits), 0)
        for commit in commits:
            self.assertEqual(len(commit), 4)


if __name__ == "__main__":
    unittest.main()
