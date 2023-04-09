
import sys
sys.path.append("../")

from Command import CommandBuilder, Command
from CmdArchive import CmdArchive, to_command
from StateHolder import SessionStateHolder
import os

def test_environment():
    cmdArch = CmdArchive("./session_test_archive/")
    cmdArch.setup_environment()

    # assert os.path.exists("./session_test_archive/history.json")
    assert os.path.exists("./session_test_archive/favourites.json")
    assert os.path.exists("./session_test_archive/parameter_flags.json")

def test_favourites():
    cmdArch = CmdArchive("./session_test_archive/")
    cmdArch.setup_environment()

    cmdBuilder = CommandBuilder()
    cmdBuilder = cmdBuilder.set_script("ls").append_token_flag(["FLAG1","ON"]).set_build_cmd("build").set_epilogue("; notify.sh")
    cmd = cmdBuilder.build()

    cmdArch.add_favourite("fav1",cmd)

    favourites = cmdArch.get_favourites()
    assert str(to_command(favourites["fav1"])) == str(cmd)


def test_parameters():
    cmdArch = CmdArchive("./session_test_archive/")
    cmdArch.setup_environment()

    cmdArch.add_parameter_flag("Flag1")

    assert cmdArch.get_parameters() == {"Flag1": True}

    cmdArch.remove_parameter("Flag1")

    assert cmdArch.get_parameters() == {}
