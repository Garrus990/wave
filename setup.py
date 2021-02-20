from setuptools import setup, find_packages

setup(
    name="wavemaker-task",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ["*.pkl", "*/*.pkl"],
    },
    install_requires=[
        'numpy',
        'pandas',
        'tensorflow',
        'tqdm',
        'sklearn',
        'scipy',
        'requests'
    ]
)

