from CmdArchive import CmdArchive 
from Command import CommandBuilder

cmdArch = CmdArchive()
cmdArch.setup_environment().environment_test()

cmdBuilder = CommandBuilder()
cmd = cmdBuilder.set_script("ls").set_epilogue("echo 'it worked'").build()

cmdArch.run_cmd(cmd)

