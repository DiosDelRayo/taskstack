from setuptools import setup

setup(
    name='taskstack',
    version='0.2',
    packages=['taskstack'],
    install_requires=['github3.py'],
    entry_points={
        'console_scripts': [
            'taskstack = taskstack.__main__:main',
            'taskstack-start = taskstack.__main__:start',
            'taskstack-stop = taskstack.__main__:stop',
            'taskstack-next = taskstack.__main__:next',
            'ts = taskstack.__main__:main',
            'ts = taskstack.__main__:main',
        ],
    },
)

