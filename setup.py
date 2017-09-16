from setuptools import setup, find_packages

setup(
    name='tveebot-common',
    version='0.1',
    description='Packages containing modules used by the daemon and the client',
    url='https://github.com/tveebot/common',
    license='MIT',
    author='David Fialho',
    author_email='fialho.david@protonmail.com',

    packages=find_packages(),
)
