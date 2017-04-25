from setuptools import setup


setup(
	name="always320",
	author=["Parth Parikh","Sanket Patel"],
	author_email=["parthpower@gmail.com","sanketplus@gmail.com"],
	maintainer=["Parth Parikh","Sanket Patel"],
	maintainer_email=["parthpower@gmail.com","sanketplus@gmail.com"],
	url="http://superuser.blog",
	version="0.2.5",
	packages=['always320'],
    entry_points={
        'console_scripts': [
            'get320=always320.get320:main',
        ],
    },
	long_description='''# always320
Download [amlost] always 320kpbs high quality mp3 from YouTube.

`Usage: get320.py [-f file_name][Song Name]`

Specify a song name or input file with song name in each line.
	
	''',
	install_requires=['mechanize','beautifulsoup','html5lib','wget']
)