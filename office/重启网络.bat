@echo off
netsh int ip reset
ipconfig /release
ipconfig /renew
netsh winsock reset
shut*down /r /t 0