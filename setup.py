#!/usr/bin/env python3

from setuptools import setup, find_packages

requirements = [
    "galaxy_importer==0.1.3b8",
    "packaging",
    "pulpcore~=3.0rc7",
    "PyYAML",
    "semantic_version",
]

with open("README.rst") as f:
    long_description = f.read()

setup(
    name="pulp-ansible",
    version="0.2.0b6.dev",
    description="Pulp plugin to manage Ansible content, e.g. roles",
    long_description=long_description,
    license="GPLv2+",
    author="Pulp Ansible Plugin Project Developers",
    author_email="pulp-dev@redhat.com",
    url="https://github.com/pulp/pulp_ansible",
    install_requires=requirements,
    extras_require={
        "test": [
            "coverage",
            "flake8",
            "flake8-docstrings",
            "flake8-quotes",
            "flake8-tuple",
            "mock",
            "pulp-smash",
            "pytest",
        ]
    },
    include_package_data=True,
    packages=find_packages(exclude=["tests"]),
    classifiers=(
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: POSIX :: Linux",
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ),
    entry_points={"pulpcore.plugin": ["pulp_ansible = pulp_ansible:default_app_config"]},
)
