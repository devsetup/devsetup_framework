# standard library includes
import os

import dsf
from . import Step

def init(parent_file, write_to_log=True):
	dsf.dslog.init(os.path.dirname(parent_file), write_to_log)

def step(msg):
	return Step.Step(msg)