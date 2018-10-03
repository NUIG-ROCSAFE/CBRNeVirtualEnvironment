

cd ..
set base_dir=%cd%

echo %base_dir%

REM everything here is commented cd ./elasticsearch-oss-6.3.0/elasticsearch-6.3.0/bin
REM everything here is commented start elasticsearch 

cd %base_dir%
cd ./BrettSOPRanking/RocsafeCode/Demo-IR
start python display.py

cd %base_dir%
cd ./Mask_RCNN/samples
start python CPU_mode_laptop_object_detection_latest_file_final.py

cd %base_dir%
cd ./IJCAIDemoBinary/WindowsNoEditor
start OS_01RadiationIntegr
pause

