from StateHolder import TmuxStateHolder

import subprocess
import os 
from io import StringIO # Python3 use: from io import StringIO
import sys
import libtmux
s = libtmux.Server()

tmux = TmuxStateHolder("~/.local/share/cmd_archive/tmux/")

try:
    #print(os.environ["TMUX"])
    #tmux.session_id()
    print(tmux.get_path())
except Exception as e:
    print(e)
    print("No TMUX")


