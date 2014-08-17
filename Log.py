# -*- coding:utf8 -*-

import io
import os

class Log:
	# this is where all the commands we run will write to
	LOG_STDOUT=None
	LOG_STDERR=None

	@staticmethod
	def init(project_folder):
		# where will the logfile live?
		log_filename = os.path.join(project_folder, "devsetup.log")

		# create it
		logfile = io.open(log_filename, "w")

		# all done
		Log.LOG_STDOUT = logfile
		Log.LOG_STDERR = logfile