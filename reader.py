import pybullet as p
import time
import math
import pybullet_data
import argparse
import os, sys
import time
from utillc import *
parser = argparse.ArgumentParser()
parser.add_argument('--urdf')
args = parser.parse_args()

useGui = True
path = args.urdf
if (useGui):
  p.connect(p.GUI)
else:
  p.connect(p.DIRECT)

p.resetSimulation()
  
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
#p.configureDebugVisualizer(p.COV_ENABLE_RENDERING,0)

p.setGravity(0, 0, -10)
timeStep = 1. / 240.

def load() :
  p.setAdditionalSearchPath(pybullet_data.getDataPath())
  p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
  #p.configureDebugVisualizer(p.COV_ENABLE_RENDERING,0)

  p.setGravity(0, 0, -10)
  ti_m = os.path.getmtime(path)

  shp = p.createCollisionShape(p.GEOM_PLANE)
  p.createMultiBody(1,shp)
  EKOX(shp)
  
  ii = p.loadURDF(path, [0, 0, 1])
  EKOX(ii)
  EKOX(p.getBodyInfo(ii));
      
  return ii, ti_m

ii, ti = load()

while(1) :
  EKO()
  while (1) :

    a=1
    
    ti_m2 = os.path.getmtime(path)
    if (ti_m2 > ti) :
      
      EKOT("reload")
      p.removeBody(ii)
      p.resetSimulation()
      p.disconnect()
      p.connect(p.GUI)
      
      ii, ti = load()
      break
    keys = p.getKeyboardEvents()
    if keys.get(97 + ord('Q') - ord('A')):   #A
      sys.exit(0)

      time.sleep(timeStep)
  EKO()
