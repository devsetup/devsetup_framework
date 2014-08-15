# welcome to devsetup

from __future__ import print_function
import sys
from devsetup.core import console, log

class Step:
	def __init__(self, msg):
		# keep track of our mission
		self.operation = msg

		# tell the end-user what is happening
		if log.logging_to_file:
			console.start_new_line()
			console.print_bullet()
			console.print_message(msg)
			console.print_trail()

		# we'd better update the log file too
		log.log_new_operation(msg)

	def __enter__(self):
		return self

	def __exit__(self, etype, value, traceback):
		if not etype:
			self.okay()
			return

		# if we get here, something went wrong
		self.fail()
		log.log_last_exception()

		if log.logging_to_file:
			console.print_blank_line()
			console.print_see_logfile()
		sys.exit(1)

	def okay(self, msg=''):
		if log.logging_to_file:
			console.print_okay()

		# we'd better update the log file too
		log.log_operation_okay(self.operation)

	def skip(self, msg=''):
		if log.logging_to_file:
			console.print_skip()

		# we'd better update the log file too
		log.log_operation_skipped(self.operation)

	def fail(self, msg=''):
		if log.logging_to_file:
			console.print_fail()

		# we'd better update the log file too
		log.log_operation_failed(self.operation)