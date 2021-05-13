from setuptools import setup

setup(
    name='OptiCon',
    version='1.1.1',
    packages=['OptiCon'],
    url='https://github.com/Beta5051/MinecraftWS',
    license='MIT',
    author='beta5051',
    author_email='beta5051@gmail.com',
    description='Minecraft Bedrock Websocket',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=['websockets>=8.1']
)
