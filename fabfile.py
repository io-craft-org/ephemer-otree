# encoding: utf-8

"""
Fabfile to drive development and deployment of ephemer-otree

Usage: fab deploy --hosts=...

original authors : raphael.marvie@beta.gouv.fr, guillaume.libersat@beta.gouv.fr
"""

from fabric import task

PROJECT_NAME = "ephemer-otree"
GIT_REPO_URL = f"git@github.com:io-craft-org/{PROJECT_NAME}.git"


@task
def upgrade(cnx):
    """Upgrade requirements to last version on server for site"""
    cnx.run(
        f"cd www/{PROJECT_NAME} "
        f"&& git pull "
        f"&& source ./venv/bin/activate "
        f"&& pip install --upgrade --requirement requirements.txt"
    )


@task
def deploy(cnx):
    """Deploy new version of project to server for site"""
    cnx.run(
        f"cd ./www "
        f"&& git clone {GIT_REPO_URL} "
        f"&& cd ./{PROJECT_NAME} "
        f"&& python3 -m venv venv "
        f"&& source ./venv/bin/activate "
        f"&& pip install --requirement requirements.txt "
    )
