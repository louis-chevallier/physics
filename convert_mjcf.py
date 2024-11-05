import json, yaml
from utillc import *


class T :
	def __init__(self,
				 name = "name",
				 params = [],
				 children = []) :
		self.name = name
		self.params = params
		self.children = children
		pass

	
	def dump(self, t="") :

		rr = ""
		for nn,vv in self.params :
			rr += nn + "=" + '"' + vv + '"'; 
		r = t + "<" + self.name  + " " + rr + ">\n" ;
		for e in self.children :
			r += e.dump(t + "\t")
		r += "</" + self.name + ">"
		return r
	
class Mujoco :
	def __init__(self) :
		pass
	def dump(self) :
		tt = T(name="mujoco",
			   params = [ ("model", "example") ])
		return tt.dump()
	def yaml(self) :
		with open('data.yaml', 'r') as file:
			data = yaml.safe_load(file)
			EKOX(data)
			EKOX(json.dumps(data, indent = 4))
		return self
		
	

EKOX("\n" + Mujoco().dump())
EKOX("\n" + Mujoco().yaml().dump())


