# -*- coding:utf8 -*-

import os
import devsetup

class UsingGithubSsh:
	def __init__(self, step):
		self.step = step

	def clone(self, user, repo, target_name=None, cwd=None, branch='master'):
		# make sure we know where we are cloning to
		if cwd is None:
			cwd = os.getcwd()

		if target_name is None:
			target_name=repo

		# this is where we are cloning to
		target_dir = os.path.join(cwd, target_name)

		# make sure that the target_dir exists
		devsetup.UsingFs(self.step).ensure_folder_exists(cwd)

		# do we already have a Storyplayer repo in there?
		if not devsetup.UsingGit(self.step, target_dir).is_repository():
			# build the command that we are running
			cmd = ['git', 'clone', '-b', branch ]
			cmd = cmd + ['git@github.com:' + user + '/' + repo + '.git', target_name]

			# run the command
			devsetup.UsingShell(self.step).run(cmd, cwd=cwd)

		# are we on the right branch?
		if devsetup.UsingGit(self.step, target_dir).get_current_branch() != branch:
			devsetup.UsingGit(self.step, target_dir).change_branch(branch)