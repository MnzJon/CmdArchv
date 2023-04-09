from ShellCommand import ShellCommand

def add(d_x):
    return d_x["x"] + 2

def test_shell_command():
    scmd = ShellCommand("add")

    assert scmd.add_function(add)
    assert scmd.is_base()

    assert scmd.run_cmd({"x": 2}) != None

def test_shell_add():
    cmd = ShellCommand("show")
    cmd.add_function(add)
    scmd = ShellCommand("history")

    assert scmd.add_cmd(cmd)

    next_cmd = scmd.get_cmd("show")
    assert next_cmd != None
    assert next_cmd.is_base()
