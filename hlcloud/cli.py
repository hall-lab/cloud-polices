import click, sys

from hlcloud import buckets

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
#@click.group(context_settings=CONTEXT_SETTINGS)
#@click.version_option(version=__version__)

# make_bucket cmd

@click.command()
@click.argument('url', type=click.STRING)
@click.option('--service-account', '-s', type=click.STRING, help="Service account to give access to bucket.")
@click.option('--group', '-g', type=click.STRING, help="Google group to give access to bucket.")
@click.option('--mbopts', '-m', type=click.STRING, help="String of options (ex location, project) to pass directly to `gsutil mb`. Otherwise, defaults will be used.")
def make_bucket(url, service_account, group, mbopts):
    """
    Make a Google Cloud Bucket with Permiesions that Conform to the Hall Lab Cloud Policies

    Need to provide a group, service account, or both.

    """
    buckets.make_bucket(url=url, service_account=service_account, group=group, mbopts=mbopts)

#-- make_bucket
