# -*- coding:utf8 -*-

import subprocess

import fs, log

def get_output_from_command(cmd, cwd=None):
	# are we changing folders first?
	if cwd:
		popd = fs.pushd(cwd)

	# make sure there is a record of what we are doing
	log.log_command_start(cmd)

	# run the command
	p1 = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	# get the output
	output = p1.communicate()

	# put a copy of the output in the log file
	log.log_command_output(output)
	log.log_command_result(p1.returncode)

	# did we run this in a different folder?
	if cwd:
		fs.popd(popd)

	# all done
	return output

def run(cmd, cwd=None):
	# are we changing folders first?
	if cwd:
		popd = fs.pushd(cwd)

	# make sure there is a record of what we are doing
	log.log_command_start(cmd)

	# run the command
	retval = subprocess.call(cmd, stdout=log.LOG_STDOUT, stderr=log.LOG_STDERR)

	# make sure there's a record of the command's exit code
	log.log_command_result(retval)

	# now what do we do?
	if retval == 0:
		# the command succeeded
		if cwd:
			fs.popd(popd)
		return

	# if we get here, then the command failed :(
	raise RuntimeError