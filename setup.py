from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='acb2csv',
      version='0.3',
      description='Team/Players performance importer/exporter',
      url='https://github.com/alxgarcia/acb2csv',
      author='alxgarcia',
      author_email='alxgarcia@github.com',
      license='MIT',
      packages=['acb2csv'],
      entry_points={
          'console_scripts': ['acb2csv=acb2csv.command_line:main'],
      },
      install_requires=['beautifulsoup4'],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
