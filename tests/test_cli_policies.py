import re, subprocess, unittest

class CliPolicyTest(unittest.TestCase):

    def test0_polices(self):
        expected_help = re.compile('Usage: hlcloud policies \[OPTIONS\] COMMAND \[ARGS\]')

        out = subprocess.check_output(['hlcloud', 'policies', '--help'], stderr=subprocess.STDOUT)
        self.assertRegex(str(out), expected_help)

    def test1_policies_buckets(self):
        expected_help = re.compile('Usage: hlcloud policies buckets \[OPTIONS\]')

        out = subprocess.check_output(['hlcloud', 'policies', 'buckets', '--help'], stderr=subprocess.STDOUT)
        self.assertRegex(str(out), expected_help)

# -- CliPolicyTest

if __name__ == '__main__':
    unittest.main(verbosity=2)

#-- __main__
