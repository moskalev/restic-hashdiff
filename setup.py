import setuptools
from datetime import datetime

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="restic_hashdiff", # Replace with your own name
    version="0.1." + datetime.now().strftime("%m%d.%H-%M"),
    author="Alexandr Moskalev",
    author_email="moskalev@umich.edu",
    description="A program to find differences between local filesystem and a restic snapshot based on SHA256 hashes. Requires a custom restic client to generate input file with block hashes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/moskalev/restic-hashdiff",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    install_requires=[
        'pandas'
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    entry_points={
        "console_scripts": [
            "restic-hashdiff = restic-hashdiff.__main__:main"
        ]
    }
)
