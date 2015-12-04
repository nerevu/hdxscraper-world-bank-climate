import sys
import app
import pkutils

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

sys.dont_write_bytecode = True
requirements = list(pkutils.parse_requirements('requirements.txt'))
dev_requirements = list(pkutils.parse_requirements('dev-requirements.txt'))
dependencies = list(pkutils.parse_requirements('requirements.txt', dep=True))
readme = pkutils.read('README.md')
changes = pkutils.read('CHANGES.rst').replace('.. :changelog:', '')
license = app.__license__
name = app.__title__
gh = 'https://github.com/reubano'

setup(
    name=name,
    version=app.__version__,
    description=app.__description__,
    long_description=readme,
    author=app.__author__,
    author_email=app.__email__,
    url='%s/%s' % (gh, name),
    download_url='%s/%s/downloads/%s*.tgz' % (gh, name, name),
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        pkutils.LICENSES[license],
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Microsoft :: POSIX'
    ],
    keywords=[name],
    packages=find_packages(exclude=['tests']),
    package_data={},
    zip_safe=False,
    license=license,
    platforms=['MacOS X', 'Windows', 'Linux'],
)
