# welcome to devsetup

from __future__ import print_function
import sys
import dsf

class Step:
	def __init__(self, msg):
		# keep track of our mission
		self.operation = msg

		# tell the end-user what is happening
		if dsf.core.log.logging_to_file:
			dsf.core.console.start_new_line()
			dsf.core.console.print_bullet()
			dsf.core.console.print_message(msg)
			dsf.core.console.print_trail()

		# we'd better update the log file too
		dsf.core.log.log_new_operation(msg)

	def __enter__(self):
		return self

	def __exit__(self, etype, value, traceback):
		if not etype:
			self.okay()
			return

		# if we get here, something went wrong
		self.fail()
		dsf.core.log.log_last_exception()

		if dsf.core.log.logging_to_file:
			dsf.core.console.print_blank_line()
			dsf.core.console.print_see_logfile()
		sys.exit(1)

	def okay(self, msg=''):
		if dsf.core.log.logging_to_file:
			dsf.core.console.print_okay()

		# we'd better update the log file too
		dsf.core.log.log_operation_okay(self.operation)

	def skip(self, msg=''):
		if dsf.core.log.logging_to_file:
			dsf.core.console.print_skip()

		# we'd better update the log file too
		dsf.core.log.log_operation_skipped(self.operation)

	def fail(self, msg=''):
		if dsf.core.log.logging_to_file:
			dsf.core.console.print_fail()

		# we'd better update the log file too
		dsf.core.log.log_operation_failed(self.operation)