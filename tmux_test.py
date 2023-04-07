from StateHolder import TmuxStateHolder

import subprocess
import os 
from io import StringIO # Python3 use: from io import StringIO
import sys
import libtmux
s = libtmux.Server()

tmux = TmuxStateHolder()
print(s.session)

try:
    #print(os.environ["TMUX"])
    tmux.session_id()
except:
    print("No TMUX")


