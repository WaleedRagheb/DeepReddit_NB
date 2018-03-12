# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 14:43:45 2018

@author: HP
"""

from IPython.nbformat import v3, v4

with open(r"../DataProcessing/testing.py") as fpin:
    text = fpin.read()

nbook = v3.reads_py(text)
nbook = v4.upgrade(nbook)  # Upgrade v3 to v4

jsonform = v4.writes(nbook) + "\n"
with open("testing.ipynb", "w") as fpout:
    fpout.write(jsonform)