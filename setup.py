'''
Test lib 1
'''

from setuptools import setup

HOST='git+https://github.com/alexanderdevm/'

setup(
    author='Demo',
    name='test-lib-1',
    version='1.0.0',
    description='Test lib 1',
    install_requires=[f'test-lib-2@{HOST}test-lib-2.git#egg=test-lib-2'],
    py_modules=['test-lib-1']
)
