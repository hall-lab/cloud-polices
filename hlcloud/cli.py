import click, sys

from hlcloud.version import __version__
from hlcloud import buckets

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

# buckets_make_cmd
@click.command(short_help="make a bucket with correct policies")
@click.argument('url', type=click.STRING)
@click.option('--service-account', '-s', type=click.STRING, help="Service account to give access to bucket.")
@click.option('--groups', '-g', type=click.STRING, help="Google group(s) to give access to bucket. If multiple groups given (via comma separation), the first group is the owner, the rest will be object admins.")
@click.option('--mbopts', '-m', type=click.STRING, help="String of options (ex location, project) to pass directly to `gsutil mb`. Otherwise, defaults will be used.")
def buckets_make_cmd(url, service_account, groups, mbopts):
    """
    Make a Google Cloud Bucket with Permissions that Conform to the Hall Lab Cloud Policies

    Need to provide a group, service account, or both.

    """
    buckets.make_bucket(url=url, service_account=service_account, groups=groups.split(','), mbopts=mbopts)
buckets_cmd.add_command(buckets_make_cmd, name="make")

#-- buckets_make_cmd
#-- BUCKETS
