# welcome to devsetup

import sys
from pprint import pprint

# import all the things (sigh)
# surely there has to be a better to do this?
#from devsetup.cli import usingCli
#from devsetup.console import usingConsole
#from devsetup.fs import usingFs
#from devsetup.git import fromGit
#from devsetup.github_ssh import usingGithubSsh
#from devsetup.internal import fromInternal, usingInternal
#from devsetup.log import log, fromLog, usingLog
#from devsetup.shell import fromShell, usingShell
#from devsetup.step import step

class devsetup:
	# this is where all the commands we run will write to
	LOG_STDOUT=None
	LOG_STDERR=None

	# keep track of the project folder
	DEVSETUP_PROJECT_FOLDER=None

	# you must call this from your devsetup.py script to bootstrap everything
	@staticmethod
	def init(script_filename):
		#global DEVSETUP_PROJECT_FOLDER
		#global LOG_STDOUT, LOG_STDERR

		devsetup.uses('usingInternal')
		devsetup.uses('initLog')
		devsetup.uses('usingLog')
		devsetup.uses('usingStep')

		# work out where our project folder is
		devsetup.DEVSETUP_PROJECT_FOLDER = devsetup.usingInternal().determineProjectFolder(script_filename)

		# create the log file
		[devsetup.LOG_STDOUT, devsetup.LOG_STDERR] = devsetup.initLog().init(devsetup.DEVSETUP_PROJECT_FOLDER)

	@staticmethod
	def uses(class_name):
		# do we already have this module loaded?
		try:
			getattr(devsetup, class_name)
		except AttributeError:
			try:
				module=__import__("devsetup.%s" % class_name, fromlist=[ class_name ])
				imported_class=getattr(module, class_name)
				setattr(devsetup, class_name, imported_class)
			except ImportError:
				print("unable to import module devsetup.%s" % class_name)

	@staticmethod
	def startStep(msg):
		step = devsetup.usingStep(msg)
		return step