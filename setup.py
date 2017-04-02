from setuptools import setup

version = '0.1.0'
name = 'nlcalc'
install_requires = ['botify']

setup(name=name,
      version=version,
      description='Natural Language Mathematical Calculator',
      install_requires=install_requires,
      long_description=open('README.rst', 'rt').read(),
      author='Priyam Singh',
      author_email='priyamsingh.22296@gmail.com',
      packages=['nlcalc'],
      url='https://github.com/pri22296/{}'.format(name),
      download_url='https://github.com/pri22296/{}/tarball/{}'.format(name, version),
      license='MIT',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.5',
      ],
)
