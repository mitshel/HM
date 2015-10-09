#!/bin/bash

DEPLOY_DIR='/home/www/homemediacat/'

cp -rf HM assets hm_auth photogal static templates manage.py README.md $DEPLOY_DIR

rem cp -rf ./HM $DEPLOY_DIR"HM"
rem cp -rf ./assets $DEPLOY_DIR"assets"
rem cp -rf ./hm_auth $DEPLOY_DIR"hm_auth"
rem cp -rf ./photogal $DEPLOY_DIR"photogal"
rem cp -rf ./static $DEPLOY_DIR"static"
rem cp -rf ./templates $DEPLOY_DIR"templates"
rem cp -rf ./manage.py $DEPLOY_DIR"manage.py"
rem cp -rf ./README.md $DEPLOY_DIR"README.md"
