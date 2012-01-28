from setuptools import setup, find_packages

from podcast import __version__ as version

setup(
    name="mezzanine-podcast",
    version=version,
    author="Lee Carpenter",
    author_email="elcarpie@gmail.com",
    description="A simple podcast manager for the Mezzanine CMS",
    long_description=open("README.rst").read(),
    license="BSD",
    url="https://github.com/carpie/mezzanine-podcast",
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),

    install_requires=[
        "mezzanine >= 0.12",
        "grappelli_safe >= 0.1.9",
        "filebrowser_safe",
        "south",
        "PIL",
    ],

    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Software Development :: Libraries :: "
                                            "Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)

