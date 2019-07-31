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

        expected_policy['bindings'][0]['members'] += [ 'group:mgi@wustl.edu' ]
        expected_policy["bindings"] +=  [{ "members": [ "group:mgi-users@wustl.edu", "user:collaborator@abc.edu", "serviceAccount:mgi-users@wustl.edu" ], "role": "roles/storage.objectAdmin" }]
        policy = policies.bucket_policy(project="mgi", groups=["mgi@wustl.edu","mgi-users@wustl.edu"], service_account="mgi-users@wustl.edu", collaborators=["collaborator@abc.edu"])
        self.assertDictEqual(policy, expected_policy)

    def test2_bucket_readme(self):
        self.assertTrue(policies.bucket_readme())

# -- PoliciesTest

if __name__ == '__main__':
    unittest.main(verbosity=2)

#-- __main__
