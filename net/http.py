import urllib
import dsf

def download_file(url, target_file, cwd=None):
	with dsf.core.fs.pushd(cwd):
		# download the file
		dsf.dslog.log_command_start(["HTTP", "GET", url, "->", target_file])
		client=urllib.URLopener()
		client.retrieve(url, target_file)
		dsf.dslog.log_command_result(0)