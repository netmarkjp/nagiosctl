from setuptools import setup

setup(
    name="nagiosctl",
    version="1.1.0",
    description="control multiple nagios",
    author="Toshiaki Baba",
    author_email="toshiaki@netmark.jp",
    url="https://github.com/netmarkjp/nagiosctl",
    install_requires=["click", "paramiko", "PyYAML", "requests", ],
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ],
    scripts=["bin/nagiosctl", ],
)
