#!/bin/bash

DEPLOY_DIR='/home/www/homemediacat/'

cp -rf ./ $DEPLOY_DIR"HM"
cp -rf ./assets $DEPLOY_DIR"assets"
cp -rf ./hm_auth $DEPLOY_DIR"hm_auth"
cp -rf ./photogal $DEPLOY_DIR"photogal"
cp -rf ./static $DEPLOY_DIR"static"
cp -rf ./templates $DEPLOY_DIR"templates"
cp -rf ./manage.py $DEPLOY_DIR"manage.py"
cp -rf ./README.md $DEPLOY_DIR"README.md"
