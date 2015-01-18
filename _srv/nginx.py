# -*- coding:utf8 -*-

'''
dsf module for working with nginx

@author: Stuart Herbert <stuart@stuartherbert.com>

https://devsetup.systems/dsf-framework/
'''

import os
import dsf

def enable_site(site_name):
	# is the site already enabled?
	if is_site_enabled(site_name):
		return

	# enable the site
	available_file=_site_available_filename(site_name)
	enabled_file=_site_enabled_filename(site_name)
	os.link(available_file, enabled_file)

def is_site_enabled(site_name):
	enabled_file=_site_enabled_filename(site_name)
	if os.path.isfile(enabled_file) or os.path.islink(enabled_file):
		return True
	return False

def _site_available_filename(site_name):
	return "/etc/nginx/sites-available/%s" % site_name

def _site_enabled_filename(site_name):
	return "/etc/nginx/sites-enabled/%s" % site_name
