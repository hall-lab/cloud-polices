import json, subprocess, sys, tempfile
from subprocess import CalledProcessError

from hlcloud import policies
from hlcloud.config import HLCConfig

import click

# MAKE
@click.command(short_help="make a bucket with correct permissions and policies")
@click.argument('url', type=click.STRING)
@click.option('--service-account', '-s', type=click.STRING, help="Service account to give access to bucket.")
@click.option('--groups', '-g', type=click.STRING, help="Google group(s) to give access to bucket. If multiple groups given (via comma separation), the first group is the owner, the rest will be object admins.")
@click.option('--collaborators', '-c', type=click.STRING, help="Collaborator email addresses to give ADMIN OBJECT access to bucket. Give multiple email addresses via comma separation.")
@click.option('--mbopts', '-m', type=click.STRING, help="String of options (ex location, project) to pass directly to `gsutil mb`. Otherwise, defaults will be used.")
@click.option('--user', '-u', type=click.STRING, help="User to use in bucket labels. Default is current logged in username.")
@click.option('--project', '-p', type=click.STRING, required=True, help="Project to use in bucket labels.")
@click.option('--pipeline', '-l', type=click.STRING, required=True, help="Pipeline to use in bucket labels.")
def buckets_make_cmd(url, service_account, groups, collaborators, mbopts, user, project, pipeline):
    """
    Make a Google Cloud bucket that conforms to the Hall Lab cloud policies

    Need to provide a group, service account, or both.
    """
    config = HLCConfig()
    sys.stderr.write("Make bucket: {}\n".format(url))

    if groups:
        groups = groups.split(',')
    if collaborators:
        collaborators = collaborators.split(',')
    buckets.make_bucket(
        url=url, service_account=service_account, groups=groups, collaborators=collaborators, mbopts=mbopts,
        labels={"user": user, "project": project, "pipeline": pipeline}
    )

    if not url.startswith("gs://"):
        raise Exception("ERROR: Invalid google bucket URL: {}".format(url))

    if service_account is None and ( groups == None or len(groups) == 0 ):
        raise Exception('ERROR: Need to provide service account or group (or both) to make bucket!')

    if not 'user' in labels or labels['user'] is None:
        labels['user'] = config.user
    sys.stderr.write("Labels:\n User: {}\n".format(labels['user']))

    for req in ["project", "pipeline"]:
        if not req in labels or labels[req] is None:
            raise Exception("ERROR: Required label not found: {}".format(req))
        sys.stderr.write(" {}: {}\n".format(req.capitalize(), labels[req]))

    cloud_project = config.project
    sys.stderr.write("Google cloud project: {}\n".format(cloud_project))

    cmd = ['gsutil', 'mb']
    if mbopts:
        cmd += mbopts.split(' ')
    cmd += [url]
    sys.stderr.write("Running: {}\n".format(" ".join(cmd)))
    subprocess.check_call(cmd)

    iam_policy = policies.bucket_policy(project=cloud_project, groups=groups, service_account=service_account, collaborators=collaborators)

    with tempfile.NamedTemporaryFile(mode='w') as f:
        f.write(json.dumps(iam_policy))
        f.flush()

        try:
            cmd = [ "gsutil", "iam", "set", f.name, url ]
            sys.stderr.write("Running: {}\n".format(" ".join(cmd)))
            subprocess.check_call(cmd)

            cmd = [ "gsutil", "defacl", "set", "bucket-owner-full-control", url ]
            sys.stderr.write("Running: {}\n".format(" ".join(cmd)))
            subprocess.check_call(cmd)

        except CalledProcessError:
            sys.stderr.write("ERROR: Setting IAM/ACLs on bucket failed. Attempting to remove bucket.\n")
            subprocess.check_call(['gsutil', 'rb', url])
            raise

    try:
        update_labels(url=url, labels=["user:{}".format(labels['user']), "project:{}".format(labels['project']), "pipeline:{}".format(labels['pipeline'])])

    except:
        sys.stderr.write("ERROR: Failed to update labels on bucket. Attempting to remove bucket.\n")
        subprocess.check_call(['gsutil', 'rb', url])
        raise

    sys.stderr.write("Make bucket...SUCCESS\n")
#-- buckets_make_cmd
