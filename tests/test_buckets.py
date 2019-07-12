import os, subprocess, sys, unittest
from io import StringIO
from mock import patch

from .context import hlcloud
from hlcloud import buckets

class BucketsTest(unittest.TestCase):

    def test1_make_bucket_fails(self):
        with self.assertRaisesRegex(Exception, "ERROR: Invalid bucket URL: gs:/test"):
            buckets.make_bucket(url="gs:/test", service_account="SA", group="G")
        with self.assertRaisesRegex(Exception, "ERROR: Need to provide service account or group \(or both\) to make bucket!"):
            buckets.make_bucket(url="gs://test")
    
    @patch('subprocess.check_call')
    def test2_make_bucket_success(self, test_patch):
        err = StringIO()
        sys.stderr = err
        
        test_patch.return_value = 1
        buckets.make_bucket(url="gs://test", service_account="SA", group="G")
        expected_err = "\n".join(["Make bucket: gs://test", "Setting defacl...", "Setting acl...",
            "Setting iam...", "Setting service account: SA", "Setting group: G", "Make bucket...SUCCESS"])
        self.assertEqual(err.getvalue(), expected_err)
        sys.stderr = sys.__stderr__

# -- BucketsTest

if __name__ == '__main__':
    unittest.main(verbosity=2)

#-- __main__
