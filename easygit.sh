#!/usr/bin/bash
set -r
git add .
git commit -m $1
git push
