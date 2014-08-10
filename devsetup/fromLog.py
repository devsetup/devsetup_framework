# -*- coding:utf8 -*-

class fromLog:
	def __init__(self, step):
		self.step = step

	def convert_command_to_string(self, cmd):
		retval=''
		for arg in cmd:
			# are we appending to the return value?
			if len(retval) > 0:
				retval=retval+' '

			# does the arg need quoting?
			if ' ' in arg:
				if "'" in arg:
					retval=retval+"'" + arg + "'"
				else:
					retval=retval+'"' + arg + '"'
			else:
				retval=retval+arg

		# all done
		return retval

