import re
import dsf

def start(cwd=None, destroy_first=False, vms = ['default']):
	with dsf.core.fs.pushd(cwd):
		# do we have a vagrant file?
		if not dsf.core.fs.has_file('Vagrantfile'):
			raise RuntimeError("no Vagrantfile found")

		# start vagrant
		dsf.core.shell.run(["vagrant", "up"] + vms)

def stop(cwd=None, vms = ['default']):
	with dsf.core.fs.pushd(cwd):
		# do we have a vagrant file?
		if not dsf.core.fs.has_file('Vagrantfile'):
			raise RuntimeError("no Vagrantfile found")

		# start vagrant
		dsf.core.shell.run(["vagrant", "down"] + vms)

def get_ipv4_address(cwd=None, machine="default"):
	with dsf.core.fs.pushd(cwd):
		# do we have a vagrant file?
		if not dsf.core.fs.has_file('Vagrantfile'):
			raise RuntimeError("no Vagrantfile found")

		# get a list of interfaces
		output = dsf.core.shell.get_output_from_command(["vagrant", "ssh", "-c", "/sbin/ifconfig eth1", machine])
		regex  = re.compile(r'([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})')
		for line in output:
			matches = regex.search(line)
			if matches is not None:
				return matches.group(1)

		# if we get here, no IP address found
		raise RuntimeError("unable to determine IP address")