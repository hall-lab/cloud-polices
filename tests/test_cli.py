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

    def test11_buckets(self):
        expected_help = re.compile('Usage: hlcloud buckets \[OPTIONS\] COMMAND \[ARGS\]')

        out = subprocess.check_output(['hlcloud', 'buckets', '--help'], stderr=subprocess.STDOUT)
        self.assertRegex(str(out), expected_help)

    def test12_buckets_make(self):
        expected_help = re.compile('Usage: hlcloud buckets make \[OPTIONS\] URL')

        out = subprocess.check_output(['hlcloud', 'buckets', 'make', '--help'], stderr=subprocess.STDOUT)
        self.assertRegex(str(out), expected_help)

    def test13_bucket_readme(self):
        expected_help = re.compile('Usage: hlcloud buckets readme \[OPTIONS\]')

        out = subprocess.check_output(['hlcloud', 'buckets', 'readme', '--help'], stderr=subprocess.STDOUT)
        self.assertRegex(str(out), expected_help)

    def test14_buckets_update_labels(self):
        expected_help = re.compile('Usage: hlcloud buckets update-labels \[OPTIONS\] URL')

        out = subprocess.check_output(['hlcloud', 'buckets', 'update-labels', '--help'], stderr=subprocess.STDOUT)
        self.assertRegex(str(out), expected_help)

    def test2_polices(self):
        expected_help = re.compile('Usage: hlcloud policies \[OPTIONS\] COMMAND \[ARGS\]')

        out = subprocess.check_output(['hlcloud', 'policies', '--help'], stderr=subprocess.STDOUT)
        self.assertRegex(str(out), expected_help)

    def test21_policies_buckets(self):
        expected_help = re.compile('Usage: hlcloud policies buckets \[OPTIONS\]')

        out = subprocess.check_output(['hlcloud', 'policies', 'buckets', '--help'], stderr=subprocess.STDOUT)
        self.assertRegex(str(out), expected_help)

# -- CliTest

if __name__ == '__main__':
    unittest.main(verbosity=2)

#-- __main__
