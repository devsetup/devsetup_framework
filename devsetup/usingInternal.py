# -*- coding:utf8 -*-

import os

class usingInternal:
	def determineProjectFolder(self,script_filename):
		project_folder = os.path.dirname(os.path.abspath(script_filename))
		return project_folder
