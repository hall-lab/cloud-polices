import re, subprocess, unittest
from click.testing import CliRunner
from mock import patch

from hlcloud.iam_cli import cli, list_cmd
import hlcloud.iam

class IamCliTest(unittest.TestCase):

    def test_cli(self):
        runner = CliRunner()
        result = runner.invoke(cli, [])
        self.assertEqual(result.exit_code, 0)
        result = runner.invoke(cli, ["--help"])
        self.assertEqual(result.exit_code, 0)

    @patch("hlcloud.iam.groups")
    @patch("hlcloud.iam.service_accounts")
    def test_list_cmd(self, sa_p, g_p):
        runner = CliRunner()
        result = runner.invoke(list_cmd, ["--help"])
        self.assertEqual(result.exit_code, 0)

        g_p.return_value = ["g1"]
        sa_p.return_value = [{"email": "sa1@google.com"}]
        result = runner.invoke(list_cmd, [])
        try:
            self.assertEqual(result.exit_code, 0)
        except:
            print(result.output)
            raise
        expected_output = """EMAIL           TYPE
--------------  ---------------
sa1@google.com  SERVICE_ACCOUNT
g1@wustl.edu    GROUP"""
        self.assertEqual(result.output, expected_output)


# -- IamCliTest

if __name__ == '__main__':
    unittest.main(verbosity=2)

#-- __main__
