import urllib
import fs, log

def download_file(url, target_file, cwd=None):
	# are we switching folder?
	if cwd:
		popDir = fs.pushd(cwd)

	# download the file
	log.log_command_start(["HTTP", "GET", url, "->", target_file])
	client=urllib.URLopener()
	client.retrieve(url, target_file)
	log.log_command_result(0)

	# are we switching back?
	if cwd:
		fs.popd(popDir)