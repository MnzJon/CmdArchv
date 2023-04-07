from CmdArchive import CmdArchive 
from Command import CommandBuilder

cmdArch = CmdArchive()
cmdArch.setup_environment().environment_test()

cmdBuilder = CommandBuilder()
cmd = cmdBuilder.set_script("ls").set_epilogue("echo 'it worked'").append_token_flag(["FLAG1","ONE"]).build()

#cmdArch.run_cmd(cmd)
#print(cmd.to_dictionary())
#cmdArch.run_previous_cmd()
# cmdArch.select_history_cmd()
cmdArch.get_favourites()
# cmdArch.add_favourite_prompt()
