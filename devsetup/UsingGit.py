# -*- coding:utf8 -*-

import os
import re
import devsetup

class UsingGit:
	def __init__(self, step, repodir):
		self.step = step
		self.repodir = repodir

	def change_branch(self, branch):
		# checkout the branch
		devsetup.UsingShell(self.step).run(['git', 'checkout', branch], cwd=self.repodir)

	def get_current_branch(self):
		output = devsetup.UsingShell(self.step).get_output_from_command(['git', 'branch'], cwd=self.repodir)

		for line in output:
			if line[0:2] == '* ':
				branch = line[2:].rstrip()
				return branch

		# if we get here, we are not on a current branch
		return "* HEADLESS"

	def is_repository(self):
		# quickest test - is there a .git folder?
		dotgit_folder = os.path.join(self.repodir, '.git')
		if not os.path.isdir(dotgit_folder):
			return False

		# is the folder a real git repo?
		output = devsetup.UsingShell(self.step).get_output_from_command(['git', 'status'], cwd=self.repodir)

		regex=re.compile("fatal: Not a git repository")
		if any(regex.match(line) for line in output):
			return False

		# what about when self.repodir is a subfolder of a git repo?
		output = devsetup.UsingShell(self.step).get_output_from_command(['git', 'rev-parse', '--show-toplevel'], cwd=self.repodir)
		if output[0].rstrip() != devsetup.UsingFs(self.step).get_realpath(self.repodir):
			return False

		# if we get here, then it is a git repo
		return True