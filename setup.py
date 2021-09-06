from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='This project will analyse global land temperature from datasets provided by Berkeley Earth, eventually building a predictive model to predict what global land temperatures will look like several years into the future. The two datasets to be used are global land temperatures by city and by country.',
    author='Sophia Wisniewska',
    license='MIT',
)
