import getpass, google.auth, subprocess, unittest
from mock import patch

from .context import hlcloud
from hlcloud.config import HLCConfig

class ConfigTest(unittest.TestCase):

    @patch('getpass.getuser')
    @patch('google.auth.default')
    def test1_hlcconfig(self, auth_patch, getuser_patch):
        credentials = "streetcred"
        project = "high-priority"
        auth_patch.return_value = (credentials, project)
        user = "rfranklin"
        getuser_patch.return_value = user
        conf = HLCConfig()
        self.assertIsNotNone(conf)
        self.assertEqual(conf.credentials, credentials)
        self.assertEqual(conf.project, project)
        self.assertEqual(conf.user, user)
        conf2 = HLCConfig()
        self.assertEqual(conf, conf2)

    @patch('getpass.getuser')
    def test1_get_user(self, getuser_patch):
        user = "rfranklin"
        getuser_patch.return_value = user
        self.assertEqual(HLCConfig.get_user(), user)

# -- ConfigTest

if __name__ == '__main__':
    unittest.main(verbosity=2)

#-- __main__
