from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="relatusengine", 
    version="1.0.0",
    author="Ashton Benson",
    author_email="ashtonbenson305@gmail.com",
    description="A barebone and adaptable game engine for creating dynamic RPGs", 
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AshtonBenson/RelatusEngine",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[ 
        "textblob",
    ],
    extras_require={ 
        "dev": ["pytest>=6.0"],
    },
    entry_points={ 
        "console_scripts": [
            "run-relatus=RelatusEngine.run_game:main",
        ],
    },
    include_package_data=True, 
)
