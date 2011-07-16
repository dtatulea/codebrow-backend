import ctags

import plugin

class Ctags(plugin.PluginBase):
	def __init__(self):
		#projects.get()
		return

	def search(self, tag):
		print "search: " + tag

	def name(self):
		return "ctags"

plugin.register(Ctags())
