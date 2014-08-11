# -*- coding:utf8 -*-

from Log import Log

class UsingLog:
	def __init__(self, step):
		self.step = step

	def convert_command_to_string(self, cmd):
		retval=''
		for arg in cmd:
			# are we appending to the return value?
			if len(retval) > 0:
				retval=retval+' '

			# does the arg need quoting?
			if ' ' in arg:
				if "'" in arg:
					retval=retval+"'" + arg + "'"
				else:
					retval=retval+'"' + arg + '"'
			else:
				retval=retval+arg

		# all done
		return retval

	def log_command_output(self,output):
		for line in output:
			Log.LOG_STDOUT.write(unicode(line))

	def log_command_start(self,cmd):
		# write the command to the logfile
		Log.LOG_STDOUT.write(unicode("$ " + self.convert_command_to_string(cmd) + "\n"))
		Log.LOG_STDOUT.flush()

	def log_command_result(self,retval):
		Log.LOG_STDOUT.write(unicode('# ... command exited with value ' + str(retval) + "\n\n"))
		Log.LOG_STDOUT.flush()

	def log_comment(self, msg):
		Log.LOG_STDOUT.write(unicode("# " + msg + "\n"))

	def log_comment_result(self, msg):
		Log.LOG_STDOUT.write(unicode("# ... " + msg + "\n\n"))

	def log_new_operation(self, operation):
		Log.LOG_STDOUT.write(unicode("# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"))
		Log.LOG_STDOUT.write(unicode("# " + operation + "\n\n"))

	def log_operation_okay(self, operation):
		Log.LOG_STDOUT.write(unicode("# OKAY: " + operation + "\n"))
		Log.LOG_STDOUT.write(unicode("# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\n"))

	def log_operation_failed(self, operation):
		Log.LOG_STDOUT.write(unicode("# FAILED: " + operation + "\n"))
		Log.LOG_STDOUT.write(unicode("# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\n"))

	def log_operation_skipped(self, operation):
		Log.LOG_STDOUT.write(unicode("# SKIPPED: " + operation + "\n"))
		Log.LOG_STDOUT.write(unicode("# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\n"))