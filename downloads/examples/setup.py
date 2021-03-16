# setup.py
# python setup.py build_ext --inplace

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
  name = 'Test app',
  ext_modules=[
    Extension('test',
              sources=['testobj.pyx'],
              extra_compile_args=['-Wno-cpp', '-std=c++17', '-fopenmp', '-DMS_WIN64'],
              language='c++')
    ],
  cmdclass = {'build_ext': build_ext}
)
