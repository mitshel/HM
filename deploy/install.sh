#!/bin/bash

DEPLOY_DIR='/home/www/homemediacat/'
MANAGE_PY=$DEPLOY_DIR"manage.py"
sudo -u www cp -rf HM assets hm_auth photogal templates static manage.py README.md $DEPLOY_DIR
sudo -u www sed -i "s/DEBUG = True/DEBUG = False/g" $DEPLOY_DIR"HM/settings.py"
sudo -u www sed -i "s/DEPLOY = False/DEPLOY = True/g" $DEPLOY_DIR"HM/settings.py"
sudo -u www python3 $MANAGE_PY collectstatic
sudo -u www python3 $MANAGE_PY migrate

