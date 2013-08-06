from fabric.api import *
from fabric.contrib.files import *
import os
from copy import copy
import time

"""
	Call this with fab -H <hostname> TASK to deploy THREDDS
	Note: SSH public key must be in /home/thredds/.ssh/authorized_keys
"""

env.user = "thredds"
code_dir = "/home/thredds/maracoos_catalog"
prod_dir = "/var/tomcat/THREDDS_PROD"

def deploy_tomcat():
	git_pull()
	copy_catalog()
	restart_tomcat()

def git_pull():
	if not os.path.exists(code_dir):
		git_clone()
	with cd(code_dir):
		run("git pull origin master")

def git_clone():
	with cd("~"):
		run("rm -rf maracoos_catalog")
		run("git clone https://github.com/asascience-open/maracoos_catalog.git")

def copy_catalog():
	sudo("rsync -av %s/TDS/* %s/content/thredds/" % (code_dir, prod_dir))
	sudo("chown -R tomcat:tomcat /var/tomcat/THREDDS_PROD/content/thredds/*")

def restart_tomcat():
	sudo("service tomcat_thredds restart")

# Usually this is all that needs to be called
def deploy():
	execute(deploy_tomcat)
