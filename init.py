# standard library includes
import os

import core

def init(parent_file, write_to_log=True):
	core.log.init(os.path.dirname(parent_file), write_to_log)
