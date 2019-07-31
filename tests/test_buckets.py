import os, subprocess, sys, unittest
from io import StringIO
from mock import patch

from .context import hlcloud
from hlcloud import buckets, config

class BucketsTest(unittest.TestCase):

    def test1_make_bucket_fails(self):
        err = StringIO()
        sys.stderr = err

        with self.assertRaisesRegex(Exception, "ERROR: Invalid google bucket URL: gs:/test"):
            buckets.make_bucket(url="gs:/test", service_account="SA", groups="G")
        with self.assertRaisesRegex(Exception, "ERROR: Need to provide service account or group \(or both\) to make bucket!"):
            buckets.make_bucket(url="gs://test")

        with self.assertRaisesRegex(Exception, "ERROR: Required label not found: project"):
            buckets.make_bucket(url="gs://test", service_account="SA", groups="G", labels={"pipeline": "mgi-pipeline"})
        with self.assertRaisesRegex(Exception, "ERROR: Required label not found: project"):
            buckets.make_bucket(url="gs://test", service_account="SA", groups="G", labels={"project": None, "pipeline": "mgi-pipeline"})

        with self.assertRaisesRegex(Exception, "ERROR: Required label not found: pipeline"):
            buckets.make_bucket(url="gs://test", service_account="SA", groups="G", labels={"project": "mgi-project"})
        with self.assertRaisesRegex(Exception, "ERROR: Required label not found: pipeline"):
            buckets.make_bucket(url="gs://test", service_account="SA", groups="G", labels={"project": "mgi-project", "pipeline": None})

        sys.stderr = sys.__stderr__
    
    @patch('hlcloud.config.get_project')
    @patch('hlcloud.config.get_user')
    @patch('subprocess.check_call')
    def test2_make_bucket_success(self, patch_check_call, patch_get_user, patch_get_project):
        err = StringIO()
        sys.stderr = err
        
        patch_check_call.return_value = 1
        patch_get_project.return_value = "mgi-cloud"
        patch_get_user.return_value = "mgi-user"
        buckets.make_bucket(url="gs://test", service_account="SA", groups="G1", collaborators=["C1@abc.edu", "C2@abc.edu"], labels={"project": "mgi-project", "pipeline": "mgi-pipeline"})
        expected_err = "\n".join([
            "Make bucket: gs://test",
            "User: mgi-user",
            "Project: mgi-project",
            "Pipeline: mgi-pipeline",
            "Google cloud project: mgi-cloud",
            "Running: gsutil mb gs://test",
            "Running: gsutil iam set /tmp/[\w\d]+ gs://test",
            "Running: gsutil label ch -l user:mgi-user -l project:mgi-project -l pipeline:mgi-pipeline gs://test",
            "Update bucket labels\.\.\.SUCCESS",
            "Make bucket\.\.\.SUCCESS"])
        self.assertRegex(err.getvalue(), expected_err)
        sys.stderr = sys.__stderr__

    @patch('subprocess.check_call')
    def test3_update_labels_success(self, test_patch):
        err = StringIO()
        sys.stderr = err

        test_patch.return_value = 1
        buckets.update_labels(url="gs://test", labels=["user:mgi-user", "project:genome", "pipeline:aln"])
        expected_err = "\n".join([
            "Running: gsutil label ch -l user:mgi-user -l project:genome -l pipeline:aln gs://test",
            "Update bucket labels\.\.\.SUCCESS"])
        self.assertRegex(err.getvalue(), expected_err)
        sys.stderr = sys.__stderr__

# -- BucketsTest

if __name__ == '__main__':
    unittest.main(verbosity=2)

#-- __main__
