#!/bin/bash

DEPLOY_DIR='/home/www/homemediacat/'

sudo -u www cp -rf HM assets hm_auth photogal templates manage.py README.md $DEPLOY_DIR

