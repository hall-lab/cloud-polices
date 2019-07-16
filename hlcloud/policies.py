import subprocess, sys

def bucket_policy(project, service_account=None, group=None):

    bucket_policy = {
        "bindings": [
           {
             "members": [
                 "projectOwner:{}".format(project),
             ],
             "role": "roles/storage.legacyBucketOwner",
           },
        ],
    }

    if group:
        bucket_policy['bindings'][0]['members'] += [ "group:{}".format(group) ]
    if service_account:
        bucket_policy['bindings'][0]['members'] += [ "serviceAccount:{}".format(service_account) ]

    return bucket_policy
    
#-- bucket_policy
