# -*- coding:utf8 -*-

from devsetup import devsetup
import os
import re

# a list of the modules we use
devsetup.uses('fromFs')
devsetup.uses('usingFs')
devsetup.uses('usingLog')
devsetup.uses('fromShell')

class fromGit:
	def __init__(self, step, repodir):
		self.step = step
		self.repodir = repodir

	def isRepository(self):
		# quickest test - is there a .git folder?
		dotgit_folder = os.path.join(self.repodir, '.git')
		if not os.path.isdir(dotgit_folder):
			return False

		# is the folder a real git repo?
		popDir = devsetup.usingFs(self.step).pushd(self.repodir)
		output = devsetup.fromShell(self.step).getOutputFromCommand(['git', 'status'])
		devsetup.usingFs(self.step).popd(popDir)

		regex=re.compile("fatal: Not a git repository")
		if any(regex.match(line) for line in output):
			return False

		# what about when self.repodir is a subfolder of a git repo?
		popDir = devsetup.usingFs(self.step).pushd(self.repodir)
		output = devsetup.fromShell(self.step).getOutputFromCommand(['git', 'rev-parse', '--show-toplevel'])
		devsetup.usingFs(self.step).popd(popDir)
		if output[0].rstrip() != devsetup.fromFs(self.step).getRealpath(self.repodir):
			return False

		# if we get here, then it is a git repo
		return True