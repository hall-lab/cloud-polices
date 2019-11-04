import re, subprocess, unittest
from mock import MagicMock, Mock, patch
from click.testing import CliRunner

from .context import hlcloud
from hlcloud import cli_buckets_list

class CliBucketsListTest(unittest.TestCase):

    @patch("google.cloud.storage.Client")
    def test_buckets_list(self, client_patch):
        expected_help = re.compile('Usage: hlcloud buckets list')

        out = subprocess.check_output(['hlcloud', 'buckets', 'list', '--help'], stderr=subprocess.STDOUT)
        self.assertRegex(str(out), expected_help)

        client = Mock()
        client_patch.return_value = client
        bucket = Mock()
        bucket.name = "BUCKET"
        bucket.storage_class = "REGIONAL"
        bucket.location = "US-CENTRAL1"
        bucket.labels = {
            "user": "rfranklin",
            "project": "mgi-project",
            "pipeline": "mgi_pipeline",
        }
        bucket.update = MagicMock(return_value=1)
        client.list_buckets = MagicMock(return_value=[bucket])

        runner = CliRunner()
        result = runner.invoke(cli_buckets.buckets_list_cmd)
        self.assertEqual(result.exit_code, 0)

        expected_output = """NAME    LOCATION     CLASS     USER       PROJECT      PIPELINE
------  -----------  --------  ---------  -----------  ------------
BUCKET  US-CENTRAL1  REGIONAL  rfranklin  mgi-project  mgi_pipeline"""
        self.assertEqual(result.output, expected_output)

        client.list_buckets.assert_called()
        bucket.update.assert_called

# -- CliBucketsTest

if __name__ == '__main__':
    unittest.main(verbosity=2)

#-- __main__
