import subprocess, sys, unittest
from mock import patch

from .context import hlcloud
from hlcloud import gsutills

class GsutillsTest(unittest.TestCase):

    @patch('subprocess.check_output')
    def test1_ls(self, patch):
        patch.return_value = "gs://test\ngs:://test-2\n"
        buckets_list = gsutills.ls()

        expected = patch.return_value.split("\n")
        self.assertEqual(buckets_list, expected)
        sys.stdout = sys.__stdout__

# -- GsutillsTest

if __name__ == '__main__':
    unittest.main(verbosity=2)

#-- __main__
