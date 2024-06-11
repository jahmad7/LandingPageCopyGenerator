from setuptools import setup, find_packages

setup(
    name='LandingPageCopyGenerator',
    version='0.1.0',
    packages=find_packages(),
    entry_points='''
        [console_scripts]
        LandingPageCopyGenerator=LandingPageCopyGenerator.main:main
    ''',
)