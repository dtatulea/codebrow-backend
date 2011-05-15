import os
import glob
import json

class loader:
	def __init__(self):
		self.cfg_path = "./config/" # XXX: config option
		self.prj_list = {}

		for cfg in glob.glob(self.cfg_path + "*.json"):
			p = config(cfg)
			self.prj_list[p["name"]] = p
	
	# act as an array iterator
	def __iter__(self):
		for prj in self.prj_list:
			yield self.prj_list[prj]
		return

	def __getitem__(self, key):
		return self.prj_list[key]

class config:
	cfg_json_buf = ""

	def __init__(self, cfg_file):
		# TODO: stat path, exception catch
		self.cfg_json_buf = open(cfg_file).read()
		self.cfg = json.load(open(cfg_file))
		
		# TODO: self.validate() 

	def __getitem__(self, key):
		return self.cfg[key]

	def json(self):
		return self.cfg_json_buf

prj_list = loader()

# get the project name
def get(name):
	return prj_list[name]

class handle_list:
	def GET(self):
		ret = ""
		for p in prj_list:
			ret = ret + p.json() + "\n"
			print p
		return ret

class handle:
	def GET(self, name):
		try:
			p = prj_list[name]
			return p.json()
		except KeyError:
			return None



if __name__ == "__main__":
	d = loader()
	for p in d:
		print p.json()

	print d["linux-kernel"].json()
