#!/bin/bash

cd "$(dirname "$0")"
pipenv run python ipdf.py compress $1 -v --overwrite
