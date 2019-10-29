import click, yaml, sys

# BUCKET CLI
@click.group()
def buckets_cli():
    """
    Commands for Buckets
    """
    pass

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
@click.option('--labels', '-l', type=click.STRING, help="Google group(s) to give access to bucket. If multiple groups given (via comma separation), the first group is the owner, the rest will be object admins.")
def buckets_update_labels_cmd(url, labels):
    """
    Add or update labels on a bucket

    """
    cmd = ['gsutil', 'label', 'ch']
    for l in labels:
        cmd += ['-l', l]
    cmd += [url]
    sys.stderr.write("Running: {}\n".format(" ".join(cmd)))
    subprocess.check_call(cmd)
    sys.stderr.write("Update bucket labels...SUCCESS\n")
buckets_cli.add_command(buckets_update_labels_cmd, name="update-labels")
