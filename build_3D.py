#https://github.com/format37/python3d/blob/main/solidpython_examples/solidpython_example_05.ipynb

from utillc import *
import solid2 as scad
import openpyscad as ops
import subprocess
import os, sys
import numpy as np
#from myplot import plot_verticles
from solid2 import *
import numpy as np
from scipy import spatial
#from stl import mesh
#from myplot import plot_mesh

import matplotlib.pyplot as plt
depth = 3
sponge = scad.cube([1,1,1], center = True)
z = 1.1
side = 1
for d in range(1, depth+1):
    side /= 3
    for x in range(1,3**d,3):
        for y in range(1,3**d,3):
            box_a = scad.cube([side,side,z], center = True)
            box_a = scad.translate([side*x-0.5+side/2, side*y-0.5+side/2, 0]) (box_a)            
            box_b = scad.rotate([90,0,0]) (box_a)
            box_c = scad.rotate([0,90,0]) (box_a)
            sponge -= box_a
            sponge -= box_b
            sponge -= box_c

#sponge = scad.translate([3.3, 0.5, 0.5]) (sponge)
d = cube(5) + sphere(5).right(5) - cylinder(r=2, h=6)

D, R, H, R1 = 20, 10, 1, 2.1

EKOX(scad.__file__)
d = cylinder(r=R, h=H, _fn=50)# + sphere(5).right(5) - cylinder(r=2, h=6)


for n in range(D) :
    a = n * 360 / D
    ar = n*2*np.pi/D
    x,y = (R-R1) * np.cos(ar), (R-R1) * np.sin(ar)
    #o = cylinder(h=H*2, r=R1, _fn=30).translate([x,y, 0])
    e = (R1-H)/2
    o = cube(R1).scale((4,1,1)).rotate(a=[0,0,a]).translate([x,y, -e])
    o1 = cube(R1).scale((4,1,1)).rotate(a=[0,0,a+20]).translate([x,y, -e])    
    
    d = d - o
    d = d - o1


render = scad_render_to_file(d, "example.scad")

sys.exit(0)

vertices = np.array([
    [-3, -3, 0],
    [+3, -3, 0],
    [+3, +3, 0],
    [-3, +3, 0],
    [+0, +0, +3]
])
plot_verticles(vertices = vertices, isosurf = False)

vertices = np.array(
[
[-3, -3, 0],
[+3, -3, 0],
[+3, +3, 0],
[-3, +3, 0],
[+0, +0, +3]
]
)
hull = spatial.ConvexHull(vertices)
faces = hull.simplices

myramid_mesh = mesh.Mesh(
  np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype)
)
for i, f in enumerate(faces):
  for j in range(3):
    myramid_mesh.vectors[i][j] = vertices[f[j],:]
    plot_mesh(myramid_mesh)

myramid_mesh.save('numpy_stl_example_02.stl')
points = np.array([
[0,0],
[-2,0],
[-2,2],
[0,1.5],
[2,2],
[2,0]
])
hull = spatial.ConvexHull(points)
    
import pymesh
box_a = pymesh.generate_box_mesh([0,0,0], [1,1,1])
box_b = pymesh.generate_box_mesh([0.4,0.4,0], [0.6,0.6,1])
box_c = pymesh.boolean(
  box_a,
  box_b,
  operation='difference',
  engine="igl"
)
filename = "/pymesh_examples/pymesh_example_02.stl"
pymesh.save_mesh(filename, box_c, ascii=False)

