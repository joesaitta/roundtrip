REM Example file to execute from a remote Linux system, then pass output back to Linux
@echo off
set host=%COMPUTERNAME%
set user=%USERNAME%
set remote_file=/home/%user%/PycharmProjects/linux_to_windows/windows_response_%host%.txt
set linux_cmd=/home/jsaitta/PycharmProjects/linux_to_windows/linux_response.py
set final_file=/home/jsaitta/PycharmProjects/linux_to_windows/final_file.txt

REM Write a file, then send it over to Linux and execute a Linux process 
@echo File created from %1 %date%-%time% > %2

REM Copy the file over to Linux
scp %2 %user%@linux_host:%remote_file%

REM Execute the Linux code to parse to what we just created/copied over
ssh %user%@linux_host python3 %linux_cmd% -infile %remote_file% -outfile %final_file%