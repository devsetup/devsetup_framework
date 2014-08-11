# -*- coding:utf8 -*-

import os

class UsingInternal:
	def determine_project_folder(self,script_filename):
		project_folder = os.path.dirname(os.path.abspath(script_filename))
		return project_folder
