import os
import subprocess

# os.system("start cmd /c dir")
# os.system("start /B start cmd.exe @cmd /k dir")
# Needs to be shell since start isn't an executable, its a shell cmd
# p = subprocess.Popen(["start", "cmd", "/k", "dir"], shell=True)
# p.wait()
import subprocess
import subprocess
import os

# os.system("gnome-terminal -e 'bash -c \"sudo apt-get update; exec bash\"'")
# os.system("gnome-terminal -e 'bash -c \"ssh evanik@192.168.1.17 exec bash\"'")
# os.system("gnome-terminal --window --title=Log -e 'ssh evanik@192.168.1.17'")
# p = subprocess.call(["gnome-terminal", "--", "python3", "server_login_paramiko.py"])
os.system("gnome-terminal --tab -- sshpass -p evanik ssh -o StrictHostKeyChecking=no evanik@192.168.1.17")
os.system("gnome-terminal -e 'bash -c \"sudo apt-get update; exec bash\"'")
