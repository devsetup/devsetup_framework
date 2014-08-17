# -*- coding:utf8 -*-

import os
import fs, git, shell

def clone(user, repo, target_name=None, cwd=None, branch='master'):
	# make sure we know where we are cloning to
	if cwd is None:
		cwd = os.getcwd()

	if target_name is None:
		target_name=repo

	# this is where we are cloning to
	target_dir = os.path.join(cwd, target_name)

	# make sure that the target_dir exists
	fs.ensure_folder_exists(cwd)

	# do we already have a Storyplayer repo in there?
	if not git.is_repository(cwd=target_dir):
		# build the command that we are running
		cmd = ['git', 'clone', '-b', branch ]
		cmd = cmd + ['git@github.com:' + user + '/' + repo + '.git', target_name]

		# run the command
		shell.run(cmd, cwd=cwd)

	# are we on the right branch?
	if git.get_current_branch(cwd=target_dir) != branch:
		git.change_branch(branch, cwd=target_dir)