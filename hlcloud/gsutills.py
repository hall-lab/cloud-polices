import subprocess

def ls():
    cmd = ["gsutil", "ls"]
    out = subprocess.check_output(cmd)
    return out.split("\n")

#-- ls
