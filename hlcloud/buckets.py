import json, subprocess, sys, tempfile
from subprocess import CalledProcessError

from hlcloud import config, policies

def make_bucket(url, service_account=None, groups=[], labels={}, mbopts=None):
    sys.stderr.write("Make bucket: {}\n".format(url))

    if not url.startswith("gs://"):
        raise Exception("ERROR: Invalid google bucket URL: {}".format(url))

    if service_account is None and ( groups == None or len(groups) == 0 ):
        raise Exception('ERROR: Need to provide service account or group (or both) to make bucket!')

    if not 'user' in labels or labels['user'] is None:
        labels['user'] = config.get_user()
    sys.stderr.write("User: {}\n".format(labels['user']))

    for req in ["project", "pipeline"]:
        if not req in labels or labels[req] is None:
            raise Exception("ERROR: Required label not found: {}".format(req))
        sys.stderr.write("{}: {}\n".format(req.capitalize(), labels[req]))

    cloud_project = config.get_project()
    sys.stderr.write("Google cloud project: {}\n".format(cloud_project))

    cmd = ['gsutil', 'mb']
    if mbopts:
        cmd += mbopts.split(' ')
    cmd += [url]
    sys.stderr.write("Running: {}\n".format(" ".join(cmd)))
    subprocess.check_call(cmd)

    iam_policy = policies.bucket_policy(project=cloud_project, groups=groups, service_account=service_account)

    with tempfile.NamedTemporaryFile(mode='w') as f:
        f.write(json.dumps(iam_policy))
        f.flush()

        try:
            cmd = [ "gsutil", "iam", "set", f.name, url ]
            sys.stderr.write("Running: {}\n".format(" ".join(cmd)))
            subprocess.check_call(cmd)

        except CalledProcessError:
            sys.stderr.write("ERROR: Setting IAM/ACLs on bucket failed. Attempting to remove bucket.\n")
            subprocess.check_call(['gsutil', 'rb', url])
            raise

    try:
        update_labels(url=url, labels=["user:{}".format(labels['user']), "project:{}".format(labels['project']), "pipeline:{}".format(labels['pipeline'])])

    except:
        sys.stderr.write("ERROR: Failed to update labels on bucket. Attempting to remove bucket.\n")
        subprocess.check_call(['gsutil', 'rb', url])
        raise

    sys.stderr.write("Make bucket...SUCCESS\n")

#-- make_bucket

def update_labels(url, labels):

    cmd = ['gsutil', 'label', 'ch']
    for l in labels:
        cmd += ['-l', l]
    cmd += [url]
    sys.stderr.write("Running: {}\n".format(" ".join(cmd)))
    subprocess.check_call(cmd)
    sys.stderr.write("Update bucket labels...SUCCESS\n")

#-- add_labels
