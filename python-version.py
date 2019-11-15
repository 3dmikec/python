'''
DISPLAYS PYTHON VERSION AND INFO
'''

import sys

def ver_info():
    print("Python version: " + str(sys.version))
    print("Version info: " + str(sys.version_info))

ver_info()

input("Press ENTER to exit")
