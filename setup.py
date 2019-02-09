from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="rebus",
    version="0.1",
    keywords="puzzles",
    packages=["rebus"],
    url="https://github.com/gmarmstrong/rebus",
    author="Guthrie McAfee Armstrong",
    author_email="guthrie.armstrong@gmail.com",
    description="Generates rebuses",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3"
        "Topic :: Artistic Software",
        "Topic :: Games/Entertainment :: Puzzle Games",
        ],
    install_requires=[
        "nltk",
        "flask"
        ]
)
