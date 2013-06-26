# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='pygments-routerlexers',
    version='0.3.2',
    description="""Pygment lexers for router configuration files""" ,
    author="Brandon Bennett",
    packages = find_packages(),
    entry_points='''
    [pygments.lexers]
    IOSLexer = pygments_routerlexers:IOSLexer
    JunosLexer = pygments_routerlexers:JunosLexer
    ScreenOSLexer = pygments_routerlexers:ScreenOSLexer
    ''',
)

