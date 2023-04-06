from Command import CommandBuilder

cmdBuilder = CommandBuilder()
cmdBuilder.set_script("json").set_build_cmd("make").set_epilogue("notify.sh").append_token_flag(["FLAG_ONE","ON"])


my_cmd = cmdBuilder.build()

print(str(my_cmd))

