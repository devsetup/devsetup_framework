# -*- coding:utf8 -*-

'''
dsf core module for working with the user's screen

@author: Stuart Herbert <stuart@stuartherbert.com>

https://devsetup.systems/dsf-framework/
'''

from __future__ import print_function
import dsf
import sys

def start_new_line():
	"""
	Move the cursor to the beginning of the next line - only if we
	aren't already there!
	"""
	# are we already at the start of a new line?
	pos = dsf.core.terminal.cursor.pos()[1]
	if pos != 1:
		# no - so start a new line
		print()

	# all done

def print_blank_line():
	"""
	Print a single blank line.
	"""
	start_new_line()
	print()

def print_bullet():
	"""
	Print a bullet point.
	"""
	sys.stdout.write(dsf.core.terminal.colorize("* ", "yellow", "reset", "bright"))

def print_message(msg):
	"""
	Print a string to the screen.

	Currently doesn't support word-wrap at all. One day it will.
	"""
	# TODO - make this word-wrap so that longer strings don't make a
	# mess of the console
	sys.stdout.write(msg)

def print_trail():
	"""
	Print a trail of dots across to the right-hand side of the current
	line.

	Puts the cursor in the right position for calling print_fail() et al.
	"""
	# how wide is the console?
	width = dsf.core.terminal.screen.cols()

	# how far across are we currently?
	pos = dsf.core.terminal.cursor.pos()[1]

	# now we know how long a trail to print
	trail_length = width - pos - 8
	sys.stdout.write(' ' + '.' * trail_length + ' ')
	sys.stdout.flush()

def print_fail():
	"""
	Print '[fail]' on the screen.
	"""
	print_result('fail', 'red', 'bright')

def print_okay():
	"""
	Print '[okay]' on the screen.
	"""
	print_result('okay', 'green', 'bright')

def print_skip():
	"""
	Print '[skip]' on the screen.
	"""
	print_result('skip', 'yellow', 'bright')

def print_result(result, color, lum='normal'):
	"""
	Helper method called by print_fail() et al to do the actual printing.
	"""
	sys.stdout.write('[')
	sys.stdout.write(dsf.core.terminal.colorize(result, color, lum=lum))
	sys.stdout.write("]\n")
	sys.stdout.flush()

def print_see_logfile():
	"""
	Prints a helpful message about the devsetup.log file.
	"""
	sys.stdout.write("See ")
	sys.stdout.write(dsf.core.terminal.colorize("devsetup.log", "red", lum="bright"))
	sys.stdout.write(" for details of what went wrong.\n")
	sys.stdout.flush()