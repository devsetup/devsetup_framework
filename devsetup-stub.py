#!/usr/bin/env python

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# devsetup stub
# - https://github.com/devsetup/devsetup_framework.git
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# our imports
import os
import subprocess

# special case - get the devsetup framework
if not os.path.isdir("dsf"):
    subprocess.call(["git", "clone", "https://github.com/devsetup/devsetup_framework.git", "dsf"])

# load devsetup framework (dsf)
import dsf
dsf.init(__file__)

def install():
	# Your install steps go here
	pass

def main():
	install()

# make things happen
main()