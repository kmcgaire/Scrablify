
from setuptools import setup

setup(
    name='scrableify',
    version='1.0',
    description='Scrabble Emoji The things',
    packages=['scrableify'],
    entry_points={
        'console_scripts': [
            'scrableify=scrableify.commands:scrableify'
        ]
    }
)
