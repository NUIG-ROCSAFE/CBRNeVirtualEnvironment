cd ..
set base_dir=%cd%

echo %base_dir%

call BatchScripts\start_doc_retrieval.bat

cd %base_dir%
cd ./Mask_RCNN/samples
start python CPU_mode_laptop_object_detection_latest_file_final.py

cd %base_dir%
cd ./IJCAIDemoBinary/WindowsNoEditor
start OS_01RadiationIntegr
pause

