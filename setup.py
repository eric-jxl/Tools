# -*- coding:utf-8 -*-

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="eric_tools",
    version="1.4.0",
    author="Eric",
    author_email="jxleric95@gmail.com",
    description="Python Daily Development Tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Eric-jxl/Tools",
    packages=setuptools.find_packages(),
    keyword=["eric", "tools"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
    install_requires=[
        'psycopg2',
        'requests',
        'Pillow',
        'xlsxwriter',
        "ImageHash",
    ]
)
