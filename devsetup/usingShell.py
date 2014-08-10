# -*- coding:utf8 -*-

from devsetup import devsetup
import subprocess
import sys

class usingShell:
	def __init__(self, step):
		self.step = step

	def run(self, cmd):
		# make sure there is a record of what we are doing
		devsetup.usingLog(self.step).command_start(cmd)

		# run the command
		retval = subprocess.call(cmd, stdout=devsetup.LOG_STDOUT, stderr=devsetup.LOG_STDERR)

		# make sure there's a record of the command's exit code
		devsetup.usingLog(self.step).command_result(retval)

		# now what do we do?
		if retval == 0:
			# the command succeeded
			return

		# if we get here, then the command failed :(
		self.step.fail()
		sys.exit(1)