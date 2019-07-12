import subprocess, sys
from subprocess import CalledProcessError

def make_bucket(url, service_account=None, group=None, mbopts=None):

    if not url.startswith("gs://"):
        raise Exception("ERROR: Invalid bucket URL: gs:/test")

    if service_account is None and group is None:
        raise Exception('ERROR: Need to provide service account or group (or both) to make bucket!')

    sys.stderr.write("Make bucket: {}\n".format(url))
    cmd = ['gsutil', 'mb', url]
    if mbopts:
        cmd += mbopts
    subprocess.check_call(cmd)

    try:
        sys.stderr.write("Setting defacl...\n")
        subprocess.check_call(['gsutil', 'defacl', 'set', 'url-owner-full-control', url])
        sys.stderr.write("Setting acl...\n")
        subprocess.check_call(['gsutil', 'acl', 'set', 'private', url])
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
