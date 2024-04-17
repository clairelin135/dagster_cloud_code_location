from setuptools import find_packages, setup

setup(
    name="quickstart_etl",
    packages=find_packages(exclude=["quickstart_etl_tests"]),
    install_requires=[
        "dagster==1.7.2rc2",
        "dagster-plus==1.7.2rc2",
        "boto3",
        "pandas",
        "matplotlib",
        "gql",
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
