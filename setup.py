from __future__ import absolute_import
from os.path import join, dirname
from setuptools import setup
import natoki.core
import natoki.chat

basepath = dirname(__file__)
binpath = join(basepath, 'bin')

setup(
  name = 'natoki',
  packages = ['natoki.core', 'natoki.chat'],
  version = natoki.core.__version__,
  description = 'A misterious chat server',
  long_description = open(join(basepath, 'README.txt')).read(),
  scripts = [join(binpath, 'natoki')],
  install_requires=['tornado'],
  author = 'Gamaliel Espinoza M.',
  author_email = 'gamaliel.espinoza@gmail.com',
  url = 'https://github.com/gamikun/natoki',
  keywords = ['chat', 'server', 'websocket'],
  classifiers = [],
)
