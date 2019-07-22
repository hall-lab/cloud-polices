import json, subprocess, sys, unittest
from mock import patch

from .context import hlcloud
from hlcloud import gsutils

class GsutilsTest(unittest.TestCase):

    @patch('subprocess.check_output')
    def test1_ls(self, patch):
        patch.return_value = "gs://test\ngs:://test-2\n"
        buckets_list = gsutils.ls()

        expected = patch.return_value.split("\n")
        self.assertEqual(buckets_list, expected)


    @patch('subprocess.check_output')
    def test2_bucket_iam(self, patch):
        expected_iam =  {
            "bindings": [
               {
                   "members": [ "projectOwner:washu-genome-inh-dis-analysis" ],
                   "role": "roles/storage.legacyBucketOwner",
               },
               {
                   "members": [ "group:green-hall-lab-collab@wustl.edu", "user:mhauknes@ucsc.edu", "user:mmescalo@ucsc.edu" ],
                   "role": "roles/storage.objectAdmin",
               },
            ],
        }
        patch.return_value = json.dumps(expected_iam)
        iam = gsutils.bucket_iam(url="gs://test")
        self.assertEqual(iam, expected_iam)

# -- GsutilsTest

if __name__ == '__main__':
    unittest.main(verbosity=2)

#-- __main__
