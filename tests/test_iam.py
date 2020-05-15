import json, subprocess, unittest
from mock import patch

import hlcloud.iam

class IamTest(unittest.TestCase):

    @patch('subprocess.check_output')
    def test_service_accounts(self, check_output_p):
        expected_service_accounts = [
                {'disabled': False, 'displayName': 'tester', 'email': 'tester@myproject.iam.gserviceaccount.com', 'etag': 'EEE=', 'name': 'projects/myproject/tester@myproject.iam.gserviceaccount.com', 'oauth2ClientId': '1', 'projectId': 'myproject', 'uniqueId': '1'},
        ]
        check_output_p.return_value = json.dumps(expected_service_accounts).encode()
        self.assertEqual(hlcloud.iam.service_accounts(), expected_service_accounts)

    @patch('subprocess.check_output')
    def test_load_from_command(self, check_output_p):
        expected = [{ "foo": "bar", }, { "baz": "1"}]
        check_output_p.return_value = json.dumps(expected).encode()
        self.assertEqual(hlcloud.iam.load_from_command(["/bin/bash"]), expected)

# -- IamTest

if __name__ == '__main__':
    unittest.main(verbosity=2)

#-- __main__
