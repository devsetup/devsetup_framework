# -*- coding:utf8 -*-

import os
from devsetup import devsetup

# a list of the modules we need
devsetup.uses("usingLog")

class usingFs:
	def __init__(self, step):
		self.step = step

	def pushd(self, target_dir):
		pop_dir = os.getcwd()
		devsetup.usingLog(self.step).command_start(["cd",  "%s" % target_dir])
		os.chdir(target_dir)
		devsetup.usingLog(self.step).command_result(0)
		return pop_dir

	def popd(self, target_dir):
		devsetup.usingLog(self.step).command_start(["cd",  "-"])
		os.chdir(target_dir)
		devsetup.usingLog(self.step).command_result(0)