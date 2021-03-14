from distutils.core import setup
from Cython.Build import cythonize

setup(name="day3_c", ext_modules=cythonize('day3_c.pyx'))
