from setuptools import setup, find_packages

setup(
    name="claude_helper",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "anthropic",
        "python-dotenv"
    ]
)