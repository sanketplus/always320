from setuptools import setup


setup(
	name="always320",
	author=["Parth Parikh","Sanket Patel"],
	author_email=["parthpower@gmail.com","sanketplus@gmail.com"],
	maintainer=["Parth Parikh","Sanket Patel"],
	maintainer_email=["parthpower@gmail.com","sanketplus@gmail.com"],
	version="0.2.8",
	packages=['always320'],
    entry_points={
        'console_scripts': [
            'get320=always320.get320:main',
        ],
    },
	long_description='''# always320
Download [amlost] always high quality mp3 from YouTube.

`Usage: get320.py [-f file_name][Song Name]`

Specify a song name or input file with song name in each line.
	
	''',
	install_requires=['beautifulsoup4','html5lib','robobrowser'],
	extras_require = {
        'Vubey Support for Python2':  ['mechanize','wget']
    }
)