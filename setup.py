import setuptools

setuptools.setup(
    name="rondlib",
    version="0.0.1",
    author="Rondinelli Morais",
    author_email="rondinellimorais@gmail.com",
    description="A small example package",
    long_description="A simple description",
    long_description_content_type="text/markdown",
    url="https://github.com/rondinellimorais/rondlib",
    project_urls={
        "Bug Tracker": "https://github.com/rondinellimorais/rondlib/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)