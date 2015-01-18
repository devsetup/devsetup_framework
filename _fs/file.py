# -*- coding:utf8 -*-

'''
dsf module for working with the local filesystem

@author: Stuart Herbert <stuart@stuartherbert.com>

https://devsetup.systems/dsf-framework/
'''

import os
import shutil
import time

import dsf

def file_pair(source_file, target_file, cache_for=3600, cwd=None):
	retval = FilePair(source_file, target_file, cache_for=cache_for, cwd=cwd)
	return retval


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

def copy(source_file, target_file, mode=0644):
	"""
	Copys source_file to target_file

	Params:

	* source_file: the file to copy

	* target_file: where to copy the source_file to

	* mode: the file permissions to set on the new file

	Raises RuntimeError when:

	a) 'source_file' does not exist
	b) cannot create 'target_file'
	c) you do not have permission to chmod 'target_file'
	"""

	dsf.dslog.log_command_start(['copy', source_file, target_file, oct(mode)])
	if not os.path.exists(source_file):
		dsf.dslog.log_command_output(["source file not found"])
		dsf.dslog.log_command_result(1)
		raise RuntimeError

	try:
		shutil.copy(source_file, target_file)
	except IOError:
		dsf.dslog.log_command_output(["failed to copy to target file"])
		dsf.dslog.log_command_result(1)
		raise RuntimeError

	chmod(target_file, mode)

def gunzip(source_file, cwd=None, cache=360, force=False):
	with dsf.dir.pushd(cwd):
		target_file=os.path.splitext()[0]

		# is the file too new to overwrite?
		if not force:
			if os.path.isfile(target_file):
				details = os.stat(target_file)
				if details.st_mtime > time.time() - cache:
					return

		# uncompress the file
		if dsf.shell.run(["gunzip", "-f", source_file]) is not 0:
			raise RuntimeError

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


def is_cached(source_file=None, target_file=None, cache_for=3600, cwd=None):
	"""
	Check to see if a file is recent enough or not.  Can be used to check the age
	of just the target_file, or to also make sure that the (optional) source_file
	isn't newer than the target_file.

	Params:

	* source_file: the file used to create the target_file (optional)
	* target_file: the file to check the age of
	* cache_for: how old target_file can be before it's no longer considered valid (optional)
	* cwd: the folder where source_file and/or target_file are (optional)

	Returns:

	* True if target_file exists and isn't too old
	* False otherwise

	Raises:

	* RuntimeError if source_file is specified, but does not exist
	"""

	with dsf.dir.pushd(cwd):
		# does the target file exist?
		if not os.path.exists(target_file):
			# no - cannot be cached
			return False

		# get the details for the target file
		target_details = os.stat(target_file)

		# is the target file too old?
		if target_details.st_mtime < time.time() - cache_for:
			# too old
			return False

		# do we have a source file to check against?
		if source_file is None:
			# at this point, we're happy with the age of the target file
			return True

		# if we get to here, we need to make sure that the target file
		# isn't older than the source file
		if not os.path.exists(source_file):
			raise RuntimeError("source file '%s' does not exist" % source_file)

		source_details = os.stat(source_file)
		if source_details.st_mtime > target_details.st_mtime:
			return False

		# at this point, we're happy that the target file isn't too
		# old
		return True


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


class FilePair(object):
	def __init__(self, source_file, target_file, cache_for=None, cwd=None):
		# remember our constructor params
		self.source_file = source_file
		self.target_file = target_file
		self.cache_for = cache_for
		self.cwd = cwd

		# gather facts about our file pair
		self.is_cached = is_cached(source_file=source_file, target_file=target_file, cache_for=cache_for, cwd=cwd)

		# work out whether the caller needs to act or not
		self.act = True
		if self.is_cached:
			self.act = False

	def __enter__(self):
		return self

	def __exit__(self, type, value, traceback):
		if type is None:
			pass
