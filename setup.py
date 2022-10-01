"""A setuptools based setup module.
"""


from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")


setup(

    name="minikservices",  # Required
    version="0.0.1",  # Required
    description="Start and Stop minikube services in background easily.",  # Optional
    long_description_content_type="text/markdown",  # Optional (see note above)
    url="https://github.com/pypa/sampleproject",  # Optional
    author="Daniel Szortyka",  # Optional
    author_email="daniel.szortyka@gmail.com",  # Optional
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        # Pick your license as you wish
        "License :: OSI Approved :: MIT License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate you support Python 3. These classifiers are *not*
        # checked by 'pip install'. See instead 'python_requires' below.
        "Programming Language :: Python :: 3",
        #"Programming Language :: Python :: 3.7",
        #"Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        #"Programming Language :: Python :: 3.10",
        #"Programming Language :: Python :: 3 :: Only",
    ],

    keywords="minikube, k8s, minikube services",
    package_dir={"": "src"},  # Optional
    packages=find_packages(where="src"),  # Required
    python_requires=">=3.7, <4",
    #extras_require={  # Optional
    #    "dev": ["check-manifest"],
    #    "test": ["coverage"],
    #},
    
    entry_points={  # Optional
        "console_scripts": [
            "kservice=kservice.main:main",
        ],
    },
    
    project_urls={  # Optional
        "Bug Reports": "https://github.com/dszortyka/minikservices/issues",
        "Funding": "https://donate.pypi.org",
        "Say Thanks!": "http://saythanks.io/to/minikservices",
        "Source": "https://github.com/dszortyka/minikservices/",
    },
)