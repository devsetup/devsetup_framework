# -*- coding:utf8 -*-

import io
import os

class initLog:
	def init(self,project_folder):
		# where will the logfile live?
		log_filename = os.path.join(project_folder, "devsetup.log")

		# create it
		logfile = io.open(log_filename, "w")

		# all done
		return [logfile, logfile]