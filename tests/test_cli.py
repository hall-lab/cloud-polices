import re, subprocess, unittest

class CliTest(unittest.TestCase):

    def test_hlcloud(self):
        expected_help = re.compile('Usage: hlcloud \[OPTIONS\] COMMAND \[ARGS\]')

        out = subprocess.check_output(['hlcloud', '--help'], stderr=subprocess.STDOUT)
        self.assertRegex(str(out), expected_help)

        out = subprocess.check_output(['hlcloud', '-h'], stderr=subprocess.STDOUT)
        self.assertRegex(str(out), expected_help)

# -- CliTest

if __name__ == '__main__':
    unittest.main(verbosity=2)

#-- __main__
