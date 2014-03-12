#!/usr/bin/python

from distutils.core import setup

setup(name="EWSWrapper", version="0.2",
      description="Python wrapper functions for easy use of Microsoft Exchange Web Services",
      author="Michael Korzeniowski", author_email="mko_san@lafiel.net",
      packages=["EWSWrapper"], package_data={"EWSWrapper": ["wsdl/*"]})
