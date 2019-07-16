import unittest

from .context import hlcloud
from hlcloud import policies

class PoliciesTest(unittest.TestCase):

    def test1_bucket_policy(self):
        expected_policy = {
            "bindings": [
               {
                 "members": [ "projectOwner:mgi" ],
                 "role": "roles/storage.legacyBucketOwner",
               },
            ]}

        policy = policies.bucket_policy(project="mgi")
        self.assertDictEqual(policy, expected_policy)

        expected_policy['bindings'][0]['members'] += [ 'group:mgi@wustl.edu', 'serviceAccount:mgi-users@wustl.edu' ]
        policy = policies.bucket_policy(project="mgi", group="mgi@wustl.edu", service_account="mgi-users@wustl.edu")
        self.assertDictEqual(policy, expected_policy)

# -- PoliciesTest

if __name__ == '__main__':
    unittest.main(verbosity=2)

#-- __main__
