from CmdArchive import APICmdArchive

cmdAPI = APICmdArchive()
cmdAPI.sanity_check()
cmdAPI.show_history()
cmdAPI.show_favourites()

cmdAPI.show_parameters()
cmdAPI.run_previous_cmd()
cmdAPI.run_favourite("test_id")
cmdAPI.select_cmd_from_history()

