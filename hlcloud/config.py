import subprocess, sys

def get_project():

    cmd = ['gcloud', 'config', 'get-value', 'project']
    project = subprocess.check_output(cmd)#.rstrip()
    return str(project.rstrip())

#-- get_project
