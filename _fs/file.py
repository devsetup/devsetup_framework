# -*- coding:utf8 -*-

'''
dsf module for working with the local filesystem

@author: Stuart Herbert <stuart@stuartherbert.com>

https://devsetup.systems/dsf-framework/
'''

import os
import dsf

def chmod(target_file, mode):
	"""
	Sets the UNIX permissions on a file or a folder.

	Mimics the chmod(1) command available in your UNIX shell.  Very
	handy for making files executable after you've downloaded them, for
	example.

	Params:

	* target_file: the path of the file/folder to chmod

	* mode: an octal number

	Raises RuntimeError when:

	a) 'target_file' does not exist
	b) you don't have permission to chmod 'target_file'

	TODO:

	* Accept 'rwxs'-type text version of the 'mode' param.

	  This would help users who aren't comfortable with the UNIX octal
	  mode values. Would probably make their code a little more readable
	  too.
	"""
	# does the target_file actually exist?
	dsf.dslog.log_command_start(['chmod', oct(mode), target_file])
	if not os.path.exists(target_file):
		dsf.dslog.log_command_output(["no such file"])
		dsf.dslog.log_command_result(1)
		raise RuntimeError

	os.chmod(target_file, mode)
	dsf.dslog.log_command_result(0)

def has_file(target_file):
	"""
	Check to see if a file exists on disk.

	Params:

	* target_file: path to the file to check.

	Returns:

	- True if the file exists.
	- False otherwise.
	"""
	return os.path.isfile(target_file)

def require_readable_file(target_file):
	"""
	Check to see if a file exists on disk, and is readable. If it isn't,
	raise an exception.

	Params:

	* target_file: path to the file to check.

	Raises RuntimeError when:

	a) 'target_file' does not exist, or
	b) 'target_file' exists, but is not a file, or
	c) 'target_file' is a file, but you can't read it
	"""
	if not os.path.isfile(target_file):
		raise RuntimeError
	if not os.access(target_file, os.R_OK):
		raise RuntimeError