#!/usr/bin/env python3
import subprocess

x = subprocess.check_output("ifconfig")
print(x)
