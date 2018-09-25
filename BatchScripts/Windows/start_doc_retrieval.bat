set base_dir=%cd%

echo %base_dir%

REM 
cd ./elasticsearch-oss-6.3.0/elasticsearch-6.3.0/bin
REM 
start elasticsearch 

REM allow elasticsearch to start up
SLEEP 15

REM should check that this is not blank
powershell.exe Invoke-WebRequest 127.0.0.1:9200
REM remove any old indices and insert a new one
powershell.exe Invoke-WebRequest -Method DELETE 127.0.0.1:9200/_all
powershell.exe Invoke-WebRequest -Method PUT 127.0.0.1:9200/sops?pretty
cd %base_dir%
cd ./BrettSOPRanking/RocsafeCode/Demo-IR
python insertRecords.py

cd %base_dir%
cd ./BrettSOPRanking/RocsafeCode/Demo-IR
start python display.py