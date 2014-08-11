# -*- coding:utf8 -*-

import os
import log, shell

def chmod(target_file, perms):
	# does the target_file actually exist?
	log.log_command_start(['chmod', oct(perms), target_file])
	if not os.path.exists(target_file):
		log.log_command_output(["no such file"])
		log.log_command_result(1)
		return
	os.chmod(target_file, perms)
	log.log_command_result(0)

def get_realpath(target_dir):
	return os.path.realpath(target_dir)

def ensure_folder_exists(target_dir):
	# does the folder already exist?
	log.log_comment("is '%s' a folder?" % target_dir)
	if os.path.isdir(target_dir):
		log.log_comment_result("yes")
		return
	log.log_comment_result("no")

	parent = os.path.dirname(target_dir)
	log.log_comment("is '%s' a folder?" % target_dir)
	if os.isdir(parent):
		log.log_comment_result("yes")

		cmd = [ 'mkdir', target_dir ]
		popd = pushd(parent)
		shell.run(cmd)
		popd(popd)

def pushd(target_dir):
	pop_dir = os.getcwd()
	log.log_command_start(["cd",  "%s" % target_dir])
	os.chdir(target_dir)
	log.log_command_result(0)
	return pop_dir

def popd(target_dir):
	log.log_command_start(["cd",  "-"])
	os.chdir(target_dir)
	log.log_command_result(0)