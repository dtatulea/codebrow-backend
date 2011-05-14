
# TODO:
# - read path:
#	* if file return contents
#	* if dir return list

import os
import sys
import json

# locals
import projects

class listing:
	def __init__(self, project, path, abs_path=None):
		if abs_path == None:
	 		self.abs_path = project["src_path"] + path
		else:
			self.abs_path = abs_path

		self.project_name = project["name"]
		self.path = path

	def data(self):
		return {
			"project" : self.project_name,
			"rootdirectories" : self.path
			}

class directories(listing):

	def __init__(self, project, path, abs_path=None):
		listing.__init__(self, project, path, abs_path)

		self.dirs = []
		self.files = []
		self.others = []

		for p in os.listdir(self.abs_path):
			abs_p = self.abs_path + "/" + p

			if os.path.isdir(abs_p):
				self.dirs.append(p)
			elif os.path.isfile(abs_p):
				self.files.append(p)
			else:
				self.others.append(p)

	def data(self):
		ret = {
			"type" : "dirlisting",
			"data" : {
				"dirs" : self.dirs,
				"files" : self.files,
				"others" : self.others
				}
			}

		ret.update(listing.data(self))
		return ret

class file_dump(listing):

	def __init__(self, project, path, abs_path=None):
		listing.__init__(self, project, path, abs_path)

	def data(self):
		ret = {
			"type" : "file_dump",
			"data" : {
				"content" : open(self.abs_path, "r").read()
				}
			}
		ret.update(listing.data(self))

		return ret

def dispatch(project_name, path):
		try:
			project = projects.prj_list[project_name]
		except KeyError:
			print "No such project: " + project_name
			return

	 	abs_path = project["src_path"] + path
		if not os.path.exists(abs_path):
			print "No such path: " + abs_path
			return
		

		if os.path.isdir(abs_path):
			return directories(project, path, abs_path)
		elif os.path.isfile(abs_path):
			return file_dump(project, path, abs_path)
		else:
			return None


class handle:

	def GET(self, project_name, path="/"):
		ret = dispatch(project_name, path)
		if ret:
			return json.dumps(ret.data())
		else:
			return None

if __name__ == "__main__":

	print json.dumps(dispatch("linux-kernel", "/").data())
	print "-------------------------------------------------"
	print json.dumps(dispatch("linux-kernel", "Kconfig").data())
	print "-------------------------------------------------"
	print json.dumps(dispatch("linux-kernel", "drivers/net/atp.c").data())
	print "-------------------------------------------------"
	print json.dumps(dispatch("linux-kernel", "drivers/net/x.c").data())

	#print _file("linux-kernel", "README").json()
