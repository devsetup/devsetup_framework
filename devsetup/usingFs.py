# -*- coding:utf8 -*-

import os
import devsetup

class UsingFs:
	def __init__(self, step):
		self.step = step

	def chmod(self, target_file, perms):
		# does the target_file actually exist?
		self.step.log_command_start(['chmod', oct(perms), target_file])
		if not os.path.exists(target_file):
			self.step.log_command_output(["no such file"])
			self.step.log_command_result(1)
			return
		os.chmod(target_file, perms)
		self.step.log_command_result(0)

	def get_realpath(self, target_dir):
		return os.path.realpath(target_dir)

	def ensure_folder_exists(self, target_dir):
		# does the folder already exist?
		self.step.log_comment("is '%s' a folder?" % target_dir)
		if os.path.isdir(target_dir):
			self.step.log_comment_result("yes")
			return
		self.step.log_comment_result("no")

		parent = os.path.dirname(target_dir)
		self.step.log_comment("is '%s' a folder?" % target_dir)
		if os.isdir(parent):
			self.step.log_comment_result("yes")

			cmd = [ 'mkdir', target_dir ]
			popd = UsingFs(self.step).pushd(parent)
			devsetup.UsingShell(self.step).run(cmd)
			devsetup.UsingFs(self.step).popd(popd)

	def pushd(self, target_dir):
		pop_dir = os.getcwd()
		self.step.log_command_start(["cd",  "%s" % target_dir])
		os.chdir(target_dir)
		self.step.log_command_result(0)
		return pop_dir

	def popd(self, target_dir):
		self.step.log_command_start(["cd",  "-"])
		os.chdir(target_dir)
		self.step.log_command_result(0)