import json, subprocess

def ls():
    cmd = ["gsutil", "ls"]
    out = subprocess.check_output(cmd)
    return out.split("\n")

#-- ls

def bucket_iam(url):
    cmd = ["gsutil", "iam", "get", url]
    out = subprocess.check_output(cmd)
    return json.loads(out)

#-- bucket_iam
