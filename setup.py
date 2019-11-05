from setuptools import setup, find_packages


setup(
    name='shublang',
    version='0.1.0',
    license='BSD',
    description='Shublang - Data Extraction DSL',
    author='Akshay',
    author_email='akshay@scrapinghub.com',
    packages=['shublang'],
    package_data={'shublang': ['*.py']},
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

    ]
)