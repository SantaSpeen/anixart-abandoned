import os
import sys

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

packages = ['anixart']

requires = ['requests']

# 'setup.py publish' shortcut.
if sys.argv[-1] == 'publish':
    os.system('py -m build')
    os.system('py -m twine upload --repository pypi dist/*')
    os.system('py -m twine upload --repository testpypi dist/*')
    sys.exit()

about = {}
with open(os.path.join(here, 'anixart', '__version__.py'), 'r', encoding='utf-8') as f:
    exec(f.read(), about)

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    packages=packages,
    package_data={'': ['LICENSE', 'NOTICE']},
    package_dir={'anixart': 'anixart'},
    include_package_data=True,
    install_requires=requires,
    license=about['__license__'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        'Documentation': 'https://github.com/SantaSpeen/anixart/blob/master/README.md',
        'Source': 'https://github.com/SantaSpeen/anixart',
    },
    python_requires=">=3.6",
)
