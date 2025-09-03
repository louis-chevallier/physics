import mujoco
import time
import itertools
import numpy as np
#import mediapy as media
import matplotlib.pyplot as plt
from utillc import *
import os
import mujoco
import mujoco.viewer
import time
import math

import argparse
import os, sys
import time
from utillc import *
parser = argparse.ArgumentParser()
parser.add_argument('--xml')
args = parser.parse_args()
path = args.xml

def load() :
    with open(path, "r") as fd:
        XML = fd.read()
    ti_m = os.path.getmtime(path)
    m = mujoco.MjModel.from_xml_string(XML)
    d = mujoco.MjData(m)
    return m, d,ti_m

while True :
    m,d,ti = load()
    EKO()
    with mujoco.viewer.launch_passive(m, d) as viewer:
        start = time.time()
        EKO()
        while viewer.is_running() :
            step_start = time.time()
            ti_m2 = os.path.getmtime(path)
            if (ti_m2 > ti) :
                EKOT("reload")
                m,d,ti = load()
                break
            mujoco.mj_step(m, d)
            time.sleep(1./240.)



