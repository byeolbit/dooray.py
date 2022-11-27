from setuptools import setup

setup(
    name='dooray.py',
    version='0.1',
    description='Dooray! messenger slash command wrapper',
    author='Yeonwoo Jo',
    author_email='yeonwoo.jo.92@gmail.com',
    url='https://github.com/byeolbit/dooray.py',
    license='MIT',
    install_requires=['flask'],
    packages=['dooray'],
    keywords=['dooray'],
    python_requires='>=3.8',
    package_data={},
)
