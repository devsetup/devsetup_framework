# -*- coding:utf8 -*-

'''
dsf module for working with a MySQL server

@author: Stuart Herbert <stuart@stuartherbert.com>

https://devsetup.systems/dsf-framework/
'''

import pwd
import os

import dsf

def create_user(username, groups=None):
	if not user_exists(username):
		# create the user
		dsf.shell.run(["useradd", "-m", username])


def user_exists(username):
	try:
		if pwd.getpwnam(username) is None:
			return False

		return True
	except KeyError:
		return False