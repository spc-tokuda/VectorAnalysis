import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vector_analysis",
    version="0.0.1",
    author="tetuji okuda",
    author_email="tokuda@sciencepark.co.jp",
    description="how to culculate gradient, divergence and curl",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/y-takefuji/agci",
    project_urls={
        "Bug Tracker": "https://github.com/y-takefuji/agci",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    py_modules=['VectorAnalysis'],
    packages=setuptools.find_packages(where="VectorAnalysis"),
    python_requires=">=3.8",
    entry_points = {
        'console_scripts': [
            'VectorAnalysis = VectorAnalysis:main'
        ]
    },
)