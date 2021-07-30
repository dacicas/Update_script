import os
import subprocess
import sys
import shutil

Bits = "D:\\Test_Firefox\\87.0b1\\BITS_testing.txt"
os.chdir("C:\\Program Files\\Mozilla Firefox\\uninstall")
subprocess.call(["C:\\Program Files\\Mozilla Firefox\\uninstall\\helper.exe", "/s"])
firefox = "D:\\Test_Firefox\\88.0b1"
os.remove(Bits)
shutil.rmtree(firefox, ignore_errors=True)
