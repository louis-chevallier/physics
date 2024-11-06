
from utillc import *
import numpy as np
import os
import numpy as np
from collections import OrderedDict
from itertools import chain, combinations, product
import xmltodict
import trimesh
EKO()
from pyhull.convex_hull import ConvexHull
EKO()
from stl.mesh import Mesh

def xml(x, tab="") :
    if type(x) is tuple :
        return tab + str(x)
    else:
        s = x.xml(tab)
        return s


if False :

        # from https://github.com/openai/mujoco-worldgen/tree/master/mujoco_worldgen/util


        # Basic (half) unit length we normalize to
        u = 0.038  # 38 millimeters in meters


        def norm(shape):
            ''' Center a shape over the origin, and scale it to fit in unit box '''
            mins, maxs = np.min(shape, axis=0), np.max(shape, axis=0)
            return (shape - (maxs + mins) / 2) / (maxs - mins) * u * 2


        def roll3(points):
            ''' Return a set of rotated 3d points (used for construction) '''
            return np.vstack([np.roll(points, i) for i in range(3)])

        def subdivide(shape):
            ''' Take a triangulated sphere and subdivide each face. '''
            # https://medium.com/game-dev-daily/d7956b825db4 - Icosahedron section

            EKO()
            hull = ConvexHull(shape)
            radius = np.mean(np.linalg.norm(hull.points, axis=1))  # Estimate radius
            edges = set(chain(*[combinations(v, 2) for v in hull.vertices]))
            midpoints = np.mean(hull.points.take(list(edges), axis=0), axis=1)
            newpoints = midpoints / np.linalg.norm(midpoints, axis=1)[:, None] * radius
            return norm(np.vstack((hull.points, newpoints)))

        EKO()

        phi = (1 + 5 ** .5) / 2  # Golden ratio
        ihp = 1 / phi  # Inverted golden ratio (phi backwards)

        # Construct tetrahedron from unit axes and projected (ones) point
        tetra = norm(np.vstack((np.ones(3), np.eye(3))))
        # Construct cube from tetrahedron and inverted tetrahedron
        cube = np.vstack((tetra, -tetra))
        # Construct octahedron from unit axes and inverted unit axes
        octa = norm(np.vstack((np.eye(3), -np.eye(3))))
        # Construct icosahedron from (phi, 1) planes
        ico_plane = np.array(list(product([1, -1], [phi, -phi], [0])))
        icosa = norm(roll3(ico_plane))
        # Construct dodecahedron from unit cube and (phi, ihp) planes
        dod_cube = np.array(list(product(*([(-1, 1)] * 3))))
        dod_plane = np.array(list(product([ihp, -ihp], [phi, -phi], [0])))
        dodeca = norm(np.vstack((dod_cube, roll3(dod_plane))))


        # Josh's shapes (basic length 38mm)
        line = np.linspace(0, 2 * np.pi, 100)
        circle = np.c_[np.cos(line), np.sin(line), np.zeros(100)] * u

        EKO()
        cone = np.r_[circle, np.array([[0, 0, 2 * u]])]
        h = u * .75 ** .5  # half-height of the hexagon
        halfagon = np.array([[u, 0, 0], [u / 2, h, 0], [-u / 2, h, 0]])
        hexagon = np.r_[halfagon, -halfagon]
        hexprism = np.r_[hexagon, hexagon + np.array([[0, 0, 2 * u]])]
        triangle = np.array([[u, 0, 0], [-u, 0, 0], [0, 2 * h, 0]])
        tetra = np.r_[triangle, np.array([[0, h, 2 * u]])]
        triprism = np.r_[triangle, triangle + np.array([[0, 0, 2 * u]])]
        square = np.array([[u, u, 0], [-u, u, 0], [-u, -u, 0], [u, -u, 0]])
        pyramid = np.r_[square, np.array([[0, 0, u * 2]])]

        if False :
                EKO()
                # Subdivided icosahedrons
                sphere80 = subdivide(icosa)  # pentakis icosidodecahedron
                sphere320 = subdivide(sphere80)  # 320 sided spherical polyhedra
                sphere1280 = subdivide(sphere320)  # 1280 sided spherical polyhedra
                EKO()
                halfsphere = np.r_[circle, top(sphere1280)]


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
    def add(self, x) :
        self.a = list(self.a) +  x
        
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
            self.assets().add([Material(name=blue, rgba=(0,0,1,1))])

            
            return self
    def worldbody(self) :        return self.find("Worldbody")
    def assets(self) :        return self.find("Asset")

    def find(self, n) :
        for e in self.a :
            EKOX(e.sname())
            if e.sname() == n:
                return e
        return None

    
class Default(X) :
    def __init__(self, *a) :
            super().__init__(a)
            self.a = a
            pass
    def __repr__(self) :
            return ("Default", str(self.a))

    
class Geom(X) :
    def __init__(self,
                 name=None,
                 rgba=None,
                 _type=None,
                 size=None,
                 quat=None,
                 pos=None,
                 material=None,
                 fromto=None) :
            super().__init__()

            self.rgba=rgba
            self.material=material
            self._type=_type
            self.size=size
            self.fromto=fromto
            self.name=name
            self.quat = quat
            self.pos = pos


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

class Site(X) :
    def __init__(self,
                 size=None,
                 rgba=None,
                 group=None) :
            super().__init__()
            self.size=size
            self.rgba=rgba
            self.group=group
            pass    

class Mesh(X) :
    def __init__(self,
                 name=None,
                 file=None) :
            super().__init__()
            self.file=file
            self.name = name
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
                 name=None,
                 rgba=None) :
            super().__init__()
            #self._type=_type,
            self.groundplane =groundplane
            self.texture =texture
            self.texuniform=texuniform
            self.texrepeat =texrepeat
            self.reflectance =reflectance 
            self.rgba =rgba 
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


position="position"
kp="kp"
kv="kv"
_class="_class"
forcerange="forcerange"
contype="contype"
conaffinity="conaffinity"
group="group"
material="material"
mass="mass"



blue="blue"

mesh="mesh"
damping="damping"
armature="armature"
plane="plane"
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

def axis() :
    e, l=0.008, 1.
    alpha = np.pi/2
    origin, xaxis, yaxis, zaxis = [0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]    
    EKOX(trimesh.transformations.quaternion_about_axis(alpha, xaxis))
    quat1 = tuple(trimesh.transformations.quaternion_about_axis(alpha, xaxis))
    quat2 = tuple(trimesh.transformations.quaternion_about_axis(alpha, yaxis))
    b = Body(pos(0,0,0))(
        Geom(size=(e,l), _type=cylinder, material=blue),
        Geom(pos=(0,l,-l), size=(e,l), _type=cylinder, quat=quat1, material=blue),
        Geom(pos=(l,0,-l), size=(e,l), _type=cylinder, quat=quat2, material=blue))
    return b
    
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
                                _type=_2d,
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
                                _type=_2d,
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
        

        example.worldbody().add([axis()])
        
        e1 = example
        EKOX("\n" + e1.xml())


