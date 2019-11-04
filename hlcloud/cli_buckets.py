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
@click.command(short_help="add or update bucket labels")
@click.argument('url', type=click.STRING)
@click.option('--user', '-u', type=click.STRING, required=False, help="User to use in bucket labels. Default is current logged in username.")
@click.option('--project', '-p', type=click.STRING, required=True, help="Project to use in bucket labels.")
@click.option('--pipeline', '-l', type=click.STRING, required=True, help="Pipeline to use in bucket labels.")
def buckets_update_labels_cmd(url, user, project, pipeline):
    """
    Add or update labels on a bucket

    """
    sys.stderr.write("Update bucket labels...\n")
    if not user:
        user = hlcloud.config.HLCConfig.get_user()

    storage = google.cloud.storage.Client()
    bucket = storage.get_bucket(url)
    if not bucket:
        raise Exception("No bucket for {}".format(url))

    labels = bucket.labels
    if labels is None:
        labels = dict()

    new_labels = {
        "user": user,
        "project": project,
        "pipeline": pipeline,
    }
    if new_labels == labels:
       sys.stderr("New and current bucket labels are the same, not updating.\n")
       return

    labels.update(new_labels)
    bucket.labels = labels
    sys.stderr.write("New labels:\n{}".format(yaml.dump(bucket.labels)))
    bucket.update()
    sys.stderr.write("Update bucket labels...SUCCESS\n")
buckets_cli.add_command(buckets_update_labels_cmd, name="update-labels")
