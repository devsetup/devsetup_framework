# -*- coding:utf8 -*-

import os
import re
import dsf

def change_branch(branch, cwd=None):
	# checkout the branch
	dsf.core.shell.run(['git', 'checkout', branch], cwd=cwd)

def get_current_branch(cwd=None):
	output = dsf.core.shell.get_output_from_command(['git', 'branch'], cwd=cwd)

	for line in output:
		if line[0:2] == '* ':
			branch = line[2:].rstrip()
			return branch

	# if we get here, we are not on a current branch
	return "* HEADLESS"

def is_repository(cwd=None):
	# make sure we have a current working directory
	if not cwd:
		cwd = os.getcwd()

	# quickest test - is there a .git folder?
	dotgit_folder = os.path.join(cwd, '.git')
	if not os.path.isdir(dotgit_folder):
		return False

	# is the folder a real git repo?
	output = dsf.core.shell.get_output_from_command(['git', 'status'], cwd=cwd)

	regex=re.compile("fatal: Not a git repository")
	if any(regex.match(line) for line in output):
		return False

	# what about when self.repodir is a subfolder of a git repo?
	output = dsf.core.shell.get_output_from_command(['git', 'rev-parse', '--show-toplevel'], cwd=cwd)
	if output[0].rstrip() != dsf.core.fs.get_realpath(cwd):
		return False

	# if we get here, then it is a git repo
	return True