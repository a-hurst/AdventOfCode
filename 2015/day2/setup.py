from distutils.core import setup
from Cython.Build import cythonize

setup(name="day2_c", ext_modules=cythonize('day2_c.pyx'),)

