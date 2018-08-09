#!/usr/bin/env bash
python user.py > /dev/null &
nosetests --with-coverage