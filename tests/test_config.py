import subprocess, sys, unittest
from io import StringIO
from mock import patch

from .context import hlcloud
from hlcloud import config

class ConfigTest(unittest.TestCase):

    @patch('subprocess.check_output')
    def test1_get_project(self, test_patch):
        err = StringIO()
        sys.stderr = err
        
        test_patch.return_value = b'mgi\n'
        config.get_project()
        expected_err = "\n".join([
            "Running: gcloud config get-value project",
            ""])
        self.assertEqual(err.getvalue(), expected_err)
        sys.stderr = sys.__stderr__

# -- ConfigTest

if __name__ == '__main__':
    unittest.main(verbosity=2)

#-- __main__
