from setuptools import setup, find_packages

setup(
    name='lord_of_the_rings_sdk',
    version='1.0.0',
    author='Luis Chacon',
    description='Python SDK for the Lord of the Rings API',
    long_description='A Python SDK that provides access to the Lord of the Rings API for retrieving movie and quote data.',
    long_description_content_type='text/markdown',
    url='https://github.com/LChacon41/LuisChacon-SDK',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)