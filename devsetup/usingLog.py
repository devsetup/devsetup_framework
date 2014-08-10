# -*- coding:utf8 -*-

from devsetup import devsetup

# a list of the modules we need
devsetup.uses("fromLog")

class usingLog:
	def __init__(self, step):
		self.step = step

	def command_output(self,output):
		for line in output:
			devsetup.LOG_STDOUT.write(unicode(line))

	def command_start(self,cmd):
		# write the command to the logfile
		devsetup.LOG_STDOUT.write(unicode("$ " + devsetup.fromLog(self.step).convert_command_to_string(cmd) + "\n"))
		devsetup.LOG_STDOUT.flush()

	def command_result(self,retval):
		devsetup.LOG_STDOUT.write(unicode('# ... command exited with value ' + str(retval) + "\n\n"))
		devsetup.LOG_STDOUT.flush()

	def new_operation(self, operation):
		devsetup.LOG_STDOUT.write(unicode("# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"))
		devsetup.LOG_STDOUT.write(unicode("# " + operation + "\n\n"))

	def operation_okay(self, operation):
		devsetup.LOG_STDOUT.write(unicode("# OKAY: " + operation + "\n"))
		devsetup.LOG_STDOUT.write(unicode("# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\n"))

	def operation_failed(self, operation):
		devsetup.LOG_STDOUT.write(unicode("# FAILED: " + operation + "\n"))
		devsetup.LOG_STDOUT.write(unicode("# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\n"))

	def operation_skipped(self, operation):
		devsetup.LOG_STDOUT.write(unicode("# SKIPPED: " + operation + "\n"))
		devsetup.LOG_STDOUT.write(unicode("# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\n"))