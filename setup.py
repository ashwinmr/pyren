from setuptools import setup

setup(
      name='pyren',
      version='0.1',
      description='Program for renaming files',
      url='https://github.com/ashwinmr/pyren',
      author='Ashwin Rao',
      author_email='iashwinrao@gmail.com',
      license='MIT',
      packages=['pyren'],
      include_package_data=True,
      entry_points = {
            'console_scripts': ['pyren = pyren.pyren:main']
      },
      zip_safe=False
)
