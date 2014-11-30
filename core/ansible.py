# -*- coding:utf8 -*-

'''
dsf core module for working with Ansible

@author: Stuart Herbert <stuart@stuartherbert.com>

https://devsetup.systems/dsf-framework/
'''

import os
import tempfile
import dsf

def create_inventory(groups={}):
	"""
	Creates an Ansible inventory for you to add machines to, and then to
	run Ansible against.

	We create a temporary inventory file on disk, which is eventually
	passed to the ansible-playbook command using the -i switch.  The
	temporary inventory file guarantees that, when you run your playbook,
	only the hosts that you define in your inventory are acted upon.
	Ensures that you never accidentally run Ansible against any of the
	hosts in your real inventory when using this module :)

	Here's an example of how to use it:

	with dsf.core.create_inventory() as inv:
		inv.add_host_to_group("www-wordpress", "www.stuartherbert.com")
		dsf.core.ansible.run_playbook(inv, ...)
	"""
	return Ansible_Inventory(groups)

def run_playbook(inv, private_key=None, user=None, cwd=None, playbook="site.yml"):
	"""
	Runs the 'ansible-playbook' command against the inventory that you
	defined when you called dsf.core.ansible.create_inventory().

	Params:

	* private_key: path to the SSH key to use to log into hosts defined
	  in the inventory

	* user: the name of the user to use when SSH'ing into hosts

	* cwd: the path to your top-level Ansible playbook. This is normally
	  the folder containing your 'site.yml' file.

	* playbook: the playbook to run Ansible against. This is normally
	  your 'site.yml' file, but it can be a different <play.yml> file if
	  you prefer for whatever reason.
	"""
	# make sure the inventory exists on disk
	inv.persist()

	# build up our command to run
	cmd = ["ansible-playbook", "-i", inv.folder]
	if private_key:
		cmd = cmd + [ "--private-key", private_key ]
	if user:
		cmd = cmd + [ "--user", user ]
	cmd = cmd + [ playbook ]

	retval = dsf.shell.run(cmd, cwd=cwd)
	if retval != 0:
		raise RuntimeError("Ansible provisioning failed")

class Ansible_Inventory:
	def __init__(self, groups = {}):
		self.groups = {}
		self.folder = None

	def __enter__(self):
		return self

	def __exit__(self, type, value, traceback):
		self.cleanup()

	def persist(self):
		"""
		Creates a temporary Ansible inventory file on disk
		"""
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
		"""
		Currently does nothing.
		"""
		# TODO - remove the inventory that we wrote to disk
		pass

	def add_host_to_group(self, group, host, params={}):
		"""
		Adds a host to a group in the temporary Ansible inventory that
		we are building up.

		* group: the name of the group to add the host to. This is the
		  text that goes inside [ and ] in an Ansible inventory file.

		* host: the hostname / IP address of the host to add to the
		  group.

		* params: a list of any Ansible variables that you want to set
		  for this host.
		"""
		if not group in self.groups:
			self.groups[group] = {}
		self.groups[group][host] = params