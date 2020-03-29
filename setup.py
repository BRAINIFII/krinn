import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="krinn", # Replace with your own username
    version="0.0.1",
    author="Kritik Bangera",
    author_email="bangerakritik@gmail.com",
    description="This module helps in getting the price or title of a product",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BRAINIFII/krinn",
    packages={"krinn"},
    install_requires=[
        "bs4",
        "requests",
        "user_agents",
        ],
    extras_require = {
        "devlp":[
            "pytest>=3.7",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)