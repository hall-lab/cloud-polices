import re, subprocess, unittest

class CliBucketsTest(unittest.TestCase):

    def test0_buckets(self):
        expected_help = re.compile('Usage: hlcloud buckets \[OPTIONS\] COMMAND \[ARGS\]')

        out = subprocess.check_output(['hlcloud', 'buckets', '--help'], stderr=subprocess.STDOUT)
        self.assertRegex(str(out), expected_help)

    def test1_buckets_make(self):
        expected_help = re.compile('Usage: hlcloud buckets make \[OPTIONS\] URL')

        out = subprocess.check_output(['hlcloud', 'buckets', 'make', '--help'], stderr=subprocess.STDOUT)
        self.assertRegex(str(out), expected_help)

    def test2_bucket_readme(self):
        expected_help = re.compile('Usage: hlcloud buckets readme \[OPTIONS\]')

        out = subprocess.check_output(['hlcloud', 'buckets', 'readme', '--help'], stderr=subprocess.STDOUT)
        self.assertRegex(str(out), expected_help)

    def test3_buckets_update_labels(self):
        expected_help = re.compile('Usage: hlcloud buckets update-labels \[OPTIONS\] URL')

        out = subprocess.check_output(['hlcloud', 'buckets', 'update-labels', '--help'], stderr=subprocess.STDOUT)
        self.assertRegex(str(out), expected_help)

# -- CliTest

if __name__ == '__main__':
    unittest.main(verbosity=2)

#-- __main__
