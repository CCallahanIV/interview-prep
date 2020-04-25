import inspect
import os
import sys


testfile = os.path.abspath(inspect.getsourcefile(lambda: 0))
testdir = os.path.split(testfile)[0]
srcdir = os.path.join(os.path.split(testdir)[0], "src")

sys.path.insert(0, srcdir)