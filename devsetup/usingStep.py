# welcome to devsetup

from __future__ import print_function
from devsetup import devsetup

# a list of the modules we need
devsetup.uses("usingConsole")
devsetup.uses("usingLog")

class usingStep:
	def __init__(self, msg):
		# keep track of our mission
		self.operation = msg

		# tell the end-user what is happening
		devsetup.usingConsole(self).start_new_line()
		devsetup.usingConsole(self).print_bullet()
		devsetup.usingConsole(self).print_message(msg)
		devsetup.usingConsole(self).print_trail()

		# we'd better update the log file too
		devsetup.usingLog(self).new_operation(msg)

	def okay(self, msg=''):
		devsetup.usingConsole(self).print_okay()

		# we'd better update the log file too
		devsetup.usingLog(self).operation_okay(self.operation)

	def skip(self, msg=''):
		devsetup.usingConsole(self).print_skip()

		# we'd better update the log file too
		devsetup.usingLog(self).operation_skipped(self.operation)

	def fail(self, msg=''):
		devsetup.usingConsole(self).print_fail()

		# we'd better update the log file too
		devsetup.usingLog(self).operation_failed(self.operation)
