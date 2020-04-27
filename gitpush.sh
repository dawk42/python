#!/usr/bin/bash
#updated --all to have two dashes
git pull
git add --all
git commit -m "$*"
git push
