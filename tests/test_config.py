import subprocess, unittest
from mock import patch

from .context import hlcloud
from hlcloud import config

class ConfigTest(unittest.TestCase):

    @patch('subprocess.check_output')
    def test1_get_project(self, test_patch):
        test_patch.return_value = bytes('mgi\n', 'utf-8')
        project = config.get_project()
        self.assertEqual(project, "mgi")

    def test2_get_user(self):
        user = config.get_user()
        self.assertTrue(user)

# -- ConfigTest

if __name__ == '__main__':
    unittest.main(verbosity=2)

#-- __main__
