# -*- coding:utf8 -*-

'''
dsf core module for working with Debian / Ubuntu 'apt' package manager

@author: Stuart Herbert <stuart@stuartherbert.com>

https://devsetup.systems/dsf-framework/
'''

import os
import dsf

def install(pkg):
	"""
	Uses 'apt' to install the given package

	Params:

	* pkg: the name of the package to install. Can be a single string
	  or a list of packages
	"""

	# make sure we force non-interactive mode for apt (grrr)
	os.environ["DEBIAN_FRONTEND"] = "noninteractive"

	# build the command to run apt
	cmd = ["apt-get", "install", "-y" ]
	if type(cmd) in (tuple, list):
		for pkg in cmd:
			cmd.append(pkg)
	else:
		cmd.append(pkg)

	# run the command, and make sure it worked
	retval = dsf.shell.run(cmd)
	if retval != 0:
		raise RuntimeError("apt-get install failed")