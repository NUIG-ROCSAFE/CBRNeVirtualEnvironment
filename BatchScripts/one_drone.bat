cd ..
set base_dir=%cd%

cd ./PythonCode/PythonClientGPSMapping/GPSMappings/Images/Images1/Camera1
del *.png

cd %base_dir%

cd ./PythonCode/PythonGridMapping/AirSimPythonClient
start python rav_zero_mapper.py
