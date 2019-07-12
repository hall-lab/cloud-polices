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
        sys.stderr.write("Setting iam...\n")
        if service_account:
            sys.stderr.write("Setting service account: {}\n".format(service_account))
            subprocess.check_call(['gsutil', 'iam', 'set', ..., url]) # FIXME:
        if group:
            sys.stderr.write("Setting group: {}\n".format(group))
            subprocess.check_call(['gsutil', 'iam', 'set', ..., url]) # FIXME:
    except CalledProcessError:
        sys.stderr.write("ERROR: Setting permission on bucket failed. Removing bucket.\n")
        subprocess.check_call(['gsutil', 'rb', url])
        raise
    sys.stderr.write("Make bucket...SUCCESS")    
