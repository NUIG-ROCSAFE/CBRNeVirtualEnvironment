cd ../..
set base_dir=%cd%

cd ./RAVCollectedData/PNGImages/ImagesRAV1
del /F /S *.png

cd %base_dir%

cd ./PythonCode/Routing/AirSimPythonClient/RAVExecuteRoutes
start python rav_zero_mapper.py
