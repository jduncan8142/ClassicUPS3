from distutils.core import setup

setup(
    name='ClassicUPS3',
    version='0.1.8',
    author='Jason Duncan',
    author_email='jason.matthew.duncan@gmail.com',
    url='https://github.com/jduncan8142/ClassicUPS3',
    packages=['ClassicUPS3'],
    description='Usable UPS Integration in Python 3',
    long_description=open('README.rst').read(),
    keywords=['UPS'],
    install_requires=[
        'dict2xml==1.0',
        'xmltodict==0.4.2'
    ],
    classifiers=[
        'Programming Language :: Python 3',
        'License :: GNU General Public License v3.0',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Development Status :: 4 - Beta'
    ]
)

# To update pypi: `python setup.py register sdist bdist_wininst upload`
