#!/bin/bash

# Deploy script for GitLab CI

DEPLOY_DIR='/home/www/homemediacat/'
MANAGE_PY=$DEPLOY_DIR"manage.py"
sudo -u www cp -rf HM assets hm_auth photogal templates static manage.py README.md $DEPLOY_DIR
#sudo -u www sed -i "s/DEBUG = True/DEBUG = False/g" $DEPLOY_DIR"HM/settings.py"
sudo -u www sed -i "s/DEPLOY = False/DEPLOY = True/g" $DEPLOY_DIR"HM/settings.py"
sudo -u www python3 $MANAGE_PY collectstatic --noinput
sudo -u www python3 $MANAGE_PY migrate
sudo /usr/bin/systemctl restart uwsgi


