import os
import subprocess
def runcmd(cmd):
    os.popen(cmd).read()