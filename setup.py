from setuptools import setup, find_packages

setup(
    name='TREX_Core',
    version='0.0.1',
    install_requires=[
                "python-socketio<=4.6.1",
                "tensorflow>=2.0"],
    packages=find_packages()
    )

