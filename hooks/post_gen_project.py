import os
import subprocess


# poetry lock and install
print("> Initializing git repository")
subprocess.call(["poetry", "install"])

# initialize the git repository
print("> Initializing git repository")
subprocess.call(["git", "init"])
subprocess.call(["git", "add", "*"])
subprocess.call(["git", "commit", "-m", "Cookiectutter generated initial commit"])
