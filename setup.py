import io
from setuptools import setup, find_packages

def readme():
    with io.open('README.md', encoding='utf-8') as f:
        return f.read()

def requirements(filename):
    reqs = list()
    with io.open(filename, encoding='utf-8') as f:
        for line in f.readlines():
            reqs.append(line.strip())
    return reqs


setup(
    name="fpypeline",
    version="0.0.1",
    author="Álvaro Calzado",
    author_email="ac28042@hotmail.com",
    url='https://fpypeline.readthedocs.io/',
    description="A Python package template to illustrate a complete building pipeline.",
    long_description=readme(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=requirements(filename='requirements/requirements.txt'),
    extras_require={
        "dev": requirements(filename='requirements/dev-requirements.txt'),
    },
    include_package_data=True,
    project_urls={
        'Source': 'https://github.com/QuantumA/full-python-pipeline',
        'Documentation': 'https://fpypeline.readthedocs.io/'
    },
)