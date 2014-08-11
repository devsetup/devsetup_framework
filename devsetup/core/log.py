# -*- coding:utf8 -*-

import io
import os

LOG_STDOUT=None
LOG_STDERR=None

def init(project_folder):
	global LOG_STDOUT
	global LOG_STDERR

	# where will the logfile live?
	log_filename = os.path.join(project_folder, "devsetup.log")

	# create it
	logfile = io.open(log_filename, "w")

	# all done
	LOG_STDOUT = logfile
	LOG_STDERR = logfile

def convert_command_to_string(cmd):
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

def log_command_output(output):
	global LOG_STDOUT

	for line in output:
		LOG_STDOUT.write(unicode(line))

def log_command_start(cmd):
	global LOG_STDOUT

	# write the command to the logfile
	LOG_STDOUT.write(unicode("$ " + convert_command_to_string(cmd) + "\n"))
	LOG_STDOUT.flush()

def log_command_result(retval):
	global LOG_STDOUT

	LOG_STDOUT.write(unicode('# ... command exited with value ' + str(retval) + "\n\n"))
	LOG_STDOUT.flush()

def log_comment(msg):
	global LOG_STDOUT
	LOG_STDOUT.write(unicode("# " + msg + "\n"))

def log_comment_result(msg):
	global LOG_STDOUT
	LOG_STDOUT.write(unicode("# ... " + msg + "\n\n"))

def log_new_operation(operation):
	global LOG_STDOUT
	LOG_STDOUT.write(unicode("# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"))
	LOG_STDOUT.write(unicode("# " + operation + "\n\n"))

def log_operation_okay(operation):
	global LOG_STDOUT
	LOG_STDOUT.write(unicode("# OKAY: " + operation + "\n"))
	LOG_STDOUT.write(unicode("# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\n"))

def log_operation_failed(operation):
	global LOG_STDOUT
	LOG_STDOUT.write(unicode("# FAILED: " + operation + "\n"))
	LOG_STDOUT.write(unicode("# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\n"))

def log_operation_skipped(operation):
	global LOG_STDOUT
	LOG_STDOUT.write(unicode("# SKIPPED: " + operation + "\n"))
	LOG_STDOUT.write(unicode("# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\n"))