import click

from hlcloud.version import __version__

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
from hlcloud.cli_buckets import buckets_cli;
hlcloud_cmd.add_command(buckets_cli, name="buckets")

# IAM
from hlcloud.iam_cli import iam_cli;
hlcloud_cmd.add_command(iam_cli, name="iam")

# POLICIES
from hlcloud.cli_policies import policies_cli;
hlcloud_cmd.add_command(policies_cli, name="policies")
