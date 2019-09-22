from subprocess import Popen, PIPE
import os

from pathlib import Path, PureWindowsPath

shellpath = r"c:\windows\system32\WindowsPowerShell\v1.0\powershell.exe"
# print(PureWindowsPath(shellpath))
# subprocess.run()
print("Enter command:")
ar = input()

p = Popen([shellpath, ar], stdin=PIPE, stdout=PIPE,
          stderr=PIPE, universal_newlines=True)
# [ 'ls -l']
stdout, stderr = p.communicate()
print(stdout+"  \n Error :"+stderr)
p.kill()
