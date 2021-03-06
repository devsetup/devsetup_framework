# -*- coding:utf8 -*-

import subprocess

import dsf

def get_output_from_command(cmd, cwd=None):
	# what is the command we are actually going to run?
	cmd_to_run = _command_to_string(cmd)

	with dsf.core.fs.pushd(cwd):
		# make sure there is a record of what we are doing
		dsf.dslog.log_command_start(cmd_to_run)

		# run the command
		p1 = subprocess.Popen(cmd_to_run, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

		# get the output
		output = p1.communicate()

		# put a copy of the output in the log file
		dsf.dslog.log_command_output(output)
		dsf.dslog.log_command_result(p1.returncode)

		# all done
		return output

def run(cmd, cwd=None):
	with dsf.core.fs.pushd(cwd):
		cmd_to_run = _command_to_string(cmd)

		# make sure there is a record of what we are doing
		dsf.dslog.log_command_start(cmd_to_run)

		# run the command
		retval = subprocess.call(cmd_to_run, stdout=dsf.dslog.LOG_STDOUT, stderr=dsf.dslog.LOG_STDERR)

		# make sure there's a record of the command's exit code
		dsf.dslog.log_command_result(retval)

		# let the caller raise the exception - it makes things much
		# easier to understand when looking at the logs
		return retval

def run_with_passthru(cmd, cwd=None):
	# what is the command we are actually going to run?
	cmd_to_run = _command_to_string(cmd)

	with dsf.core.fs.pushd(cwd):
		# make sure there is a record of what we are doing
		dsf.dslog.log_command_start(cmd_to_run)

		# run the command
		retval = subprocess.call(cmd_to_run)

		# make sure there's a record of the command's exit code
		dsf.dslog.log_command_result(retval)

		# let the caller raise the exception - it makes things much
		# easier to understand when looking at the logs
		return retval

def _command_to_string(cmd):
	# as Python's subprocess module is utterly fucked when using shell=True,
	# we have to emulate the correct behaviour ourselves

	cmd_string=""
	for param in cmd:
		if len(cmd_string) > 0:
			cmd_string = cmd_string + " "
		cmd_string = cmd_string + param

	retval=["/bin/bash", "-c", cmd_string]
	return retval
