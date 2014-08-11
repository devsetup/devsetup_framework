# -*- coding:utf8 -*-

import subprocess
import sys

from Log import Log
import devsetup

class UsingShell:
	def __init__(self, step):
		self.step = step

	def get_output_from_command(self, cmd, cwd=None):
		# are we changing folders first?
		if cwd:
			popd = devsetup.UsingFs(self.step).pushd(cwd)

		# make sure there is a record of what we are doing
		self.step.log_command_start(cmd)

		# run the command
		p1 = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

		# get the output
		output = p1.communicate()

		# put a copy of the output in the log file
		self.step.log_command_output(output)
		self.step.log_command_result(p1.returncode)

		# did we run this in a different folder?
		if cwd:
			devsetup.UsingFs(self.step).popd(popd)

		# all done
		return output

	def run(self, cmd, cwd=None):
		# are we changing folders first?
		if cwd:
			popd = devsetup.UsingFs(self.step).pushd(cwd)

		# make sure there is a record of what we are doing
		self.step.log_command_start(cmd)

		# run the command
		retval = subprocess.call(cmd, stdout=Log.LOG_STDOUT, stderr=Log.LOG_STDERR)

		# make sure there's a record of the command's exit code
		self.step.log_command_result(retval)

		# now what do we do?
		if retval == 0:
			# the command succeeded
			if cwd:
				devsetup.UsingFs(self.step).popd(popd)
			return

		# if we get here, then the command failed :(
		self.step.fail()
		sys.exit(1)