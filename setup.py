from setuptools import setup, find_packages

setup(
    name="tweet-cli-tool",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "tweepy",
    ],
    entry_points={
        'console_scripts': [
            'tweet=tweet_cli_tool.cli:main',
        ],
    },
    author="Your Name",
    description="A simple command-line tool for posting tweets",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
)