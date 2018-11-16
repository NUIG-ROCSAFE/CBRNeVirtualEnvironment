import os
import sys
import shutil


#This only works for linux
if not os.path.isdir(os.path.expanduser("~/AirSim/")):
    os.makedirs(os.path.expanduser("~/AirSim/"))

if not os.path.exists(os.path.expanduser("~/AirSim/settings.json")):
    shutil.copy(sys.argv[1], os.path.expanduser("~/AirSim/settings.json"))
