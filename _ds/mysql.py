# -*- coding:utf8 -*-

'''
dsf module for working with a MySQL server

@author: Stuart Herbert <stuart@stuartherbert.com>

https://devsetup.systems/dsf-framework/
'''

import os

import dsf

class MySQLServer(object):
	def __init__(self, host=None, port=None, user="root", password=None):
		self.host = host
		self.port = port
		self.user = user
		self.password = password

		# time-saving helper: mysql command
		cmd=["mysql"]
		if self.host is not None:
			cmd.append("-h")
			cmd.append(self.host)
		if self.port is not None:
			cmd.append("--port")
			cmd.append(str(self.port))
		cmd.append("-u")
		cmd.append(self.user)
		if self.password is not None:
			cmd.append("-p")
			cmd.append(self.password)
		self.mysql_command = cmd

		# time-saving helper: mysqladmin command
		cmd=["mysqladmin"]
		if self.host is not None:
			cmd.append("-h")
			cmd.append(self.host)
		if self.port is not None:
			cmd.append("--port")
			cmd.append(str(self.port))
		cmd.append("-u")
		cmd.append(self.user)
		if self.password is not None:
			cmd.append("-p")
			cmd.append(self.password)
		self.mysqladmin_command = cmd

	def __enter__(self):
		return self

	def __exit__(self, type, value, traceback):
		if type is None:
			pass

def server(host=None, port=None, user="root", password=None):
	return MySQLServer(host, port, user, password)

def create_database(server, db_name):
	# do not try to create something that's already there
	if database_exists(server, db_name):
		return

	# if we get here, we need to create the database
	cmd = server.mysqladmin_command
	cmd.append("create")
	cmd.append(db_name)

	if dsf.shell.run(cmd) is not 0:
		raise RuntimeError

def database_exists(server, db_name):
	cmd = server.mysql_command
	cmd.append("-e")
	cmd.append("use %s" % db_name)
	retval = dsf.shell.run(cmd)
	if retval is 0:
		return True
	if retval is 1:
		return False

	raise RuntimeError("unexpected response from mysql command")


def run_sql_from_file(server, database, source_file):
	"""
	Executes SQL stored in a file on disk.

	A handy wrapper for calling the 'mysql' command.

	Params:

	* server: the MySQLServer class returned from dsf.mysql.server()

	* database: the database to run the source_file against

	* source_file: the file containing the SQL to run

	Raises RuntimeError when:

	a) 'source_file' does not exist
	b) 'source_file' does not execute successfully
	"""
	if not os.path.isfile(source_file):
		raise RuntimeError

	# build the command to execute
	cmd=server.mysql_command
	cmd.append(database)
	cmd.append("<")
	cmd.append(source_file)

	if dsf.shell.run(cmd) is not 0:
		raise RuntimeError

def chmod(target_file, mode):
	"""
	Sets the UNIX permissions on a file or a folder.

	Mimics the chmod(1) command available in your UNIX shell.  Very
	handy for making files executable after you've downloaded them, for
	example.

	Params:

	* target_file: the path of the file/folder to chmod

	* mode: an octal number

	Raises RuntimeError when:

	a) 'target_file' does not exist
	b) you don't have permission to chmod 'target_file'

	TODO:

	* Accept 'rwxs'-type text version of the 'mode' param.

	  This would help users who aren't comfortable with the UNIX octal
	  mode values. Would probably make their code a little more readable
	  too.
	"""
	# does the target_file actually exist?
	dsf.dslog.log_command_start(['chmod', oct(mode), target_file])
	if not os.path.exists(target_file):
		dsf.dslog.log_command_output(["no such file"])
		dsf.dslog.log_command_result(1)
		raise RuntimeError

	os.chmod(target_file, mode)
	dsf.dslog.log_command_result(0)
