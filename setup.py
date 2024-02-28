"""
Setup of the duka_smartfan_sdk module
"""
from setuptools import setup

setup(
    name="duka_smartfan_sdk",
    version="0.1.0",
    description="Duka Smartfan Wifi ventilation SDK",
    long_description=(
        "SDK for connection to the Duka Smartfan Wifi ventilation. "
        "Made for interfacing to home assistant"
    ),
    author="Jens Østergaard Nielsen, Søren Howe Gersager",
    url="https://github.com/dingusdk/dukaonesdk",
    packages=["duka_smartfan_sdk"],
    license="GPL-3.0",
)
