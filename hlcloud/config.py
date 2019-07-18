import subprocess, sys

def get_project():

    cmd = ['gcloud', 'config', 'get-value', 'project']
    project = subprocess.check_output(cmd)
    return project.decode('utf-8').rstrip()

#-- get_project
