import re, subprocess, unittest
from mock import MagicMock, Mock, patch
from click.testing import CliRunner

from .context import hlcloud
from hlcloud import cli_buckets

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

    @patch("google.cloud.storage.Client")
    def test3_buckets_update_labels(self, client_patch):
        expected_help = re.compile('Usage: hlcloud buckets update-labels \[OPTIONS\] URL')

        out = subprocess.check_output(['hlcloud', 'buckets', 'update-labels', '--help'], stderr=subprocess.STDOUT)
        self.assertRegex(str(out), expected_help)

        client = Mock()
        client_patch.return_value = client
        bucket = Mock()
        bucket.labels = None
        bucket.update = MagicMock(return_value=1)
        client.get_bucket = MagicMock(return_value=bucket)

        runner = CliRunner()
        url = "gs://mgi-bucket"
        labels = {
            "user": "rfranklin",
            "project": "mgi-project",
            "pipeline": "mgi_pipeline",
        }
        result = runner.invoke(cli_buckets.buckets_update_labels_cmd, [url, "-u", labels["user"], "-p", labels["project"], "-l", labels["pipeline"]])

        expected_output = """
        Update bucket labels...
        New labels:
            pipeline: mgi_pipeline
            project: mgi-project
            user: rfranklin
            Update bucket labels...SUCCESS
"""
        self.assertEqual(result.exit_code, 0)

        client.get_bucket.assert_called_with(url)
        self.assertEqual(bucket.labels, labels)
        bucket.update.assert_called

# -- CliBucketsTest

if __name__ == '__main__':
    unittest.main(verbosity=2)

#-- __main__
