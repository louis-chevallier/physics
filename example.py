from py2xml import *
from py2xml import _2d


def muj() :
    r =  Mujoco(model="example")(
        Default(
            Geom(rgba=rgba(.8, .6, .4, 1))),
        Asset(
            Texture(_type=skybox,
                    builtin=gradient,
                    rgb1=(.3, .5, .7),
                    width=32,
                    height=512),
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
                     reflectance=0.2)),
        
        Worldbody(
            Light(pos=(0,1,1), dir=(0,-1, -1), diffuse=(1,1,1)),
            Body(pos(0,0.,-0.5))(
                Geom(name="floor", size=(0,0,0.05), _type=plane, material=groundplane))))

    l = []
    l.append(
        Body(pos(0,0.5,0.6))(
		    #Joint(_type=ball),
		    Geom(_type=box, size=0.06, fromto=(0,0,0, 0,0,0.3))))
    if True :
        l.append(Body(pos=pos(0,0.5,0.01))(
		    Joint(axis=(0,1,0)),
		    #Joint(axis=(1,0,0)),
		    Geom(_type=cylinder, size=0.06, fromto=(0,0,0, -0.3,0,0))))
        
    if (False) :
        l = []        
        e = (0.2, 0.3, 0.4)
        
        l.append(Body(pos(0,0.5,0))(
		    Joint(axis=(0,1,0)),    
		    Geom(_type=box, size=e, rgba=(0.1, 0.9, 0.1, 1), fromto=(0,0,0, 0,0,0.1))))
        l.append(Body(pos(0,0.5,1))(
		    Joint(_type=ball),
		    Geom(_type=capsule, size=0.06, fromto=(0,0,0, 0,0,-0.4))))
    


    
    r.worldbody().add([axis()])
    r.worldbody().add(l)
    return r
    
    
