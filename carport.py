from utillc import *
from solid import *
import numpy as np

import sys
from math import cos, radians, sin, pi, tau
from pathlib import Path

from euclid3 import Point2, Point3, Vector3

from euclid3 import Point2, Point3, Vector3

from solid import scad_render_to_file, text, translate, cube, color, rotate
from solid.utils import UP_VEC, Vector23, distribute_in_grid, extrude_along_path
from solid.utils import down, right, frange, lerp




from typing import Set, Sequence, List, Callable, Optional, Union, Iterable, Tuple



SEGMENTS = 48
PATH_RAD = 50 
SHAPE_RAD = 15

TEXT_LOC = [-0.6 *PATH_RAD, 1.6 * PATH_RAD]

H, W, L = 1600, 300, 300
e,l = 3.6, 14.5
sol = cube((W,L, 1))

Black       = (0, 0, 0)
def make_label(message:str, text_loc:Tuple[float, float]=TEXT_LOC, height=5) -> OpenSCADObject:
    return translate(text_loc)(
        linear_extrude(height)(
            text(message)
        )
    )


def star(num_points=5, outer_rad=SHAPE_RAD, dip_factor=0.5) -> List[Point3]:
    star_pts = []
    for i in range(2 * num_points):
        rad = outer_rad - i % 2 * dip_factor * outer_rad
        angle = radians(360 / (2 * num_points) * i)
        star_pts.append(Point3(rad * cos(angle), rad * sin(angle), 0))
    return star_pts

def sinusoidal_ring(rad=25, segments=SEGMENTS) -> List[Point3]:
    outline = []
    for i in range(segments):
        angle = radians(i * 360 / segments)
        scaled_rad = (1 + 0.18*cos(angle*5)) * rad
        x = scaled_rad * cos(angle)
        y = scaled_rad * sin(angle)
        z = 0
        # Or stir it up and add an oscillation in z as well
        # z = 3 * sin(angle * 6)
        outline.append(Point3(x, y, z))
    return outline


def vague(d) :
        w = 35
        outline = [ Point3(x+d*w, 0, z) for (x, z) in [ (0,0), (30, 0), (31, 3),  (34, 3),  (35, 0)] ]
        return outline

def vagues() :
        l = []
        for n in range(10) :
                l = l + vague(n)
        return l

def profil() :
        return vagues()

def toit():
    path_rad = PATH_RAD
    shape = star(num_points=5)
    shape = [ Point3(0, 0, 0), Point3(800, 0, 0)]
    path = sinusoidal_ring(rad=path_rad, segments=240)
    path = profil()

    # At its simplest, just sweep a shape along a path
    extruded = extrude_along_path( shape_pts=shape, path_pts=path)
    extruded += make_label('Carport')
    #return profil()
    return translate((0,800-50,320))(extruded)


def poteau() :
        return cube((e, l, 300))

def jambe(s=1) :
        return rotate((45 * s, 0, 0))(cube((e, l, np.sqrt(2) * 100)))

def traverse(s=1) :
        return cube((300, 5, 20))

def jambes(dd=60, s=1, rr=1) :
        return union() ( [ translate((0, x + 100 * rr, dd))(jambe(s)) for x in range(0, 700, 100)])


def poutre() :
        return cube((8, 400, 20))

def align() :
        return union()([ translate((0, x, 0))(poteau()) for x in range(0, 800, 100)])

def traverses() :
        return translate((0,0,300))(union()([ translate((0, x, 0))(traverse()) for x in range(0, 800, 100)]))


def poutres(vv=0) :
        return  translate((-e + vv, -50, 0))(union()(
                translate((0, 0, 300))(poutre()),
                translate((0, 400, 300))(poutre())))


#EKOX(dir(cube))



d = align() + poutres() + poutres(300) + jambes() + jambes(200, -1, 0) + traverses() + color('grey')(toit())
EKOX(d)

file_out = scad_render_to_file(d, out_dir='.', include_orig_code=True)

