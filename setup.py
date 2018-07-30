from setuptools import setup,find_packages
setup(name='hello world',
version='1.0',
author='kela',
packages=find_packages('src'),
package_data={
    '':['*.txt', 'hello_*'],
    },
entry_points = {
    'console_scripts':[
        'hello = bin.hello_world1:main',
	'world = bin.hello_world2:main',
	'yeh = bin.hello_world3:_main'
	]
	}
)
