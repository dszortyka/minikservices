"""A setuptools based setup module.
"""


from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

requirements = (here / "requirements.txt").read_text(encoding="utf-8")



setup(

    name="minikservices",
    version="0.0.5",
    license='MIT',
    description="App to start, stop and view minikube services easily.",
    long_description = long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dszortyka/minikservices",  
    author="Daniel Szortyka",  
    author_email="daniel.szortyka@gmail.com",  
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        #"Programming Language :: Python :: 3.7",
        #"Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],

    keywords="minikube, k8s, minikube services",
    package_dir={"": "src"},  
    packages=find_packages(where="src"),
    install_requires=[
        'setuptools',
        'wheel',
        'kubernetes==24.2.0',
        'prettytable==3.4.1'
    ],
    python_requires=">=3.9, <4",
    
    entry_points={  
        "console_scripts": [
            "kservice=kservice.main:main",
        ],
    },
    
    project_urls={  
        "Bug Reports": "https://github.com/dszortyka/minikservices/issues",
        "Funding": "https://donate.pypi.org",
        #"Say Thanks!": "http://saythanks.io/to/minikservices",
        "Source": "https://github.com/dszortyka/minikservices/",
    },
)