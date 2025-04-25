from setuptools import setup, find_packages

setup(
    name="ipdb-precommit",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'remove-ipdb=ipdb_precommit.pre_commit_hook:main',
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A pre-commit hook to remove ipdb statements from Python files",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ipdb-precommit",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 