from setuptools import setup, find_packages


setup(
    name='ddconnector',
    version='0.1',
    description='Doordu connect your world!',
    author='Aidan He',
    author_email='erhuabushuo@gmail.com',
    url='https://gitlab.doordu.com/server/ddconnector',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    platforms='all',
    data_files=[
        ('/etc', ['ddconnector.ini'])
    ],
    install_requires=[
        'uvloop',
        'aioredis',
        'raven',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 3.6',
        'Topic :: Communications',
        'Topic :: Internet'        
    ],
    entry_points={
        'console_scripts': [
            'ddconnector = scripts.ddconnector_script:main'
        ]
    },
)