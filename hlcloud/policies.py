import subprocess, sys

def bucket_policy(project, groups=None, service_account=None):

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

    object_admin_members = []
    if groups:
        bucket_policy['bindings'][0]['members'] += [ "group:{}".format(groups[0]) ]
        for g in groups[1:]:
            object_admin_members += [ "group:{}".format(g) ]

    if service_account:
        object_admin_members += [ "serviceAccount:{}".format(service_account) ]

    if object_admin_members:
        bucket_policy['bindings'] += [{
            "members": object_admin_members,
            "role": "roles/storage.objectAdmin",
        }]

    return bucket_policy
    
#-- bucket_policy
