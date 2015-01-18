# -*- coding:utf8 -*-

'''
dsf core module for working with the local filesystem

@author: Stuart Herbert <stuart@stuartherbert.com>

https://devsetup.systems/dsf-framework/
'''

import os
import dsf

def ensure_folder_exists(target_dir):
	"""
	Makes sure that the named folder exists. Will create it if it does
	not exist, if it can.

	You can use this in your code to guarantee that the folder you want
	will be there.

	Params:

	* target_dir: path to the folder that must exist.

	Raises RuntimeError when:

    a) target_dir already exists, but is not a folder
	b) target_dir does not exist, and we cannot create it
	"""
	# does the folder already exist?
	dsf.dslog.log_comment("is '%s' a folder?" % target_dir)
	if os.path.isdir(target_dir):
		dsf.dslog.log_comment_result("yes")
		return
	dsf.dslog.log_comment_result("no")
	if os.path.exists(target_dir):
		raise RuntimeError

	parent = os.path.dirname(target_dir)
	dsf.dslog.log_comment("is '%s' a folder?" % target_dir)
	if os.isdir(parent):
		dsf.dslog.log_comment_result("yes")
		cmd = [ 'mkdir', '-p', target_dir ]
		dsf.shell.run(cmd, cwd=parent)

	raise RuntimeError

def get_realpath(target_dir):
	"""
	Converts a path to a file/folder into its real path - stripping out
	any symlinks along the way.

	This is very handy when trying to compare two paths to see if they
	are the same or not. Some UNIX utils only output realpaths. If you
	try to compare their output to what you're expecting, this can break
	your code unless you use dsf.core.get_realpath() yourself.

	Params:

	* target_dir: a folder (can be a file instead) that we want to know
	  the realpath to.

	Returns:

	- the realpath to 'target_dir'

	Raises RuntimeError when:

	a) 'target_dir' does not exist
	"""
	if not os.path.exists(target_dir):
		raise RuntimeError

	return os.path.realpath(target_dir)

def mkdir(target_dir, mode=0755, owner="root", group="root"):
	dsf.dslog.log_command_start(["mkdir", "-p", target_dir])
	os.mkdirs(target_dir, mode)
	dsf.dslog.log_command_result(0)

	dsf.shell.run(["chown", "%s:%s" % (owner, group), target_dir])


def require_readable_folder(target_dir):
	"""
	Check to see if a folder exists on disk, and is readable. If it
	isn't, raise an exception.

	Params:

	* target_dir: path to the file to check.

	Raises RuntimeError when:

	a) 'target_dir' does not exist, or
	b) 'target_dir' exists, but is not a folder, or
	c) 'target_dir' is a file, but you can't read it
	"""
	if not os.path.isdir(unicode(target_dir)):
		raise RuntimeError
	if not os.access(target_dir, os.R_OK | os.X_OK):
		raise RuntimeError

def pushd(target_dir):
	"""
	Change folder, run the following code block, and then change back
	to the original folder before continuing.

	Example:

	    with dsf.core.fs.pushd("/tmp"):
	    	# at this point, the current working directory has been
	    	# changed to /tmp
	    	...

	    # at this point, the current working directory is back to what
	    # it was before

	Params:

	* target_dir: the folder to change to before continuing.

	Raises RuntimeError when:

	a) target_dir is not a folder
	b) target_dir is a folder, but you can't read it
	"""
	if target_dir:
		# is this a folder we're likely to be able to cd into?
		require_readable_folder(target_dir)

	# if we get here, then we're good to go
	return Dir(target_dir)

class Dir:
	def __init__(self, folder=None):
		if not folder:
			folder = os.getcwd()
		self.folder = folder
		self.orig_folder = os.getcwd()

	def __enter__(self):
		if os.path.realpath(self.folder) != os.path.realpath(self.orig_folder):
			dsf.dslog.log_command_start(["cd",  "%s" % self.folder])
			os.chdir(self.folder)
			dsf.dslog.log_command_result(0)
		return self

	def __exit__(self, type, value, traceback):
		if type is None:
			if os.path.realpath(self.folder) != os.path.realpath(self.orig_folder):
				dsf.dslog.log_command_start(["cd",  "-"])
				os.chdir(self.orig_folder)
				dsf.dslog.log_command_result(0)
