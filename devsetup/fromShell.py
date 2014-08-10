# -*- coding:utf8 -*-

from devsetup import devsetup
import subprocess

# a list of the modules we need
devsetup.uses('usingLog')

class fromShell:
	def __init__(self, step):
		self.step = step

	def getOutputFromCommand(self, cmd):
		# make sure there is a record of what we are doing
		devsetup.usingLog(self.step).command_start(cmd)

		# run the command
		p1 = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

		# get the output
		output = p1.communicate()

		# put a copy of the output in the log file
		devsetup.usingLog(self.step).command_output(output)
		devsetup.usingLog(self.step).command_result(p1.returncode)

		# all done
		return output
