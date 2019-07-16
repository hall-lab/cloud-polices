import json, subprocess, sys, tempfile
from subprocess import CalledProcessError

from hlcloud import config, policies

def make_bucket(url, service_account=None, group=None, mbopts=None):

    if not url.startswith("gs://"):
        raise Exception("ERROR: Invalid google bucket URL: {}".format(url))

    if service_account is None and group is None:
        raise Exception('ERROR: Need to provide service account or group (or both) to make bucket!')

    sys.stderr.write("Make bucket: {}\n".format(url))
    cmd = ['gsutil', 'mb', url]
    if mbopts:
        cmd += mbopts
    sys.stderr.write("Running: {}\n".format(" ".join(cmd)))
    subprocess.check_call(cmd)

    project = config.get_project()
    sys.stderr.write("Project ID: {}\n".format(project))

    iam_policy = policies.bucket_policy(project=project, group=group, service_account=service_account)

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

    sys.stderr.write("Make bucket...SUCCESS")

#-- make_bucket
