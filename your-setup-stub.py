#!/usr/bin/env python

# our imports
import os
import subprocess
import sys
import time

# special case - get the devsetup framework
if not os.path.isdir("devsetup"):
    subprocess.call(["git", "clone", "https://github.com/devsetup/devsetup.git"])

# load devsetup
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "devsetup"))
import devsetup
devsetup.init(__file__)

def install():
	# Your install steps go here

def main():
	install()

# make things happen
main()