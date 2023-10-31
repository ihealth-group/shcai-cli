from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="shcaicli",
    version="0.0.1",
    author="iHealth Group",
    author_email="rafael.morais@ihealthgroup.com.br",
    description="SHC.Ai Cli",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.ihealthgroup.com.br",
    project_urls={
        "Bug Tracker": "https://github.com/ihealth-group/shcai-cli/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "boto3==1.24.71",
        "antlr4-python3-runtime==4.13.1",
    ],
)