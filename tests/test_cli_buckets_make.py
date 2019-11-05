import io, re, subprocess, sys, unittest
from mock import patch
from click.testing import CliRunner

from .context import hlcloud
from hlcloud import cli_buckets_make

class CliBucketsMakeTest(unittest.TestCase):

    @patch('subprocess.check_call')
    @patch('getpass.getuser')
    @patch('google.auth.default')
    def test_buckets_make(self, auth_patch, getuser_patch, checkcall_patch):
        credentials = "streetcred"
        project = "mgi-cloud"
        auth_patch.return_value = (credentials, project)
        getuser_patch.return_value = "mgi-user"
        checkcall_patch.return_value = 1

        runner = CliRunner()
        result = runner.invoke(cli_buckets_make.buckets_make_cmd, ["gs://test", "--service-account", "SA", "--groups", "G1", "--collaborators", "C1@abc.edu,C2@abc.edu", "-p", "mgi-project", "-l", "mgi-pipeline"])
        if result.exception:
            print("{}".format(result.exception))
        self.assertEqual(result.exit_code, 0)

        expected_out = "\n".join([
            "Make bucket: gs://test",
            "Running: gsutil mb gs://test",
            "Running: gsutil iam set /tmp/[\w\d]+ gs://test",
            "Running: gsutil defacl set bucket-owner-full-control gs://test",
            "Running: gsutil label ch -l user:mgi-user -l project:mgi-project -l pipeline:mgi-pipeline gs://test",
            "Make bucket\.\.\.SUCCESS"])
        self.assertRegex(result.output, expected_out)

# -- CliBucketsMakeTest

if __name__ == '__main__':
    unittest.main(verbosity=2)

#-- __main__
