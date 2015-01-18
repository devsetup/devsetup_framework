# -*- coding:utf8 -*-

import io
import os
import sys
import traceback

LOG_STDOUT=sys.stdout
LOG_STDERR=sys.stderr
logging_to_file=True
logfile="devsetup.log"

def init(project_folder, write_to_log=True):
	global LOG_STDOUT
	global LOG_STDERR
	global logging_to_file
	global logfile

	# special case - we want to log directly to the screen
	if not write_to_log:
		logging_to_file = False
		return

	# if we get here, then we are logging
	# to a file

	# where will the logfile live?
	log_filename = os.path.join(project_folder, logfile)

	# create it
	logfile_handle = io.open(log_filename, "w")

	# all done
	LOG_STDOUT = logfile_handle
	LOG_STDERR = logfile_handle

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

def flush():
	LOG_STDOUT.flush()
	LOG_STDERR.flush()

def log_command_output(output):
	global LOG_STDOUT

	for line in output:
		LOG_STDOUT.write(unicode(line))

	LOG_STDOUT.flush()

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
	global logging_to_file

	if logging_to_file:
		LOG_STDOUT.write(unicode("# " + msg + "\n"))
		LOG_STDOUT.flush()

def log_comment_result(msg):
	global LOG_STDOUT
	global logging_to_file

	if logging_to_file:
		LOG_STDOUT.write(unicode("# ... " + msg + "\n\n"))
		LOG_STDOUT.flush()

def log_last_exception():
	if logging_to_file:
		LOG_STDOUT.write(unicode("This resulted in the following exception:\n\n"))
		output = traceback.format_exc()
		LOG_STDOUT.write(unicode(output))
		LOG_STDOUT.flush()

def log_new_operation(operation):
	global LOG_STDOUT
	global logging_to_file

	if logging_to_file:
		LOG_STDOUT.write(unicode("# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"))
		LOG_STDOUT.write(unicode("# " + operation + "\n\n"))
		LOG_STDOUT.flush()

def log_operation_okay(operation):
	global LOG_STDOUT
	global logging_to_file

	if logging_to_file:
		LOG_STDOUT.write(unicode("# OKAY: " + operation + "\n"))
		LOG_STDOUT.write(unicode("# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\n"))
		LOG_STDOUT.flush()

def log_operation_failed(operation):
	global LOG_STDOUT
	global logging_to_file

	if logging_to_file:
		LOG_STDOUT.write(unicode("# FAILED: " + operation + "\n"))
		LOG_STDOUT.write(unicode("# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\n"))
		LOG_STDOUT.flush()

def log_operation_skipped(operation):
	global LOG_STDOUT
	global logging_to_file

	if logging_to_file:
		LOG_STDOUT.write(unicode("# SKIPPED: " + operation + "\n"))
		LOG_STDOUT.write(unicode("# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\n"))
		LOG_STDOUT.flush()
