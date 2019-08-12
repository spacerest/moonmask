from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name = 'moonmask',
    packages = find_packages(),
    version = '2.3',
    license='MIT',
    description = 'Gets moon visualizations courtesy of Ernie Wright and uses them for artistic collages',
    author = 'Sadie Parker',
    author_email = 'sadiemparker@gmail.com',
    url = 'https://github.com/spacerest/moonmask',
    download_url = 'https://github.com/spacerest/moonmask/archive/v_23.tar.gz',
    keywords = ['MOON', 'ART'],
    install_requires=[
        'atomicwrites==1.3.0',
        'attrs==19.1.0',
        'importlib-metadata==0.18',
        'more-itertools==7.2.0',
        'numpy==1.16.4',
        'opencv-python==4.1.0.25',
        'packaging==19.0',
        'pluggy==0.12.0',
        'py==1.8.0',
        'pyparsing==2.4.2',
        'pytest==5.0.1',
        'six==1.12.0',
        'wcwidth==0.1.7',
        'zipp==0.5.2',
    ],
    classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Other Audience',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
