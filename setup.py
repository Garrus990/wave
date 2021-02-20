from setuptools import setup, find_packages

setup(
    name="phenotype-predictions",
    version="0.0.6",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ["*.pkl", "*/*.pkl"],
    },
    install_requires=[
        'numpy',
        'pandas<=0.24.2',
        'tqdm',
        'sklearn',
        'scipy',
        'requests'
    ]
)

