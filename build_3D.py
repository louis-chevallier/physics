#https://github.com/format37/python3d/blob/main/solidpython_examples/solidpython_example_05.ipynb


import numpy as np
from myplot import plot_verticles

import numpy as np
from scipy import spatial
from stl import mesh
from myplot import plot_mesh

import matplotlib.pyplot as plt
from scipy import spatial
import numpy as np


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
    
import pymeshbox_a = pymesh.generate_box_mesh([0,0,0], [1,1,1])
box_b = pymesh.generate_box_mesh([0.4,0.4,0], [0.6,0.6,1])
box_c = pymesh.boolean(
  box_a,
  box_b,
  operation='difference',
  engine="igl"
)
filename = "/pymesh_examples/pymesh_example_02.stl"
pymesh.save_mesh(filename, box_c, ascii=False)

