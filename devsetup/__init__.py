# standard library includes
import os

from core import log
from Step import Step

def init(parent_file):
	log.init(os.path.dirname(parent_file))

def step(msg):
	return Step(msg)