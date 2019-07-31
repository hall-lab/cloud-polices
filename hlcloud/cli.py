import click, json, sys, yaml

from hlcloud.version import __version__
from hlcloud import buckets
from hlcloud import policies

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version=__version__)
def hlcloud_cmd():
    """
    Hall Lab Cloud Helper Commands

    See https://github.com/hall-lab/cloud-polices/wiki for more help
    """
    pass

# BUCKETS
@click.group()
def buckets_cmd():
    """
    Commands for Buckets
    """
    pass

hlcloud_cmd.add_command(buckets_cmd, name="buckets")

@click.command(short_help="make a bucket with correct policies")
@click.argument('url', type=click.STRING)
@click.option('--service-account', '-s', type=click.STRING, help="Service account to give access to bucket.")
@click.option('--groups', '-g', type=click.STRING, help="Google group(s) to give access to bucket. If multiple groups given (via comma separation), the first group is the owner, the rest will be object admins.")
@click.option('--mbopts', '-m', type=click.STRING, help="String of options (ex location, project) to pass directly to `gsutil mb`. Otherwise, defaults will be used.")
@click.option('--user', '-u', type=click.STRING, help="User to use in bucket labels. Default is current logged in username.")
@click.option('--project', '-p', type=click.STRING, required=True, help="Project to use in bucket labels.")
@click.option('--pipeline', '-l', type=click.STRING, required=True, help="Pipeline to use in bucket labels.")
def buckets_make_cmd(url, service_account, groups, mbopts, user, project, pipeline):
    """
    Make a Googleg Cloud bucket that conforms to the Hall Lab cloud policies

    Need to provide a group, service account, or both.

    """
    if groups:
        groups = groups.split(',')
    buckets.make_bucket(
        url=url, service_account=service_account, groups=groups, mbopts=mbopts,
        labels={"user": user, "project": project, "pipeline": pipeline}
    )
buckets_cmd.add_command(buckets_make_cmd, name="make")

#-- buckets_make_cmd

@click.command(short_help="print bucket blank README")
def buckets_readme_cmd():
    """
    Print a blank bucket README. This can then be filled out and ploaded to a bucket.

    """
    sys.stdout.write( yaml.dump( policies.bucket_readme()) )
buckets_cmd.add_command(buckets_readme_cmd, name="readme")

#-- buckets_readme_cmd

@click.command(short_help="add or update bucket labels")
@click.argument('url', type=click.STRING)
@click.option('--labels', '-l', type=click.STRING, help="Google group(s) to give access to bucket. If multiple groups given (via comma separation), the first group is the owner, the rest will be object admins.")
def buckets_update_labels_cmd(url, labels):
    """
    Add or update labels on a bucket

    """
    buckets.update_label(url=url, labels=labels)
buckets_cmd.add_command(buckets_update_labels_cmd, name="update-labels")

#-- buckets_update_labels_cmd
#-- BUCKETS

# POLICIES
# - buckets
@click.group()
def policies_cmd():
    """
    Show current policy configurations for cloud resources.
    """
    pass

hlcloud_cmd.add_command(policies_cmd, name="policies")

@click.command(short_help="show current bucket policy JSON")
def policies_buckets_cmd():
    """
    Show current bucket policies with examples using groups and service accounts.

    """
    sys.stderr.write("Policy for just project owners, given no groups or serice account:\n")
    sys.stderr.write( json.dumps(policies.bucket_policy(project="PROJECT"), indent=4) )
    sys.stderr.write("\n\n---\n\nPolicy for 2 groups, including an owner group and service account:\n")
    sys.stderr.write( json.dumps(policies.bucket_policy(project="PROJECT", groups=["OWNER-GROUP@example.com", "USER-GROUP@example.com"], service_account="WORKER@example.com"), indent=4) )
policies_cmd.add_command(policies_buckets_cmd, name="buckets")

#-- policies_buckets
#-- POLICIES
