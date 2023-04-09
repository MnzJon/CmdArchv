import sys
sys.path.append("../")

from StateHolder import FileStateHolder
import os

def test_filestate_holder():
    f_sh = FileStateHolder("testing_holder.json")
    f_sh.setup_path()

    # File exists
    assert os.path.exists(f_sh.get_path())
    # Set element
    f_sh.set_element("recent","Hallelujah!")
    assert f_sh.get_element("recent") == "Hallelujah!"
    expected_state = {"recent": "Hallelujah!"}
    assert f_sh.get_state() == expected_state

