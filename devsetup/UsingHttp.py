import urllib
import devsetup

class UsingHttp:
	def __init__(self, step):
		self.step = step

	def get(self, url):
		return

	def download_file(self, url, target_file, cwd=None):
		# are we switching folder?
		if cwd:
			popDir = devsetup.UsingFs(self.step).pushd(cwd)

		# download the file
		self.step.log_command_start(["HTTP", "GET", url, "->", target_file])
		client=urllib.URLopener()
		client.retrieve(url, target_file)
		self.step.log_command_result(0)

		# are we switching back?
		if cwd:
			devsetup.UsingFs(self.step).popd(popDir)