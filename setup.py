from setuptools import setup, find_packages

setup(
  name='spot-sdk',
  version='2017.9.4.1',
  description='SDK for the find me spot',
  long_description=open('README.rst').read(),
  url='https://github.com/gregology/spot-sdk',
  author='Greg Clarke',
  author_email='greg@gho.st',
  license='MIT',
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python'
  ],
  keywords='spot',
  packages=find_packages(),
  package_data={
    'spot_sdk': []
  }
)
