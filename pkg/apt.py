# -*- coding:utf8 -*-

'''
dsf core module for working with Debian / Ubuntu 'apt' package manager

@author: Stuart Herbert <stuart@stuartherbert.com>

https://devsetup.systems/dsf-framework/
'''

import dsf

def install(pkg):
	"""
	Uses 'apt' to install the given package

	Params:

	* pkg: the name of the package to install. Can be a single string
	  or a list of packages
	"""

	cmd = ["apt-get", "install" ]
	if type(cmd) in (tuple, list):
		cmd = cmd + pkg
	else:
		cmd = cmd + [ pkg ]

	dsf.core.shell.run(cmd)