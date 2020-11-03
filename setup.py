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
    platforms=["POSIX", "Windows", "MacOS X"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jacobmartinez3d/temptracker",
    packages=setuptools.find_packages(include="temptracker"),
    classifiers=[
            "Development Status :: 2 - Pre-Alpha",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: POSIX",
            "Operating System :: MacOS :: MacOS X"
    ],
    python_requires=">=2.7, <=3.9"
)
