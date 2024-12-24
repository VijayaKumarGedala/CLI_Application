from setuptools import setup, find_packages

setup(
    name="my_cli_app",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "click",
    ],
    entry_points={
        'console_scripts': [
            'calc = calculator.calc:main',
        ],
    },
)
