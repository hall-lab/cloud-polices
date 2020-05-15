import io, json, subprocess

def service_accounts():
    cmd = ["gcloud", "iam", "service-accounts", "list", "--format=json"]
    service_accounts = load_from_command(cmd)
    return service_accounts

#-- service_accounts

def load_from_command(cmd):
    return json.load( io.StringIO(subprocess.check_output(cmd).decode("utf-8")) )

#-- load_from_cmd
