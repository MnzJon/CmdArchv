import sys
import time
sys.path.append("../")

from Command import CommandBuilder, Command
from CmdArchive import CmdArchive, to_command
from APICmdArchive import APICmdArchive
from StateHolder import SessionStateHolder
import os

def run_api_history():
    api_cmdArch = APICmdArchive("./api_test/")
    session_state = api_cmdArch.get_global_session()

    #api_cmdArch.show_history(session_state)

    cmdBuilder = CommandBuilder()
    cmdBuilder = cmdBuilder.set_script("ls").append_token_flag(["FLAG1","ON"]).set_build_cmd("build").set_epilogue("; notify.sh")
    cmd = cmdBuilder.build()


    api_cmdArch.store_cmd(cmd, session_state)
    api_cmdArch.store_cmd(cmd, session_state)

    api_cmdArch.show_history(session_state)
    api_cmdArch.clear_history(session_state)

run_api_history()
