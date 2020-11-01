import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="temptracker-jacob-martinez",
    version="0.0.1",
    author="Jacob Martinez",
    author_email="jacob@magnetic-lab.com",
    description="A test application for recording and performing math on temperature readings.",
    license="GNU General Public License v3 or later (GPLv3+)",
     platforms=["POSIX", "Windows"],
     py_modules=["temptracker"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jacobmartinez3d/temptracker",
    packages=setuptools.find_packages(include="temptracker"),
    classifiers=[
             "Development Status :: 2 - Pre-Alpha",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.1",
            "Programming Language :: Python :: 3.2",
            "Programming Language :: Python :: 3.3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: POSIX"
    ],
    python_requires=">=2.7, <3.9"
)
