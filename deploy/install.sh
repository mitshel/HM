#!/bin/bash

DEPLOY_DIR='/home/www/homemediacat/'
sudo -u www cp -rf HM assets hm_auth photogal templates static manage.py README.md $DEPLOY_DIR
sudo -u www sed -i "s/DEBUG = True/DEBUG = False/g" $DEPLOY_DIR"HM/settings.py"

