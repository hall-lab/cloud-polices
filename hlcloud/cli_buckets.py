import click, google, yaml, sys
import hlcloud.config

# BUCKET CLI
@click.group()
def buckets_cli():
    """
    Commands for Buckets
    """
    pass

# LIST
from hlcloud.cli_buckets_list import buckets_list_cmd
buckets_cli.add_command(buckets_list_cmd, name="list")

# MAKE
from hlcloud.cli_buckets_make import buckets_make_cmd
buckets_cli.add_command(buckets_make_cmd, name="make")

# README
@click.command(short_help="print bucket blank README")
def buckets_readme_cmd():
    """
    Print a blank bucket README tempate. This can then be filled out and ploaded to a bucket.

    """
    sys.stdout.write( yaml.dump( policies.buckets_readme()) )
buckets_cli.add_command(buckets_readme_cmd, name="readme")

# UPDATE LABELS
from hlcloud.cli_buckets_update_labels import buckets_update_labels_cmd
buckets_cli.add_command(buckets_update_labels_cmd, name="update-labels")
