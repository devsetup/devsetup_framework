# -*- coding:utf8 -*-

import os
from devsetup import devsetup

# a list of the modules we need
devsetup.uses("usingLog")

class fromFs:
	def __init__(self, step):
		self.step = step

	def getRealpath(self, target_dir):
		return os.path.realpath(target_dir)