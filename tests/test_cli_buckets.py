import re, subprocess, unittest
from mock import MagicMock, Mock, patch
from click.testing import CliRunner

from .context import hlcloud
from hlcloud import cli_buckets

class CliBucketsTest(unittest.TestCase):

    def test0_buckets(self):
        expected_help = re.compile('Usage: hlcloud buckets \[OPTIONS\] COMMAND \[ARGS\]')

        out = subprocess.check_output(['hlcloud', 'buckets', '--help'], stderr=subprocess.STDOUT)
        self.assertRegex(str(out), expected_help)

    def test1_bucket_readme(self):
        expected_help = re.compile('Usage: hlcloud buckets readme \[OPTIONS\]')

        out = subprocess.check_output(['hlcloud', 'buckets', 'readme', '--help'], stderr=subprocess.STDOUT)
        self.assertRegex(str(out), expected_help)

# -- CliBucketsTest

if __name__ == '__main__':
    unittest.main(verbosity=2)

#-- __main__
