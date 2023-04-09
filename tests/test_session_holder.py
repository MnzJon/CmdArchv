import sys
sys.path.append("../")

from StateHolder import SessionStateHolder
from Command import Command, CommandBuilder
from CmdArchive import to_command
import os



def test_session_stateholder():
    cmdBuilder = CommandBuilder()
    cmdBuilder = cmdBuilder.set_script("ls").append_token_flag(["FLAG1","ON"]).set_build_cmd("build").set_epilogue("; notify.sh")
    cmd = cmdBuilder.build()

    session_state = SessionStateHolder("global", "./session_stateholder_test/")
    session_state.setup_environment()

    assert os.path.exists(os.path.abspath("./session_stateholder_test/"))
    
    session_state.insert_to_recent(cmd)
    assert str(to_command(session_state.get_recent_cmd())) == str(cmd)

def test_history():
    cmdBuilder = CommandBuilder()
    cmdBuilder = cmdBuilder.set_script("ls").append_token_flag(["FLAG1","ON"]).set_build_cmd("build").set_epilogue("; notify.sh")
    cmd = cmdBuilder.build()

    session_state = SessionStateHolder("global", "./session_stateholder_test/")
    session_state.setup_environment()

    session_state.record_cmd(cmd)

    # Test recent cmd
    assert str(to_command(session_state.get_recent_cmd())) == str(cmd)

    # Get the only command in history
    # No way to specify the ID via time
    old_cmd = {}
    for k in session_state.get_history().keys():
        old_cmd = session_state.get_history()[k]

    assert str(to_command(old_cmd)) == str(cmd)

