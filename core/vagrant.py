import re
import dsf

def start(cwd=None, destroy_first=False, vms = ['default']):
	with dsf.core.fs.pushd(cwd):
		# do we have a vagrant file?
		if not dsf.core.fs.has_file('Vagrantfile'):
			raise RuntimeError("no Vagrantfile found")

		# set the bridge adapter
		dsf.core.virtualbox.set_bridge_adapter()

		# start vagrant
		dsf.shell.run(["vagrant", "up"] + vms)

def stop(cwd=None, vms = ['default']):
	with dsf.core.fs.pushd(cwd):
		# do we have a vagrant file?
		if not dsf.core.fs.has_file('Vagrantfile'):
			raise RuntimeError("no Vagrantfile found")

		# start vagrant
		dsf.shell.run(["vagrant", "down"] + vms)

def destroy(cwd=None):
	with dsf.core.fs.pushd(cwd):
		if not dsf.core.fs.has_file('Vagrantfile'):
			raise RuntimeError

		# shutdown the vagrant VMs
		dsf.shell.run(["vagrant", "destroy", "--force"])

def get_ipv4_address(cwd=None, machine="default"):
	with dsf.core.fs.pushd(cwd):
		# do we have a vagrant file?
		if not dsf.core.fs.has_file('Vagrantfile'):
			raise RuntimeError("no Vagrantfile found")

		# get a list of interfaces
		output = dsf.shell.get_output_from_command(["vagrant", "ssh", "-c", "/sbin/ifconfig eth1", machine])
		regex  = re.compile(r'([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})')
		for line in output[0].split("\n"):
			matches = regex.search(line)
			if matches is not None:
				return matches.group(1)

		# if we get here, no IP address found
		raise RuntimeError("unable to determine IP address")

def run_command(cmd, cwd=None, machine="default", ignore_errors=False):
	with dsf.core.fs.pushd(cwd):
		if not dsf.core.fs.has_file('Vagrantfile'):
			raise RuntimeError

		retval = dsf.shell.run(["vagrant", "ssh", "-c", cmd, machine ])
		if retval != 0 and not ignore_errors:
			raise RuntimeError("command inside VM failed")