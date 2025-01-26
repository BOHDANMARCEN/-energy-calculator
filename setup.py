from setuptools import setup, find_packages

setup(
    name="energy-calculator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.7",
    author="Your Name",
    author_email="your.email@example.com",
    description="Калькулятор для обчислення та конвертації електроенергії",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/username/energy-calculator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "energy-calculator=energy_calculator:main",
        ],
    },
)