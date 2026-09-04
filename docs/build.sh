#!/bin/sh
set -e

python3 -m pip install -r requirements.txt
mkdocs build