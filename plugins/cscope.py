import glob

import plugin

class Cscope(plugin.PluginBase):

	def __init__(self):
		return

	def search(self, tag):
		print "search: " + tag

	def name(self):
		return "cscope"

plugin.register(Cscope())
