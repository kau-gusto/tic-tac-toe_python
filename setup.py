from setuptools import setup, find_packages

setup(
    name='tic_tac_toe',
    version='0.1.0',
    author='Kauan Augusto',
    author_email='kauaug.mo@gmail.com',
    description='A simple package for creation of a tic_tac_toe',
    packages=find_packages("tic_tac_toe"),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)