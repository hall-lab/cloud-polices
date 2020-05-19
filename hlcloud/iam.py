import io, json, os, subprocess, sys, yaml

def groups():
    groups_fn = os.path.join(os.path.dirname(__file__), "resources", "groups.yaml")
    if not os.path.exists(groups_fn):
        sys.stderr.write("WARNING: No groups file available at {} to load available groups.".format(groups_fn))
        return []
    with open(groups_fn, "r") as f:
        groups = yaml.safe_load(f)
    return groups

#-- groups

def service_accounts():
    cmd = ["gcloud", "iam", "service-accounts", "list", "--format=json"]
    service_accounts = load_from_command(cmd)
    return service_accounts

#-- service_accounts

def load_from_command(cmd):
    return json.load( io.StringIO(subprocess.check_output(cmd).decode("utf-8")) )

#-- load_from_command
