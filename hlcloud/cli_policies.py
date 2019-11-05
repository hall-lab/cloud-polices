import click, json, sys, yaml

from hlcloud import policies

# POLICIES
# BUCKETS
@click.group()
def policies_cli():
    """
    Show current policy configurations for cloud resources.
    """
    pass

@click.command(short_help="show current bucket policy JSON")
def policies_buckets_cmd():
    """
    Show current bucket policies with examples using groups and service accounts.

    """
    sys.stderr.write("Policy for just PROJECT OWNERS, given no groups, users, or serice account:\n\n")
    sys.stderr.write( json.dumps(policies.bucket_policy(project="PROJECT"), indent=4) )
    sys.stderr.write("\n\n---\n\nPolicy for 2 groups (including an owner group), collaborators, and service account:\n")
    sys.stderr.write( json.dumps( policies.bucket_policy(project="PROJECT", groups=["OWNER-GROUP@example.com", "USER-GROUP@example.com"], service_account="WORKER@example.com", collaborators=["COLLABORATOR@abc.edu"]),
        indent=4))
policies_cli.add_command(policies_buckets_cmd, name="buckets")
