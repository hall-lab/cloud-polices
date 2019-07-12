import subprocess, sys
from subprocess import CalledProcessError

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

    try:
        cmd = [ 'gsutil', 'defacl', 'set', 'url-owner-full-control', url ]
        sys.stderr.write("Running: {}\n".format(" ".join(cmd)))
        subprocess.check_call(cmd)

        cmd = [ 'gsutil', 'acl', 'set', 'private', url ]
        sys.stderr.write("Running: {}\n".format(" ".join(cmd)))
        subprocess.check_call(cmd)

        cmd = [ "gsutil", "iam", "ch" ]
        if service_account:
            cmd += [ "serviceAccount:{}:storage.objectAdmin".format(service_account) ]
        if group:
            cmd += [ "group:{}:storage.objectAdmin".format(group) ]
        sys.stderr.write("Running: {}\n".format(" ".join(cmd)))
        subprocess.check_call(cmd)

    except CalledProcessError:
        sys.stderr.write("ERROR: Setting IAM/ACLs on bucket failed. Attempting to remove bucket.\n")
        subprocess.check_call(['gsutil', 'rb', url])
        raise

    sys.stderr.write("Make bucket...SUCCESS")

#-- make_bucket
