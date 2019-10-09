import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dummy",
    version="0.0.1",
    author="Tiago de Freitas Pereira",
    author_email="tiagofrepereira@gmail.com",
    description="Dummy Project",
    long_description=long_description,
    long_description_content_type="",
    url="https://github.com/tiagofrepereira2012/dummy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    
    entry_points={
        'console_scripts' : [
          'dummy_print.py = dummy.dummy:dummy_print',
        ],
    }
)
