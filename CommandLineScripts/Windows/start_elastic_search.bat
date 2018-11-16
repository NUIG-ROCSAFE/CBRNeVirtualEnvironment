@echo off
:main
    setlocal enabledelayedexpansion
    set base_dir=%cd%

    echo %base_dir%

    call :get-ini ../../Config/config.ini ELASTICSEARCH ElasticSearchBinLoc result
    
    echo r=%result%
    
    cd ../..
    cd %result%
    start elasticsearch
    SLEEP 1

    REM should check that this is not blank
    powershell.exe Invoke-WebRequest 127.0.0.1:9200
    REM remove any old indices and insert a new one
    powershell.exe Invoke-WebRequest -Method DELETE 127.0.0.1:9200/_all
    powershell.exe Invoke-WebRequest -Method PUT 127.0.0.1:9200/sops?pretty
    goto :eof

    

:get-ini <filename> <section> <key> <result>
  set %~4=
  setlocal
  set insection=
  for /f "usebackq eol=; tokens=*" %%a in ("%~1") do (
    set line=%%a
    if defined insection (
      for /f "tokens=1,* delims==" %%b in ("!line!") do (
        if /i "%%b"=="%3" (
          endlocal
          set %~4=%%c
          goto :eof
        )
      )
    )
    if "!line:~0,1!"=="[" (
      for /f "delims=[]" %%b in ("!line!") do (
        if /i "%%b"=="%2" (
          set insection=1
        ) else (
          endlocal
          if defined insection goto :eof
        )
      )
    )
  )
  endlocal