import glob
import pkgutil
import imp
import os

# Base class for plugins. Meant to provide a hint of
# functionalities/capabilities of each plugin.
class PluginBase:
	def __init__(self):
		return
	def generate_data(self):
		return
	def search(self):
		return
	def name(slef):
		return "base"

class PluginControl:
	def __init__(self):
		# all plugins will be kept here
		# XXX: should this be an array?
		self._plugin_list = {}
		
	def register(self, plugin):
		self._plugin_list[plugin.name()] = plugin
		print "%s plugin registered."%(plugin.name())
			
	def unregister(self, name):
		if name in self._plugin_list:
			removed = self._plugin_list.pop(name)
			print "%s plugin unregistered."%(name)
		else:
			print "%s is not a plugin"%(name)
	
	def __getitem__(self, key):
		return self._plugin_list[key]

	def __iter__(self):
		for p in self._plugin_list:
			yield p
		return

_plugins = PluginControl()

def register(plugin):
	_plugins.register(plugin)

def unregister(name):
	_plugins.unregister(name)

def load_plugins():
	# TODO: don't hardcode this file's name
	for p in filter(lambda f: f != "plugin.py", glob.glob('*.py', )):
		__import__(p.split('.')[0])

if __name__ == "__main__":
	print "test"
	load_plugins()
