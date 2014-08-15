# welcome to dev_setup

from __future__ import print_function
from devsetup.vendor import terminal
import sys

def start_new_line():
	# are we already at the start of a new line?
	pos = terminal.cursor.pos()[1]
	if pos != 1:
		# no - so start a new line
		print()

	# all done

def print_blank_line():
	start_new_line()
	print()

def print_bullet():
	sys.stdout.write(terminal.colorize("* ", "yellow", "reset", "bright"))

def print_message(msg):
	# TODO - make this word-wrap so that longer strings don't make a
	# mess of the console
	sys.stdout.write(msg)

def print_trail():
	# how wide is the console?
	width = terminal.screen.cols()

	# how far across are we currently?
	pos = terminal.cursor.pos()[1]

	# now we know how long a trail to print
	trail_length = width - pos - 8
	sys.stdout.write(' ' + '.' * trail_length + ' ')
	sys.stdout.flush()

def print_fail():
	print_result('fail', 'red', 'bright')

def print_okay():
	print_result('okay', 'green', 'bright')

def print_skip():
	print_result('skip', 'yellow', 'bright')

def print_result(result, color, lum='normal'):
	sys.stdout.write('[')
	sys.stdout.write(terminal.colorize(result, color, lum=lum))
	sys.stdout.write("]\n")
	sys.stdout.flush()

def print_see_logfile():
	sys.stdout.write("See ")
	sys.stdout.write(terminal.colorize("devsetup.log", "red", lum="bright"))
	sys.stdout.write(" for details of what went wrong.\n")
	sys.stdout.flush()