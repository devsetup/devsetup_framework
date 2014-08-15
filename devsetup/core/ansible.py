import os
import tempfile
import sys
import log, shell

def create_inventory(groups={}):
	return Ansible_Inventory(groups)

def run_playbook(inv, private_key=None, user=None, cwd=None):
	# make sure the inventory exists on disk
	inv.persist()

	# build up our command to run
	cmd = ["ansible-playbook", "-i", inv.folder]
	if private_key:
		cmd = cmd + [ "--private-key", private_key ]
	if user:
		cmd = cmd + [ "--user", user ]
	cmd = cmd + [ "site.yml" ]

	shell.run(cmd, cwd=cwd)

class Ansible_Inventory:
	def __init__(self, groups = {}):
		self.groups = {}
		self.folder = None

	def __enter__(self):
		return self

	def __exit__(self, type, value, traceback):
		self.cleanup()

	def persist(self):
		# TODO - create a folder on disk, and write the inventory out there
		self.folder = tempfile.mkdtemp()
		for group in self.groups:
			filename = os.path.join(self.folder, group)
			with open(filename, 'w') as f:
				f.write("[" + group + "]\n")
				for host in self.groups[group]:
					f.write(host)
					for param in self.groups[group][host]:
						f.write(" " + param + "=" + self.groups[group][host][param]);
					f.write("\n")

	def cleanup(self):
		# TODO - remove the inventory that we wrote to disk
		pass

	def add_group(self, group):
		self.groups[group] = {}

	def add_host_to_group(self, group, host, params={}):
		if not self.groups[group]:
			self.groups[group] = {}
		self.groups[group][host] = params