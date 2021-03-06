# welcome to devsetup

# import all the things (sigh)
class Devsetup:
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

		# work out where our project folder is
		devsetup.DEVSETUP_PROJECT_FOLDER = devsetup.UsingInternal().determine_project_folder(script_filename)

		# create the log file
		[devsetup.LOG_STDOUT, devsetup.LOG_STDERR] = devsetup.InitLog().init(devsetup.DEVSETUP_PROJECT_FOLDER)

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
	def start_step(operation):
		step = devsetup.UsingStep(operation)
		return step
