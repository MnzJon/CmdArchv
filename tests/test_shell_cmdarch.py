import sys
sys.path.append("../")

from ShellCmdArch import ShellCmdArchAST, parse_shell_input, ShellCmdArch
import os

def test_parse_input():
    inp = "-a -d -s history show"
    ast = parse_shell_input(inp)

    expected_options = {"a": True, "d": True, "s": True}
    expected_commands = ["history", "show"]

    assert ast != None
    assert ast.get_options() == expected_options
    assert ast.get_commands() == expected_commands

