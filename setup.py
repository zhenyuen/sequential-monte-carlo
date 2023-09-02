"""Python setup.py for sequential_monte_carlo package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("sequential_monte_carlo", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="sequential_monte_carlo",
    version=read("sequential_monte_carlo", "VERSION"),
    description="Awesome sequential_monte_carlo created by zhenyuen",
    url="https://github.com/zhenyuen/sequential-monte-carlo/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="zhenyuen",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["sequential_monte_carlo = sequential_monte_carlo.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
