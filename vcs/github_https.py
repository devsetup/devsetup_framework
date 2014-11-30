# -*- coding:utf8 -*-

import os
import dsf

def clone(user, repo, target_name=None, cwd=None, branch='master'):
	# make sure we know where we are cloning to
	if cwd is None:
		cwd = os.getcwd()

	if target_name is None:
		target_name=repo

	# this is where we are cloning to
	target_dir = os.path.join(cwd, target_name)

	# make sure that the target_dir exists
	dsf.core.fs.ensure_folder_exists(cwd)

	# do we already have a Storyplayer repo in there?
	if not dsf.core.git.is_repository(cwd=target_dir):
		# build the command that we are running
		cmd = ['git', 'clone', 'https://github.com/' + user + '/' + repo + '.git', target_name]

		# run the command
		retval = dsf.core.shell.run(cmd, cwd=cwd)

		# what happened?
		if retval != 0:
			raise RuntimeError("git clone failed")

	# are we on the right branch?
	if dsf.core.git.get_current_branch(cwd=target_dir) != branch:
		dsf.core.git.change_branch(branch, cwd=target_dir)