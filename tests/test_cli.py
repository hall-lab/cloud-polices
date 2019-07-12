import re, subprocess, unittest

from .context import hlcloud
from hlcloud import cli

class CliTest(unittest.TestCase):

    def test1_make_bucket(self):
        out = subprocess.check_output(['make-bucket', '--help'], stderr=subprocess.STDOUT)
        expected_help = re.compile('Usage: make\-bucket \[OPTIONS\] URL')
        self.assertRegex(str(out), expected_help)

# -- CliTest

if __name__ == '__main__':
    unittest.main(verbosity=2)

#-- __main__
