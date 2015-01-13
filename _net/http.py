import os
import time
import urllib

import dsf

def download_file(url, target_file, cwd=None, cache=360):
	with dsf.core.fs.pushd(cwd):
		# is the file too new to download?
		if os.path.isfile(target_file):
			details = os.stat(target_file)
			if details.st_mtime > time.time() - cache:
				return

		# download the file
		dsf.dslog.log_command_start(["HTTP", "GET", url, "->", target_file])
		client=urllib.URLopener()
		client.retrieve(url, target_file)
		dsf.dslog.log_command_result(0)