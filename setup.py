from setuptools import setup
import platform

if platform.system() == 'Windows':
    setup(
        name='Multimedia Technik',
        version='0.1.0',
        packages=[''],
        url='',
        license='Apache License 2.0',
        author='Marvin Ferber',
        author_email='marvin.ferber@ba-sachsen.de',
        description='Beispielcode MMT',
        install_requires=[
            'pillow',
		    'numpy',
		    'matplotlib',
            'opencv-python'
        ]
    )
