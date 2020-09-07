from setuptools import setup, find_packages

exclude = ['examples']

setup(
    name='shublang',
    version='0.2.2',
    license='BSD',
    author='Akshay Philar',
    author_email='akshayphilar@gmail.com',
    description='Shublang - Data Extraction DSL',
    url="https://github.com/scrapinghub/shublang",
    packages=find_packages(exclude=exclude),
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
    python_requires='>=3.6',
    install_requires=[
        'pipe >= 1.5.0',
        'jmespath >= 0.9.4',
        'w3lib >= 1.21.0',
        'parsel >= 1.5.2',
        'dateparser >= 0.7.2',
        'price-parser >= 0.3.2',
    ]
)