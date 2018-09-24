## GPSMappings Direcory
This directory contains the python classes that convert GPS coordinates to unreal engine coordinates. Vincenty's formulas are used to calculate the conversions. AirSimClient is copied from the main AirSim repo and has been modified to contain a GPSToUnreal class which converts GPS coordinates to Unreal Engine NED coordinates. The unreal engine coordinates are relative the RAV's home position and can be used with AirSim RAVS.

## RAVRoutes Directory
This directory contains the files rav_<>_mapper.py, which will execute routes which are automatically written by generateRoutesForUnreal.py. 
