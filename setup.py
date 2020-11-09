import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="flask_tinify",
    version="1.0.0",
    description="An adaption of tinify as a flask extension",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/minecraftschurli/flask_tinify",
    author="Minecraftschurli",
    author_email="minecraftschurli@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    packages=["flask_tinify"],
    include_package_data=True,
    install_requires=["flask"],
)
