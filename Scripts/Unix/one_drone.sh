cd ../..

base_dir="$( cd "$(dirname "$0")" ; pwd -P )"

cd ./RAVCollectedData/PNGImages/ImagesRAV1
find -type f -iname '*.png' -delete

cd $base_dir

cd ./PythonCode/Routing/AirSimPythonClient/RAVExecuteRoutes
python3 rav_zero_mapper.py

