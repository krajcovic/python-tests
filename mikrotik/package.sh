#!/bin/bash

python3 setup.py check
python3 setup.py sdist
#python3 setup.py bdist_wininst
python3 setup.py upload