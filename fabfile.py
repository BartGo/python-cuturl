from fabric.api import run, local

def host_name():
    run('uname -s')

def prepare_deploy():
    local("./manage.py alltests")
    local("git remote -v")
    #local("git add -p && git commit")
    #local("git push")
