import sys
sys.path.append("../")

from CmdArchive import CmdArchive
import os

def test_cmdarchive():
    cmdArch = CmdArchive("./test_home_archive/")
    cmdArch.setup_environment()
