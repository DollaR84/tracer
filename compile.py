"""
Compile module in python library pid.

Created on 25.04.2019

@author: Ruslan Dolovanyuk

example running:
    python compile.py build_ext --inplace

"""

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
               Extension("commands", ["commands.py"]),
               Extension("dialogs", ["dialogs.py"]),
               Extension("drawer", ["drawer.py"]),
               Extension("extrows", ["extrows.py"])
              ]

setup(
      name='main',
      cmdclass={'build_ext': build_ext},
      ext_modules=ext_modules
)
