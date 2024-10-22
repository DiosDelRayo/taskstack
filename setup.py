from setuptools import setup

setup(
    name='taskstack',
    version='0.1',
    packages=['taskstack'],
    install_requires=['github3.py'],
    entry_points={
        'console_scripts': [
            'taskstack = taskstack.__main__:main',
        ],
    },
)

