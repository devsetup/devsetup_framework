# welcome to dev_setup

from __future__ import print_function
from vendor import terminal
import sys

class UsingConsole:
	def __init__(self, step):
		self.step = step

	def start_new_line(self):
		# are we already at the start of a new line?
		pos = terminal.cursor.pos()[1]
		if pos != 1:
			# no - so start a new line
			print()

		# all done

	def print_bullet(self):
		sys.stdout.write(terminal.colorize("* ", "yellow", "reset", "bright"))

	def print_message(self, msg):
		# TODO - make this word-wrap so that longer strings don't make a
		# mess of the console
		sys.stdout.write(msg)

	def print_trail(self):
		# how wide is the console?
		width = terminal.screen.cols()

		# how far across are we currently?
		pos = terminal.cursor.pos()[1]

		# now we know how long a trail to print
		trail_length = width - pos - 8
		sys.stdout.write(' ' + '.' * trail_length + ' ')
		sys.stdout.flush()

	def print_fail(self):
		self.print_result('fail', 'red', 'bright')

	def print_okay(self):
		self.print_result('okay', 'green', 'bright')

	def print_skip(self):
		self.print_result('skip', 'yellow', 'bright')

	def print_result(self,result, color, lum='normal'):
		sys.stdout.write('[')
		sys.stdout.write(terminal.colorize(result, color, lum=lum))
		print(']')