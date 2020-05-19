import click, sys, tabulate

import hlcloud.iam

@click.group()
def cli():
    """
    Commands for IAM Enities
    """
    pass

@click.command()
def list_cmd():
    """
    List service accounts and groups 
    """
    rows = []
    for sa in hlcloud.iam.service_accounts():
        rows.append([sa["email"], "SERVICE_ACCOUNT"])
    for g in hlcloud.iam.groups():
        rows.append(["{}@{}".format(g, "wustl.edu"), "GROUP"])
    sys.stdout.write(tabulate.tabulate(rows, ["EMAIL", "TYPE"]))
cli.add_command(list_cmd, 'list')
