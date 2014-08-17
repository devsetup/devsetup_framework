# -*- coding:utf8 -*-

import os
import dsf

def chmod(target_file, perms):
	# does the target_file actually exist?
	dsf.core.log.log_command_start(['chmod', oct(perms), target_file])
	if not os.path.exists(target_file):
		dsf.core.log.log_command_output(["no such file"])
		dsf.core.log.log_command_result(1)
		return
	os.chmod(target_file, perms)
	dsf.core.log.log_command_result(0)

def ensure_folder_exists(target_dir):
	# does the folder already exist?
	dsf.core.log.log_comment("is '%s' a folder?" % target_dir)
	if os.path.isdir(target_dir):
		dsf.core.log.log_comment_result("yes")
		return
	dsf.core.log.log_comment_result("no")

	parent = os.path.dirname(target_dir)
	dsf.core.log.log_comment("is '%s' a folder?" % target_dir)
	if os.isdir(parent):
		dsf.core.log.log_comment_result("yes")
		cmd = [ 'mkdir', target_dir ]
		dsf.core.shell.run(cmd, cwd=parent)

def get_realpath(target_dir):
	return os.path.realpath(target_dir)

def has_file(target_file):
	return os.path.exists(target_file)

def pushd(target_dir):
	return Dir(target_dir)

class Dir:
	def __init__(self, folder=None):
		if not folder:
			folder = os.getcwd()
		self.folder = folder
		self.orig_folder = os.getcwd()

	def __enter__(self):
		if self.folder != self.orig_folder:
			dsf.core.log.log_command_start(["cd",  "%s" % self.folder])
			os.chdir(self.folder)
			dsf.core.log.log_command_result(0)
		return self

	def __exit__(self, type, value, traceback):
		if type is None:
			if self.folder != self.orig_folder:
				dsf.core.log.log_command_start(["cd",  "-"])
				os.chdir(self.orig_folder)
				dsf.core.log.log_command_result(0)
