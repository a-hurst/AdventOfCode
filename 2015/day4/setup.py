from distutils.core import setup
from Cython.Build import cythonize

setup(name="day4_c", ext_modules=cythonize('day4_c.pyx'))
