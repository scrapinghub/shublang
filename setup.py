from setuptools import setup, find_packages

exclude = ['examples']

setup(
    name='shublang',
    version='0.1.2',
    license='BSD',
    description='Shublang - Data Extraction DSL',
    author='Akshay',
    author_email='akshay@scrapinghub.com',
    packages=find_packages(exclude=exclude),
    #package_data={'shublang': ['*.py']},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'shublang = shublang.cmdline:execute_from_command_line'
        ]
    },
    platforms=['Any'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=[
        'pipe >= 1.5.0',
        'jmespath >= 0.9.4',
        'w3lib >= 1.21.0',
        'parsel >= 1.5.2',
        'dateparser >= 0.7.2',
        'price-parser >= 0.3.2',
    ]
)