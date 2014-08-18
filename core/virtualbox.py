import re
import os
import dsf

def find_bridge_adapter():
	# ask virtualbox for a list of bridgeable adapters
	output = dsf.core.shell.get_output_from_command(["VBoxManage",  "list", "bridgedifs"])

	# we're going to need some help to understand the output
	iface_regex = re.compile(r'Name:[\s]+(.*)')
	ip_regex = re.compile(r'IPAddress:[\s]+(.*)')

	# the interface we are looking at
	iface  = None

	# let's find the first interface with an IP address
	for line in output[0].split("\n"):
		matches = iface_regex.search(line)
		if matches is not None:
			iface = matches.group(1)
		else:
			matches = ip_regex.search(line)
			if iface and matches is not None:
				if matches.group(1) != "0.0.0.0":
					return iface

	# if we get here, we could not find a bridgeable interface
	return None

def set_bridge_adapter():
	iface = find_bridge_adapter()
	if iface is None:
		raise RuntimeError("unable to find a bridge adapter to use")

	# set the bridge adapter
	os.environ["VIRTUALBOX_BRIDGE_ADAPTER"] = iface