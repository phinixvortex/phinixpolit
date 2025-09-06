from setuptools import setup, find_packages

setup(
    name="phinixpolit",
    version="1.0.0",
    py_modules=["phinixpolit"],
    install_requires=[
        "colorama>=0.4.6",
        "python-whois>=0.7.3",
    ],
    entry_points={
        "console_scripts": [
            "phinixpolit=phinixpolit:main",
        ],
    },
    author="phinixvortex",
    description="PhinixPolit - A cybersecurity multi-tool for port scanning, recon, and more.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/phinixvortex/phinixpolit",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.8",
)
