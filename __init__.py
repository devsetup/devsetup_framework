# standard library includes
import os

from core import log
from Step import Step

def init(parent_file, write_to_log=True):
	log.init(os.path.dirname(parent_file), write_to_log)

def step(msg):
	return Step(msg)