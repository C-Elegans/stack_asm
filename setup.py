from setuptools import setup

setup(
    name='stack_as',
    version='0.1',
    packages=['stack_as',],
    license='All rights reserved',
    long_description=open('README.md').read(),
    entry_points = {
        "console_scripts":[
            "stack_as = stack_as:main"
        ]
    }
)
