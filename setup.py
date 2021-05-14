from setuptools import setup

setup(
    name='OptiCon',
    version='0.0.1',
    packages=['OptiCon'],
    url='https://github.com/IndigoMod/OptiCon',
    license='MIT',
    author='beta5051',
    author_email='AcaiBerii@protonmail.com',
    description='MinecraftWS fork that provides optimal performance and compatibility with IndigoMod.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=['websockets>=8.1']
)
