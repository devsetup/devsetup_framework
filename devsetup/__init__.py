# standard library includes
import os

# our list of modules
from Log import Log
from Step import Step
from UsingConsole import UsingConsole
from UsingFs import UsingFs
from UsingGit import UsingGit
from UsingGithubSsh import UsingGithubSsh
from UsingHttp import UsingHttp
from UsingLog import UsingLog
from UsingShell import UsingShell

def init(parent_file):
	Log.init(os.path.dirname(parent_file))

def step(msg):
	return Step(msg)