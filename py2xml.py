
from utillc import *


def xml(x, tab="") :
	if type(x) is tuple :
		return tab + str(x)
	else:
		return x.xml(tab)

def ddd(x) :

	if x is None :
			return "None"
	if type(x) is str :
			return x
	if type(x) is int :
			return str(x)
	if type(x) is bool  :
			return str(x)
	if type(x) is dict :
			return " ".join([ k + ddd(v) for k,v in x])
	if type(x) is float :
			return str(x)
	if type(x) is tuple :
			return ', '.join(map(ddd, x))
	if type(x) is list :
			return ', '.join(map(ddd, x))
	if x.__class__.__name__ :
			r = x.sname()
			return r
	return str(x)

class X :
	def __init__(self, a=[]) :
			self.a = a
			self.p = {}
			pass
	def sname(self) : return self.__class__.__name__

	def params(self) :
			r = [ (k,v) for (k,v) in self.__dict__.items() if k not in ['p', 'a'] and v is not  None]
			#return self.__dict__
			return r
	def params_string(self) :
			r = ""

			def proc(x) :
					x = x[1:] if x[0] == '_' else x
					x = x.lower() if x in ["True", "False"] else x
					return x
			def dd(ss) :
					ss = ' '.join(map(str, ss))  if type(ss) == tuple else ss
					return '"' + proc(str(ss)) + '"'
			def rr(kv) :
					k, v = kv
					return proc(k) + "=" + dd(v)
			return ' '.join(map(rr, self.params()))

	def xml(self, tab="") :
		if len(self.a) > 0 :
				r = (tab + "<" + self.sname().lower() + " " + self.params_string() + ">\n" +
					 "\n".join([ xml(e, tab + "  ") for e in self.a]) +
					 "\n" + tab + "</" + self.sname().lower() + ">")
		else :
				r = (tab + "<" + self.sname().lower() + " " + self.params_string() + "/>")
				
		return r

class Mujoco(X) :
	def __init__(self, model=None) :
			super().__init__()
			self.model = model			
			pass
	def __call__(self, *a) :
			self.a = a
			return self


	
class Default(X) :
	def __init__(self, *a) :
			super().__init__(a)
			self.a = a
			pass
	def __repr__(self) :
			return ("Default", str(self.a))

	
class Geom(X) :
	def __init__(self,
				 rgba=None,
				 _type=None,
				 size=None,
				 fromto=None) :
			super().__init__()
			self.rgba=rgba
			self._type=_type
			self.size=size
			self.fromto=fromto

			pass

class Asset(X) :
	def __init__(self, *a) :
			super().__init__(a)	
			pass

class Worldbody(X) :
	def __init__(self, *a) :
			super().__init__(a)	
			pass	

class Light(X) :
	def __init__(self,
				 pos=None,
				 dir=None,
				 diffuse=None) :
			super().__init__()
			self.pos=pos
			self.dir=dir
			self.diffuse=diffuse
			pass


class Body(X) :
	def __init__(self,
				 pos=None) :		
			super().__init__()
			self.pos = pos
			pass	
	def __call__(self, *a) :
			self.a = a
			return self

class Joint(X) :
	def __init__(self,
				 _type=None,
				 axis=None) :
			super().__init__()
			self._type=_type
			self.axis=axis
			pass	

class Material(X) :
	def __init__(self,
				 groundplane =None,
				 texture =None,
				 texuniform =None,
				 texrepeat =None,
				 reflectance =None,
				 rgb1 =None,
				 rgb2 =None,
				 width=None,
				 height=None,
				 name=None) :
			super().__init__()
			#self._type=_type,
			self.groundplane =groundplane
			self.texture =texture
			self.texuniform=texuniform
			self.texrepeat =texrepeat
			self.reflectance =reflectance 
			self.rgb1 =rgb1 
			self.rgb2 =rgb2 
			self.width=width
			self.height=height
			self.name=name

def  rgba(*x) : return x

def geom(rgba) :
	return rgba

def pos(*c) :
	return c

def model(*c) :
	return { 'rgba' : rgba}

def light(_type=None,
		  pos=None,
		  builtin =None) :
	return { 'type' : _type,
			 'pos' : pos,
			 'builtin' : builtin
			}

class Texture(X) :
	def __init__(self,
				 _type=None,
				 builtin =None,
				 rgb1 =None,
				 rgb2 =None,
				 width=None,
				 height=None,
				 mark=None,
				 markrgb=None,
				 name=None) :
			super().__init__()
			self._type = _type
			self.builtin = builtin;
			self.rgb1 =  rgb1
			self.rgb2 =  rgb2
			self.width =  width
			self.height = height
			self.name=name
			self.mark=mark
			self.markrgb=markrgb
	def __str__(self) :
		return self.t
	def __repr__(self) :
		return str(("Texture", str(self.t)))

		
ball="ball"
sphere="sphere"
capsule="capsule"
ellipsoid="ellipsoid"
box="box"
cylinder="cylinder"
skybox="skybox"
groundplane="groundplane"
gradient="gradient"
grid="grid"
checker="checker"
_2d="_2d"
_type="_type"
skybox="skybox"
builtin="builtin"
edge = "edge"



if __name__ == '__main__':
		example = Mujoco(model="example")(
				Default(
						Geom(rgba=rgba(.8, .6, .4, 1))),
				Asset(
						Texture(_type=skybox,
								builtin=gradient,
								rgb1=(.3, .5, .7),
								width=32,
								height=512),
						Texture(name=grid,
								_type=_2d_,
								builtin=checker,
								width=512,
								height=512,
								rgb2=(.2, .3, .4),
								rgb1=(.1, .2, .3)),
						Material(name=grid,
								 texture=grid,
								 texuniform=True,
								 texrepeat=(1,1),
								 reflectance=0.2),
						Texture(name=groundplane,
								_type=_2d_,
								builtin=checker,
								mark=edge,
								width=300,
								height=300,
								rgb1=(.2, .3, .4),
								rgb2=(.1, .2, .3),
								markrgb=(0.8, 0.8, 0.8)),
						Material(name=groundplane,
								 texture=groundplane,
								 texuniform=True,
								 texrepeat=(5,5),
								 reflectance=0.2))
				
				
		,
				Worldbody(
						Light(pos=(0,1,1), dir=(0,-1, -1), diffuse=(1,1,1)),
						Body(pos(0,0,1))(
								Joint(_type=ball),
								Geom(_type=box, size=0.06, fromto=(0,0,0, 0,0,-0.4))),
						Body(pos=pos(0,0,-0.4))(
								Joint(axis=(0,1,0)),
								Joint(axis=(1,0,0)),
								Geom(_type=box, size=0.06, fromto=(0,0,0, -0.3,0,0)))))
		
		EKO()
		e1 = example
		EKOX("\n" + e1.xml())


