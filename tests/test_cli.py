import re, subprocess, unittest

from .context import hlcloud
from hlcloud import cli

class CliTest(unittest.TestCase):

    def test0_hlcloud(self):
        expected_help = re.compile('Usage: hlcloud \[OPTIONS\] COMMAND \[ARGS\]')

        out = subprocess.check_output(['hlcloud', '--help'], stderr=subprocess.STDOUT)
        self.assertRegex(str(out), expected_help)

        out = subprocess.check_output(['hlcloud', '-h'], stderr=subprocess.STDOUT)
        self.assertRegex(str(out), expected_help)

    def test1_buckets(self):
        expected_help = re.compile('Usage: hlcloud buckets \[OPTIONS\] COMMAND \[ARGS\]')

        out = subprocess.check_output(['hlcloud', 'buckets', '--help'], stderr=subprocess.STDOUT)
        self.assertRegex(str(out), expected_help)

    def test2_buckets_make(self):
        expected_help = re.compile('Usage: hlcloud buckets make \[OPTIONS\] URL')

        out = subprocess.check_output(['hlcloud', 'buckets', 'make', '--help'], stderr=subprocess.STDOUT)
        self.assertRegex(str(out), expected_help)

# -- CliTest

if __name__ == '__main__':
    unittest.main(verbosity=2)

#-- __main__
