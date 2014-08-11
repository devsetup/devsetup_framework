# welcome to devsetup

from __future__ import print_function
from UsingConsole import UsingConsole
from UsingLog import UsingLog

class Step:
	def __init__(self, msg):
		# keep track of our mission
		self.operation = msg

		# tell the end-user what is happening
		UsingConsole(self).start_new_line()
		UsingConsole(self).print_bullet()
		UsingConsole(self).print_message(msg)
		UsingConsole(self).print_trail()

		# we'd better update the log file too
		UsingLog(self).log_new_operation(msg)

	def okay(self, msg=''):
		UsingConsole(self).print_okay()

		# we'd better update the log file too
		UsingLog(self).log_operation_okay(self.operation)

	def skip(self, msg=''):
		UsingConsole(self).print_skip()

		# we'd better update the log file too
		UsingLog(self).log_operation_skipped(self.operation)

	def fail(self, msg=''):
		UsingConsole(self).print_fail()

		# we'd better update the log file too
		UsingLog(self).log_operation_failed(self.operation)

	def log_comment(self, msg):
		UsingLog(self).log_comment(msg)

	def log_comment_result(self, msg):
		UsingLog(self).log_comment_result(msg)

	def log_command_start(self, cmd):
		UsingLog(self).log_command_start(cmd)

	def log_command_output(self, output):
		UsingLog(self).log_command_output(output)

	def log_command_result(self, result):
		UsingLog(self).log_command_result(result)