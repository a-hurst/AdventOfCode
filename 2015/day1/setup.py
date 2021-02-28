from distutils.core import setup
from Cython.Build import cythonize

setup(name="day1_c", ext_modules=cythonize('day1_c.pyx'),)

